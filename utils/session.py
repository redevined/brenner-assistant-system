#/usr/bin/env python

from flask import session

from config import Functions


class UserSession() :

	def __init__(self, key) :
		self.session = session
		self.key = key

	def get(self) :
		user = self.session.get(self.key)
		if user :
			return Functions.decode(user)

	def set(self, user) :
		if user :
			self.session[self.key] = Functions.encode(user)

	def remove(self) :
		self.session.pop(self.key, None)

	def exists(self) :
		return self.session.has_key(self.key)
