#/usr/bin/env python

import time

from utils import Session, Database, Compression, Log
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


def getByLogin(credentials) :
	data = Database.loadUser(credentials.get("username"), Compression.hash(credentials.get("password")))
	Log.debug(data)
	if data :
		user = User(*data)
		return user

def getByRegister(credentials) :
	username, password = credentials.get("username"), credentials.get("password")
	if not Database.existsUser(username) :
		user = User(username, Compression.hash(password))
		Log.debug(user)
		Database.storeUser(user)
		return user
