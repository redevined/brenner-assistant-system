#/usr/bin/env python

from utils import Session, Database, Compression
from config import Roles


session = Session.UserSession("user")


class User() :

	def __init__(self, username, password, role = Roles.user) :
		self.username = username
		self.password = Compression.hash(password)
		self.role = role


def getByLogin(credentials) :
	data = Database.loadUser(credentials.get("username"))
	if data :
		user = User(*data)
		if user.password == Compression.hash(credentials.get("password")) :
			return user

def getByRegister(credentials) :
	username, password = credentials.get("username"), credentials.get("password")
	if username and password :
		if not Database.existsUser(username) :
			user = User(username, password)
			Database.storeUser(user)
			return user
