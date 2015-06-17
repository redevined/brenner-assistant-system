#/usr/bin/env python

from utils import Session, Database, Compression
from config import Roles, Keys


session = Session.UserSession(Keys.session)


class User() :

	def __init__(self, username, password, role = Roles.user) :
		self.username = username
		self.password = Compression.hash(password)
		self.role = role


def getByLogin(credentials) :
	user = Database.loadUser(credentials.get("username"))
	if user :
		if user.password == Compression.hash(credentials.get("password")) :
			return user

def getByRegister(credentials) :
	username, password = credentials.get("username"), credentials.get("password")
	if username and password :
		if not Database.existsUser(username) :
			user = User(username, password)
			if Database.storeUser(user) :
				return user
