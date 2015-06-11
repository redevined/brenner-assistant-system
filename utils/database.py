#/usr/bin/env python

import redis

from Compression import decode, encode
from config import Db, Keys, Functions


db = redis.StrictRedis(host = Db.host, port = Db.port)


def loadUser(un) :
	user = db.hget(un, Keys.user_data)
	if user :
		return decode(user)

def storeUser(user) :
	res1 = db.hset(user.username, Keys.user_data, encode(user))
	if res1 :
		res2 = db.hset(user.username, Keys.course_incr, Functions.newId())
	return res1 and res2

def deleteUser(un) :
	return db.delete(un)

def existsUser(un) :
	return db.exists(un)

def loadCourses(un) :
	courses = [ decode(value) for key, value in db.hgetall(un).items() if key not in (Keys.user_data, Keys.course_incr) ]
	return courses

def storeCourse(un, course) :
	course.id = db.hget(un, Keys.course_incr)
	res1 = db.hset(un, Keys.course_incr, Functions.incId(course.id))
	if res1 :
		res2 = db.hset(un, course.id, encode(course))
	return res1 and res2

def deleteCourse(un, id) :
	return db.hdel(un, id)
