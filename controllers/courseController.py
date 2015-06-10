#/usr/bin/env python

from flask import redirect, render_template

from models import user, course
from config import Notifications, Logger


def view() :
	u = user.session.get()
	c = course.getAll(u.username)
	#return render_template("view.html", courses = c)
	return "Your courses!"

def add(form) :
	if user.session.exists() :
		u = user.session.get()
		course.add(u.username, form)
		Logger.info("controllers::courseController::add User {0} added a new course".format(u.username))
	return redirect("/")

def delete(id) :
	if user.session.exists() :
		u = user.session.get()
		course.delete(u.username, id)
		Logger.info("controllers::courseController::add User {0} deleted course #{1}".format(u.username, id))
	return redirect("/")

def update(id, form) :
	if user.session.exists() :
		u = user.session.get()
		course.delete(id)
		course.add(u.username, form)
		Logger.info("controllers::courseController::add User {0} updated course #{1}".format(u.username, id))
	return redirect("/")
