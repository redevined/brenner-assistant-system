#/usr/bin/env python

import time, hashlib
from flask import session as cookie

#from utils import Session, Database
from utils import Database
from config import Roles


#session = Session.UserSession("user")


class User() :

	def __init__(self, username, password, role = Roles.user) :
		self.username = username
		self.password = password
		self.role = role
		self.refresh()

	def refresh(self) :
		self.timestamp = time.time() 

	def isAdmin(self) :
		return self.role == Roles.admin


class Session() :

	def __init__(self, key) :
		self.key = key

	def get(self) :
		username = cookie.get(self.key)
		data = Database.loadUserFromSession(username)
		return User(*data)

	def set(self, user) :
		cookie[self.key] = user.username

	def remove(self) :
		cookie.pop(self.key, None)

	def exists(self) :
		return cookie.has_key(self.key)

	def remember(self, val = True) :
		cookie.permanent = val


session = Session("user")


def _hash(pw) :
	hashed = hashlib.sha1(pw)
	return hashed.hexdigest()


def getByLogin(credentials) :
	data = Database.loadUser(credentials.get("username"), _hash(credentials.get("password")))
	if data :
		user = User(*data)
		return user

def getByRegister(credentials) :
	username, password = credentials.get("username"), credentials.get("password")
	if not Database.existsUser(username) :
		user = User(username, _hash(password))
		Database.storeUser(user)
		return user
