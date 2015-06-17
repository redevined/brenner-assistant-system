#/usr/bin/env python

from flask import render_template

print "HC - Starting imports..."
from controllers import CourseController
from models import User


def view() :
	if User.session.exists() :
		return CourseController.view()
	return render_template("home.html")

def about() :
	return render_template("about.html")

def error(code) :
	return render_template("error.html", code = code), code
