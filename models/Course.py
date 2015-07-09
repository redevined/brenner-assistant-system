#/usr/bin/env python
# -*- coding: UTF-8 -*-

from utils import Database, Log
from config import Config


class Course() :

	def __init__(self, name, date, time, role, id = None) :
		self.id = id
		self.name = name
		self.date = date
		self.time = time
		self.role = role


def _formatDate(date) :
	return u".".join(date.split("-")[::-1])

def _formatTime(start, end) :
	return u"{0} - {1}".format(start, end)

def _sortDate(course) :
	return map(int, course.date.split(".")[::-1])


def add(username, info) :
	course = Course(
		info.get("name"),
		_formatDate(info.get("date")),
		_formatTime(info.get("time_start"), info.get("time_end")),
		info.get("role")
	)
	Database.storeCourse(username, course)

def getAll(username) :
	data = Database.loadCourses(username)
	courses = [Course(*obj) for obj in data]
	return sorted(courses, key = _sortDate, reverse = True)

def delete(username, id) :
	Database.deleteCourse(username, id)

def deleteAll(username) :
	Database.deleteCourses(username)

def calcMonths(courses) :
	return {
		u"{0} {1}".format(
			Config.Months[course.date.split(".")[1]],
			course.date.split(".")[2]
		) for course in courses
	}