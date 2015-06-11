#/usr/bin/env python

from flask import redirect, render_template

from models import User, Course
from config import Notifications, Logger, Urls


def view() :
	user = User.session.get()
	courses = Course.getAll(user.username)
	#return render_template("view.html", courses = courses)
	return "Your courses!"

def add(form) :
	if User.session.exists() :
		user = User.session.get()
		Course.add(user.username, form)
		Logger.info("controllers::courseController::add User {0} added a new course".format(user.username))
	return redirect(Urls.home)

def delete(id) :
	if User.session.exists() :
		user = User.session.get()
		Course.delete(user.username, id)
		Logger.info("controllers::courseController::add User {0} deleted course #{1}".format(user.username, id))
	return redirect(Urls.home)

def update(id, form) :
	if User.session.exists() :
		user = User.session.get()
		Course.delete(id)
		Course.add(user.username, form)
		Logger.info("controllers::courseController::add User {0} updated course #{1}".format(user.username, id))
	return redirect(Urls.home)
