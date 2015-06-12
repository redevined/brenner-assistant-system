#/usr/bin/env python

import redis

from Compression import decode, encode
from config import Db, Keys, Logger


db = redis.StrictRedis(host = Db.host, port = Db.port)
if not db.ping() :
	Logger.warn("utils::Database::__main__ No running Redis instance found, please check your connection settings")


def loadUser(un) :
	user = db.hget(un, Keys.user_data)
	if user :
		return decode(user)

def storeUser(user) :
	db.hincrby(user.username, Keys.course_incr, 1)
	return db.hset(user.username, Keys.user_data, encode(user))

def deleteUser(un) :
	return db.delete(un)

def existsUser(un) :
	return db.exists(un)

def loadCourses(un) :
	courses = [ decode(value) for key, value in db.hgetall(un).items() if key not in (Keys.user_data, Keys.course_incr) ]
	return courses

def storeCourse(un, course) :
	course.id = db.hget(un, Keys.course_incr)
	db.hincrby(un, Keys.course_incr, 1)
	return db.hset(un, course.id, encode(course))

def deleteCourse(un, id) :
	return db.hdel(un, id)

def optimize(un) :
	courses = { int(key) : value for key, value in db.hgetall(un).items() if key not in (Keys.user_data, Keys.course_incr) }
	for id, key in enumerate(sorted(courses.keys()), 1) :
		db.hdel(un, key)
		db.hset(un, id, courses[key])

def optimizeAll() :
	for key in db.keys("*") :
		optimize(key)
