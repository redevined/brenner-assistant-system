#/usr/bin/env python
# -*- coding: UTF-8 -*-

import time, hashlib
from flask import session as cookie

from utils import Session, Database
from config import Roles


class User() :

	def __init__(self, username, password, role = Roles.user) :
		self.username = username
		self.password = password
		self.role = role

	def isAdmin(self) :
		return self.role == Roles.admin


session = Session.UserSession(User)


def _hash(pw) :
	hashed = hashlib.sha1(pw.encode("utf-8"))
	return hashed.hexdigest()


def getByLogin(credentials) :
	data = Database.loadUserByLogin(credentials.get("username"), _hash(credentials.get("password")))
	if data :
		user = User(*data)
		return user

def getByRegister(credentials) :
	username, password = credentials.get("username"), credentials.get("password")
	if not Database.existsUser(username) :
		user = User(username, _hash(password))
		Database.storeUser(user)
		return user
