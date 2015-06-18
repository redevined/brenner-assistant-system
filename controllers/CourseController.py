#/usr/bin/env python

from flask import redirect, render_template

from models import User, Course
from config import Urls


def view() :
	user = User.session.get()
	courses = Course.getAll(user.username)
	return render_template("courses.html", user = user, courses = courses)

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

def update(id, form) :
	if User.session.exists() :
		user = User.session.get()
		Course.delete(user.username, id)
		Course.add(user.username, form)
	return redirect(Urls.home)

def submit() :
	if User.session.exists() :
		user = User.session.get()
		grouped_courses = Course.getAllGrouped(user.username)
		for year, months in grouped_courses.items() :
			for month, courses in months.items() :
				sheet = render_template("sheet.html", user = user, courses = courses, year = year, month = month)
				# Some cool magic...
				# Course.deleteAll(user.username)
	return redirect(Urls.home)
