#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import psycopg2 as pgsql
from config import Config
from utils import Log, Hash


# Try to establish connection
def getConnection(conn) :
	try :
		if not conn :
			raise OSError("No environment variable 'DATABASE_URL' found")
		db = pgsql.connect(
			database = conn.path[1:],
			user = conn.username,
			password = conn.password,
			host = conn.hostname,
			port = conn.port
		)
	except Exception as e :
		Log.error("Connection to PostgreSQL database could not be established, please check your connection settings", exception = e)
	else :
		db.autocommit = True
		return db


DB = getConnection(Config.Db.Connection)


# Execute SQL statement
def exeq(query, *params) :
	with DB.cursor() as cursor :
		cursor.execute(query, params)
		if set(query.upper().split()) & {"SELECT", "RETURNING"} :
			res = [ [str(field).decode(Config.encoding) for field in record] for record in cursor.fetchall() ]
			return res


# Return user by username and password
def loadUserByLogin(un, pw) :
	data = exeq("SELECT username, password, role FROM users WHERE username=%s AND password=%s;", un, pw)
	return data[0] if data else None

# Return user by username
def loadUser(un) :
	data = exeq("SELECT username, password, role FROM users WHERE username=%s;", un)
	return data[0] if data else None

# Write user into database
def storeUser(user) :
	exeq("INSERT INTO users (username, password, role) VALUES (%s, %s, %s);", user.username, user.password, user.role)

# Change username of user
def updateUsername(un, new) :
	exeq("UPDATE users SET username=%s WHERE username=%s;", new, un)

# Change password of user
def updatePassword(un, pw) :
	exeq("UPDATE users SET password=%s WHERE username=%s;", pw, un)

# Delete user by username
def deleteUser(un) :
	exeq("DELETE FROM users WHERE username=%s;", un)

# Check if user is in database
def existsUser(un) :
	return loadUser(un) is not None


# Get all courses in database for user
def loadCourses(un) :
	data = exeq("SELECT name, date, time, role, id FROM courses WHERE username=%s;", un)
	return data

# Write course into database
def storeCourse(un, course) :
	exeq("INSERT INTO courses (username, name, date, time, role) VALUES (%s, %s, %s, %s, %s);", un, course.name, course.date, course.time, course.role)

# Delete specific course by its id
def deleteCourse(un, id) :
	exeq("DELETE FROM courses WHERE username=%s AND id=%s;", un, id)

# Delete all courses
def deleteCourses(un) :
	exeq("DELETE FROM courses WHERE username=%s;", un)


# Return sheet from database
def loadSheet(un, id) :
	data = exeq("SELECT courses, id FROM sheets WHERE username=%s AND id=%s;", un, id)
	return data[0] if data else None

# Load all sheets by user
def loadSheets(un) :
	data = exeq("SELECT courses, id FROM sheets WHERE username=%s;", un)
	return data

# Store sheet and return its id
def storeSheetWithId(un, courses) :
	id = exeq("INSERT INTO sheets (username, courses) VALUES (%s, %s) RETURNING id;", un, courses)
	return id[0][0] if id else None

# Delete sheet
def deleteSheet(un, id) :
	exeq("DELETE FROM sheets WHERE username=%s AND id=%s;", un, id)
