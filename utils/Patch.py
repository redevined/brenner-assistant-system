#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from config import Config
from utils import Database, Log


# All patches that need to be executed
PATCHES = lambda : [
	#createTables,
	grantAdminRights
]


# Call to execute all registered patches
def execute() :
	patches = PATCHES()
	Log.warn("Starting patches!", remaining = len(patches))
	for patch in patches :
		try :
			patch.start()
		except Exception as e :
			Log.error("Patch went wrong", exception = e)
	Log.warn("All patches done.")


# Wrapper class for patch task
class Patch() :

	def __init__(self, task) :
		self.task = task
		self.key = "<Patch: {name}>".format(name = task.__name__)

	def log(self, *msgs, **vals) :
		Log.info(self.key, *msgs, **vals)

	def start(self, *args) :
		self.log("---- Start! ----")
		self.task(self.log, *args)
		self.log("--- Finished ---")


# Create all database tables
# 20.08.15
@Patch
def createTables(log = Log.info) :
	log("Creating table 'users'...")
	Database.exeq("CREATE TABLE users (username varchar(255) PRIMARY KEY, password varchar(255), role varchar(255));")
	log("Table 'users' created.")

	log("Creating table 'courses'...")
	Database.exeq("CREATE TABLE courses (id serial PRIMARY KEY, username varchar(255) REFERENCES users (username) ON UPDATE CASCADE ON DELETE CASCADE, name varchar(255), date varchar(255), time varchar(255), role varchar(255));")
	log("Table 'courses' created.")

	log("Creating table 'sheets'...")
	Database.exeq("CREATE TABLE sheets (id serial PRIMARY KEY, username varchar(255) REFERENCES users (username) ON UPDATE CASCADE ON DELETE CASCADE, courses text);")
	log("Table 'sheets' created.")


# Grant admin rights to all users
# 20.08.15
@Patch
def grantAdminRights(log = Log.info) :
	log("Granting admin rights to all users...")
	Database.exeq("UPDATE users SET role=%s;", Config.User.Roles.admin)
	log("Rights granted.")
