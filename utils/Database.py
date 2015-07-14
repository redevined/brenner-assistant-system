#/usr/bin/env python
# -*- coding: UTF-8 -*-

import psycopg2 as pgsql

from utils import Log
from config import Config


def exeq(query, *params) :
	with db.cursor() as cursor :
		cursor.execute(query, params)
		if set(query.upper().split()) & {"SELECT", "RETURNING"} :
			res = [ [str(field).decode(Config.coding) for field in record] for record in cursor.fetchall() ]
			return res


def checkTables() :
	Log.info("Performing table check")
	tables = [ res[0] for res in exeq("SELECT table_name FROM information_schema.tables;") ]
	if "users" not in tables :
		createUserTable()
	if "courses" not in tables :
		createCourseTable()
	if "sheets" not in tables :
		createSheetTable()
	
def createUserTable() :
	Log.warn("No table 'users' found, creating new")
	exeq("CREATE TABLE users (username varchar(255) PRIMARY KEY, password varchar(255), role varchar(255));")

def createCourseTable() :
	Log.warn("No table 'courses' found, creating new")
	exeq("CREATE TABLE courses (id serial PRIMARY KEY, username varchar(255) REFERENCES users (username), name varchar(255), date varchar(255), time varchar(255), role varchar(255));")

def createSheetTable() :
	Log.warn("No table 'sheets' found, creating new")
	exeq("CREATE TABLE sheets (id serial PRIMARY KEY, username varchar(255) REFERENCES users (username), courses text);")


def loadUserByLogin(un, pw) :
	data = exeq("SELECT username, password, role FROM users WHERE username=%s AND password=%s;", un, pw)
	return data[0] if data else None

def loadUser(un) :
	data = exeq("SELECT username, password, role FROM users WHERE username=%s;", un)
	return data[0] if data else None

def storeUser(user) :
	exeq("INSERT INTO users (username, password, role) VALUES (%s, %s, %s);", user.username, user.password, user.role)

def deleteUser(un) :
	exeq("DELETE FROM users WHERE username=%s;", un)
	deleteCourses(un)

def existsUser(un) :
	return loadUser(un) is not None


def loadCourses(un) :
	data = exeq("SELECT name, date, time, role, id FROM courses WHERE username=%s;", un)
	return data

def storeCourse(un, course) :
	exeq("INSERT INTO courses (username, name, date, time, role) VALUES (%s, %s, %s, %s, %s);", un, course.name, course.date, course.time, course.role)

def deleteCourse(un, id) :
	exeq("DELETE FROM courses WHERE username=%s AND id=%s;", un, id)

def deleteCourses(un) :
	exeq("DELETE FROM courses WHERE username=%s;", un)


def loadSheet(id) :
	data = exeq("SELECT courses, id FROM sheets WHERE id=%s;", id)
	return data[0] if data else None

def storeSheetWithId(un, courses) :
	id = exeq("INSERT INTO sheets (username, courses) VALUES (%s, %s) RETURNING id;", un, courses)
	return id[0][0] if id else None

def deleteSheet(id) :
	exeq("DELETE FROM sheets WHERE id=%s;", id)


try :
	if not Config.Db.Connection :
		raise OSError("No environment variable 'DATABASE_URL' found")
	db = pgsql.connect(
		database = Config.Db.Connection.path[1:],
		user = Config.Db.Connection.username,
		password = Config.Db.Connection.password,
		host = Config.Db.Connection.hostname,
		port = Config.Db.Connection.port
	)
except Exception as e :
	Log.error("Connection to PostgreSQL database could not be established, please check your connection settings", exception = e)
else :
	db.autocommit = True
	checkTables()
