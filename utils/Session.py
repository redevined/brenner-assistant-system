#/usr/bin/env python

import time
from threading import Thread
from flask import session as cookie

from utils import Log


class SessionContainer(dict) :

	def add(self, obj) :
		key = self.lowestKey()
		self[key] = obj
		return key

	def get(self, key) :
		if self.has_key(key) :
			return self[key]

	def remove(self, key) :
		if self.has_key(key) :
			del self[key]

	def lowestKey(self, key = 0) :
		if key in self.keys() :
			return self.lowestKey(key + 1)
		else :
			return key


class SessionCleaner() :

	def __init__(self, objs, timeout = 60*30) :
		self.objects = objs
		self.timeout = timeout
		self.run = False

	def __del__(self) :
		self.stop()

	def start(self, interval = 60) :
		Log.info("Starting cleaner thread", check_interval = interval, session_timeout = self.timeout)
		self.run = True
		Thread(target = self.clean, args = (interval,)).start()

	def stop(self) :
		Log.info("Stopping cleaner thread")
		self.run = False

	def clean(self, interval) :
		while self.run :
			Log.debug("Cleaning...")
			now = time.time()
			for key, obj in self.objects.items() :
				if now - obj.timestamp > self.timeout :
					del self.objects[key]
			time.sleep(interval)


class UserSession() :

	def __init__(self, name, clean = False) :
		self.name = name
		self.sessions = SessionContainer()
		self.cleaner = SessionCleaner(self.sessions)
		if clean :
			self.cleaner.start()

	def get(self) :
		key = cookie.get(self.name)
		return self.sessions.get(key)

	def set(self, user) :
		key = self.sessions.add(user)
		cookie[self.name] = key

	def remove(self) :
		key = cookie.pop(self.name, None)
		self.sessions.remove(key)

	def exists(self) :
		user = self.get()
		return user is not None

	def refresh(self) :
		Log.debug("Session::refresh", user = self.get())
		user = self.get()
		if user :
			user.refresh()

	def remember(self, val) :
		cookie.permanent = val
