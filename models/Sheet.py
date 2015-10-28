#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pickle
from base64 import b64decode, b64encode
from flask import render_template, url_for
from config import Config
from utils import Database
from utils import Log
try :
	from flask_weasyprint import HTML, CSS, render_pdf
except ImportError as e :
	Log.error("Could not import flask_weasyprint", exception = e)


class Sheet() :

	def __init__(self, user, courses, sid = None) :
		self.id = sid
		self.user = user
		self.courses = courses
		self.filename = u"Auflistung_{0}.pdf".format(user.username)
		self.template = "sheet.html"

	def render(self) :
		html = HTML(string = render_template(
				self.template,
				user = self.user,
				all_courses = self.courses
			),
			encoding = Config.encoding
		)
		css = [ CSS(url_for("static", filename = "css/bootstrap.min.css")) ]
		doc = render_pdf(html, stylesheets = css, download_filename = self.filename.encode(Config.encoding))
		return doc


def _keys(li) :
	return [ item[0] for item in li ]

def _values(li, key) :
	for item in li :
		if item[0] == key :
			return item[1]

def generate(user, courses, selected, destructive) :
	grouped = list()
	for course in courses :
		day, month, year = course.date.split(".")
		month = Config.Months[month]
		if [month, year] in selected :
			if year not in _keys(grouped) :
				grouped.append((year, list()))
			if month not in _keys(_values(grouped, year)) :
				_values(grouped, year).append((month, list()))
			_values(_values(grouped, year), month).append(course)
			if destructive :
				Database.deleteCourse(user.username, course.id)
	return storeWithId(user, grouped)

def storeWithId(user, courses) :
	data = b64encode(pickle.dumps(courses)).decode(Config.encoding)
	sid = Database.storeSheetWithId(user.username, data)
	return sid

def getById(user, sid) :
	data, sid = Database.loadSheet(user.username, sid)
	courses = pickle.loads(b64decode(data))
	sheet = Sheet(user, courses, sid)
	return sheet

def getAll(user) :
	data = Database.loadSheets(user.username)
	sheets = [
		Sheet(user, pickle.loads(b64decode(cdata)), sid)
		for cdata, sid in data
	]
	return sheets

def delete(username, sid) :
	Database.deleteSheet(username, sid)
