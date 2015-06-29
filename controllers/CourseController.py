#/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import flash, redirect, render_template

from models import User, Course, Sheet
from utils import Log
from config import Urls, Months, Msgs


def view() :
	user = User.session.get()
	courses = Course.getAll(user.username)
	months = { "{0} {1}".format(Months.get[int(course.date.split(".")[1]) - 1], course.date.split(".")[2]) for course in courses }
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
		selected = [ pair.split() for pair in form.getlist("selected[]") ]
		if selected :
			pdf = Sheet.generate(user, courses, selected, form.get("destructive"))
			flash("Kurs-Auflistung erfolgreich erstellt.", Msgs.success)
			return pdf.render() # TODO: refresh after download
		else :
			flash(u"Keine Monate ausgewählt!", Msgs.warn)
	return redirect(Urls.home)
