#/usr/bin/env python

from flask import render_template

from models import user
import courseController
from config import Logger


def view() :
	if user.session.exists() :
		return courseController.view()
	#return render_template("home.html")
	return "Welcome home!"

def error(code) :
	#return render_template("error.html", code = code), code
	return "Error!"
