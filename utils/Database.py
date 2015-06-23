#/usr/bin/env python

import psycopg2 as pgsql

from utils import Log
from config import Connection


def exeq(query, *params) :
	with db.cursor() as cursor :
		cursor.execute(query, params)
		if "SELECT" in query :
			return cursor.fetchall()


def checkTables() :
	Log.info("Performing table check")
	tables = [ res[0] for res in exeq("SELECT table_name FROM information_schema.tables;") ]
	if "users" not in tables :
		createUserTable()
	if "courses" not in tables :
		createCourseTable()

def createUserTable() :
	Log.warn("No table 'users' found, creating new")
	exeq("CREATE TABLE users (username varchar(255) PRIMARY KEY, password varchar(255), role varchar(255));")

def createCourseTable() :
	Log.warn("No table 'courses' found, creating new")
	exeq("CREATE TABLE courses (id serial PRIMARY KEY, username varchar(255) REFERENCES users (username), name varchar(255), date varchar(255), time varchar(255), role varchar(255));")


def loadUser(un, pw) :
	data = exeq("SELECT username, password, role FROM users WHERE username=%s AND password=%s;", un, pw)
	return data[0] if data else None

def loadUserFromSession(un) :
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
	data = exeq("SELECT id, name, date, time, role FROM courses WHERE username=%s;", un)
	return data

def storeCourse(un, course) :
	exeq("INSERT INTO courses (username, name, date, time, role) VALUES (%s, %s, %s, %s, %s);", un, course.name, course.date, course.time, user.role)

def deleteCourse(un, id) :
	exeq("DELETE FROM courses WHERE username=%s and id=%s;", un, id)

def deleteCourses(un) :
	exeq("DELETE FROM courses WHERE username=%s;", un)


try :
	db = pgsql.connect(
		database = Connection.path[1:],
		user = Connection.username,
		password = Connection.password,
		host = Connection.hostname,
		port = Connection.port
	)
	db.autocommit = True
	try :
		checkTables()
	except Exception as e :
		Log.error("Exception during table check", exception = str(e).replace("\n", " "))
except Exception as e :
	Log.error("Connection to PostgreSQL database could not be established, please check your connection settings", exception = str(e).replace("\n", " "))
