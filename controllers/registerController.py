#/usr/bin/env python

from flask import flash, redirect, render_template

from models import user
from config import Notifications, Logger


def view() :
	#return render_template("register.html")
	return "Sign yourself up!"

def register(form) :
	user.session.set(user.getByRegister(form))
	if user.session.exists() :
		Logger.info("controllers::registerController::register New user {0} registered and logged in".format(form["username"]))
		return redirect("/")
	else :
		Logger.warn("controllers::registerController::register Failed registering user with username '{0}'".format(form["username"]))
		flash(Notifications.register_error)
	return redirect("/register")
