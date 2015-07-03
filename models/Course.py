#/usr/bin/env python

from utils import Database, Log
from config import Months


class Course() :

	def __init__(self, name, date, time, role, id = None) :
		self.id = id
		self.name = name.decode("utf-8")
		self.date = date
		self.time = time
		self.role = role


def _formatDate(date) :
	return ".".join(date.split("-")[::-1])

def _formatTime(start, end) :
	return "{0} - {1}".format(start, end)

def _sortDate(course) :
	return map(int, course.date.split(".")[::-1])


def add(username, info) :
	Log.debug("Course::add" name = info.get("name"), name_type = type(info.get("name")))
	course = Course(
		info.get("name"),
		_formatDate(info.get("date")),
		_formatTime(info.get("time_start"), info.get("time_end")),
		info.get("role")
	)
	Log.debug("Storing course...")
	Database.storeCourse(username, course)
	Log.debug("Course stored.")

def getAll(username) :
	data = Database.loadCourses(username)
	courses = [Course(*obj) for obj in data]
	return sorted(courses, key = _sortDate, reverse = True)

def delete(username, id) :
	Database.deleteCourse(username, id)

def deleteAll(username) :
	Database.deleteCourses(username)
