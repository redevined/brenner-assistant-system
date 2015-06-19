#/usr/bin/env python

from flask import session

from utils.Compression import decode, encode
from utils import Log


class UserSession() :

	def __init__(self, key) :
		self.session = session
		self.key = key

	def get(self) :
		Log.debug("Session::get", user = self.session.get(self.key))
		user = self.session.get(self.key)
		if user :
			return decode(user)

	def set(self, user) :
		Log.debug("Session::set" user = user)
		if user :
			self.session[self.key] = encode(user)

	def remove(self) :
		self.session.pop(self.key, None)

	def exists(self) :
		Log.debug("Session::exists", exists = self.session.has_key(self.key))
		return self.session.has_key(self.key)

	def remember(self, val) :
		self.session.permanent = val
