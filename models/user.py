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
	user = Database.loadUser(credentials["username"])
	if user :
		if user.password == Compression.hash(credentials["password"]) :
			return user

def getByRegister(credentials) :
	username, password = credentials["username"], credentials["password"]
	if username and password :
		if not Database.existsUser(username) :
			user = User(username, password)
			if Database.storeUser(user) :
				return user
