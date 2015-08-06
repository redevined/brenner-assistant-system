#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
from flask import session as cookie
from config import Config
from utils import Session, Database, Hash


class User() :

	def __init__(self, username, password, role = Config.User.Roles.user) :
		self.username = username
		self.password = password
		self.role = role

	def isAdmin(self) :
		return self.role == Config.User.Roles.admin

	def update(self, username = None, password = None) :
		if username and username != self.username :
			self.username = username
			Database.updateUsername(self.username, username)
		if password and password != self.password :
			self.password = password
			Database.updatePassword(self.username, password)


session = Session.UserSession(User)


def getByLogin(credentials) :
	data = Database.loadUserByLogin(credentials.get("username"), Hash.hash(credentials.get("password")))
	if data :
		user = User(*data)
		return user

def getByRegister(credentials) :
	username, password = credentials.get("username"), credentials.get("password")
	if not Database.existsUser(username) :
		user = User(username, Hash.hash(password))
		Database.storeUser(user)
		return user
