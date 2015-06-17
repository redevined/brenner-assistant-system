#/usr/bin/env python

from flask import session

from Compression import decode, encode


class UserSession() :

	def __init__(self, key) :
		self.session = session
		self.key = key

	def get(self) :
		user = self.session.get(self.key)
		if user :
			return decode(user)

	def set(self, user) :
		if user :
			self.session[self.key] = encode(user)

	def remove(self) :
		self.session.pop(self.key, None)

	def exists(self) :
		return self.session.has_key(self.key)

	def remember(self, val) :
		self.session.permanent = val
