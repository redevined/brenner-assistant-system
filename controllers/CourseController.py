#/usr/bin/env python

from flask import redirect, render_template

from models import User, Course, Sheet
from config import Urls, Months


def view() :
	user = User.session.get()
	courses = Course.getAll(user.username)
	day, month, year = course.date.split(".")
	months = { "{0} {1}".format(Months.get[int(month) - 1], year) for course in courses }
	return render_template("courses.html", user = user, courses = courses, months = months)

def add(form) :
	if User.session.exists() :
		user = User.session.get()
		Course.add(user.username, form)
	return redirect(Urls.home)

def delete(id) :
	if User.session.exists() :
		user = User.session.get()
		Course.delete(user.username, id)
	return redirect(Urls.home)

def submit(form) :
	if User.session.exists() :
		user = User.session.get()
		courses = Course.getAll(user.username)
		pdf = Sheet.generate(user, courses, [ pair.split() for pair in form.get("selected") ])
		return pdf.render()
	return redirect(Urls.home)
