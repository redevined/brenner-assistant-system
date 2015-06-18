#/usr/bin/env python

from utils import Database
from config import Months


class Course() :

	def __init__(self, name, date, time, role) :
		self.id = None
		self.name = name
		self.date = date
		self.time = time
		self.role = role


def _format(date) :
	return ".".join(date.split("-")[::-1])

def _dateSortKey(course) :
	return map(int, course.date.split(".")[::-1])


def add(username, info) :
	course = Course(info.get("name"), _format(info.get("date")), (info.get("time_start"), info.get("time_end")), info.get("role"))
	Database.storeCourse(username, course)

def getAll(username) :
	data = Database.loadCourses(username)
	courses = [Course(*obj) for obj in data]
	return sorted(courses, key = _dateSortKey)

def getAllGrouped(username) :
	courses = dict()
	for course in getAll(username) :
		day, month, year = course.date.split(".")
		month = Months.get[int(month) - 1]
		if not courses.has_key(year) :
			courses[year] = dict()
		if not courses[year].has_key(month) :
			courses[year][month] = list()
		courses[year][month].append(course)
	return courses

def delete(username, id) :
	Database.deleteCourse(username, id)

def deleteAll(username) :
	Database.deleteCourses(username)
