#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import session as cookie
from utils import Database


class UserSession() :

	def __init__(self, cls) :
		self.key = cls.__name__
		self.temp_key = "temp"
		self.UserCls = cls

	def get(self) :
		if self.exists() :
			username = cookie.get(self.key)
			data = Database.loadUser(username)
			if data :
				return self.UserCls(*data)

	def set(self, user) :
		if user :
			cookie[self.key] = user.username

	def remove(self) :
		cookie.pop(self.key, None)

	def exists(self) :
		return cookie.has_key(self.key)

	def remember(self, val = True) :
		cookie.permanent = val

	def getTemp(self) :
		return cookie.pop(self.temp_key, None)

	def setTemp(self, obj) :
		cookie[self.temp_key] = obj

	def hasTemp(self) :
		return cookie.has_key(self.temp_key)
