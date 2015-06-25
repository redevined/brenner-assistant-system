#/usr/bin/env python

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
		Log.debug("Rendering...")
		html = HTML(string = render_template(
			self.template,
			user = self.user,
			all_courses = self.courses
		))
		Log.debug(rendered_html = html)
		css = [ CSS(url_for("static", filename = "css/bootstrap.min.css")) ]
		doc = render_pdf(html, stylesheets = css)#, download_filename = self.filename)
		log.debug(rendered_pdf = doc)
		return doc


def generate(user, courses, selected) :
	Log.info("Generating sheet for", user = user.username)
	grouped = dict()
	for course in courses :
		day, month, year = course.date.split(".")
		month = Months.get[int(month) - 1]
		if [month, year] in selected :
			if not grouped.has_key(year) :
				grouped[year] = dict()
			if not grouped[year].has_key(month) :
				grouped[year][month] = list()
			grouped[year][month].append(course)
			#Database.deleteCourse(user.username, course.id)
	sheet = Sheet(user, grouped)
	return sheet
