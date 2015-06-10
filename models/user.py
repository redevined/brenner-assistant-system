#/usr/bin/env python

from utils import session, database as db
from config import Roles, Keys, Functions


session = session.UserSession(Keys.session)


class User() :

	def __init__(self, username, password, role = Roles.user) :
		self.username = username
		self.password = Functions.hash(password)
		self.role = role


def getByLogin(credentials) :
	user = db.loadUser(credentials["username"])
	if user :
		if user.password == Functions.hash(credentials["password"]) :
			return user

def getByRegister(credentials) :
	username, password = credentials["username"], credentials["password"]
	if username and password :
		if not db.existsUser(username) :
			user = User(username, password)
			if db.storeUser(user) :
				return user
