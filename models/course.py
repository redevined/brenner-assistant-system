#/usr/bin/env python

from utils import database as db


class Course() :

	def __init__(self, name, date, start, end, role) :
		self.id = None
		self.name = name
		self.date = date
		self.time = (start, end)
		self.role = role


def add(username, info) :
	course = Course(info.name, info.date, info.start, info.end, info.role)
	return db.storeCourse(username, course)

def getAll(username) :
	courses = db.loadCourses(username)
	return courses

def delete(username, id) :
	return db.deleteCourse(id)
