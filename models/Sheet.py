#/usr/bin/env python

import pickle
from base64 import b64encode, b64decode
from flask import render_template, url_for
from flask_weasyprint import HTML, CSS, render_pdf

from utils import Database, Log
from config import Months


class Sheet() :

	def __init__(self, user, courses) :
		self.user = user
		self.courses = courses
		self.filename = "Auflistung_{0}.pdf".format(user.username)
		self.template = "sheet.html"

	def render(self) :
		html = HTML(string = render_template(
			self.template,
			user = self.user,
			all_courses = self.courses
		))
		css = [ CSS(url_for("static", filename = "css/bootstrap.min.css")) ]
		doc = render_pdf(html, stylesheets = css, download_filename = self.filename)
		return doc


def _keys(li) :
	return [ item[0] for item in li ]

def _values(li, key) :
	for item in li :
		if item[0] == key :
			return item[1]

def generate(user, courses, selected, destructive) :
	Log.info("Generating sheet for", user = user.username)
	grouped = list()
	for course in courses :
		day, month, year = course.date.split(".")
		month = Months.get[int(month) - 1]
		if [month, year] in selected :
			if year not in _keys(grouped) :
				grouped.append((year, list()))
			if month not in _keys(_values(grouped, year)) :
				_values(grouped, year).append((month, list()))
			_values(_values(grouped, year), month).append(course)
			if destructive :
				Database.deleteCourse(user.username, course.id)
	sheet = Sheet(user, grouped)
	return sheet

def encode(sheet) :
	return pickle.dumps(sheet).replace("\n", "\\n")

def decode(data) :
	return pickle.loads(data.replace("\\n", "\n"))
