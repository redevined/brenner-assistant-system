#/usr/bin/env python

from flask import session as cookie

from utils import Database, Log


class UserSession() :

	def __init__(self, cls) :
		self.key = cls.__name__
		self.UserCls = cls

	def get(self) :
		if self.exists() :
			username = cookie.get(self.key)
			data = Database.loadUserFromSession(username)
			return self.UserCls(*data)

	def set(self, user) :
		Log.info("Setting user session", user = user.username)
		if user :
			cookie[self.key] = user.username

	def remove(self) :
		Log.info("Removing user session")
		cookie.pop(self.key, None)

	def exists(self) :
		return cookie.has_key(self.key)

	def remember(self, val = True) :
		cookie.permanent = val
