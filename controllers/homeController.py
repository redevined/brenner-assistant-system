#/usr/bin/env python

from flask import render_template

from models import User
import CourseController
from config import Logger


def view() :
	if User.session.exists() :
		return CourseController.view()
	return render_template("home.html")

def about() :
	#return render_template("about.html")
	return "About this project."

def error(code) :
	#return render_template("error.html", code = code), code
	return "Error!"
