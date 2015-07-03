#/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import render_template

from controllers import CourseController
from models import User
from utils import Log


def view() :
	if User.session.exists() :
		return CourseController.view()
	return render_template("home.html")

def about() :
	return render_template("about.html")

def error(code, e) :
	Log.error(exception = e)
	return render_template("error.html", code = code), code
