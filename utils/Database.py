#/usr/bin/env python

import psycopg2 as pgsql

from config import Connection


def checkTables() :
	db.execute("SELECT table_name FROM informtaion_schema.tables")
	tables = [ res[0] for res in db.fetchall() ]
	if "user" not in tables :
		createUserTable()
	if "course" not in tables :
		createCourseTable()

def createUserTable() :
	print "INFO: No table 'user' found, creating new one."
	db.execute("CREATE TABLE user (username varchar(255), password varchar(255), role varchar(255))")

def createCourseTable() :
	print "INFO: No table 'course' found, creating new one."
	db.execute("CREATE TABLE course (id serial PRIMARY KEY, username varchar(255) REFERENCES user (username), name varchar(255), date varchar(255), time varchar(255), role varchar(255))")


def loadUser(un) :
	db.execute("SELECT username, password, role FROM user WHERE username=%s", (un,))
	return db.fetchone()

def storeUser(user) :
	db.execute("INSERT INTO user (username, password, role) VALUES (%s, %s, %s)", (user.username, user.password, user.role))

def deleteUser(un) :
	db.execute("DELETE FROM user WHERE username=%s", (un,))
	deleteCourses(un)

def existsUser(un) :
	return loadUser(un) is not None


def loadCourses(un) :
	db.execute("SELECT id, name, date, time, role FROM course WHERE username=%s", (un,))
	return db.fetchall()

def storeCourse(un, course) :
	db.execute("INSERT INTO course (username, name, date, time, role) VALUES (%s, %s, %s, %s, %s)", (un, course.name, course.date, course.time, user.role))

def deleteCourse(un, id) :
	db.execute("DELETE FROM course WHERE username=%s and id=%s", (un, id))

def deleteCourses(un) :
	db.execute("DELETE FROM course WHERE username=%s", (un,))


try :
	conn = pgsql.connect(
		database = Connection.path[1:],
		user = Connection.username,
		password = Connection.password,
		host = Connection.hostname,
		port = Connection.port
	)
	db = conn.cursor()
	checkTables()
except Exception :
	print "WARNING: Connection to PostgreSQL database could not be established, please check your connection settings."
