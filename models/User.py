#/usr/bin/env python

from utils import Session, Database, Compression, Log
from config import Roles


session = Session.UserSession("user")


class User() :

	def __init__(self, username, password, role = Roles.user) :
		self.username = username
		self.password = Compression.hash(password)
		self.role = role

	def checkPassword(self, pw) :
		return self.password == Compression.hash(pw)

	def isAdmin(self) :
		return self.role == Roles.admin


def getByLogin(credentials) :
	data = Database.loadUser(credentials.get("username"))
	Log.debug(data)
	if data :
		user = User(*data)
		log.debug(user)
		if user.checkPassword(credentials.get("password")) :
			return user

def getByRegister(credentials) :
	username, password = credentials.get("username"), credentials.get("password")
	if not Database.existsUser(username) :
		user = User(username, password)
		Log.debug(user)
		Database.storeUser(user)
		return user
