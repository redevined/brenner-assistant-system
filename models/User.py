#/usr/bin/env python

import time, hashlib

from utils import Session, Database
from config import Roles


session = Session.UserSession("user")


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
