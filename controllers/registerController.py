#/usr/bin/env python

from flask import flash, redirect, render_template

from models import User
from config import Notifications, Logger, Urls


def view() :
	return render_template("register.html")

def register(form) :
	User.session.set(User.getByRegister(form))
	if User.session.exists() :
		Logger.info("controllers::registerController::register New user {0} registered and logged in".format(form["username"]))
		return redirect(Urls.home)
	else :
		Logger.warn("controllers::registerController::register Failed registering user with username '{0}'".format(form["username"]))
		flash(Notifications.register_error)
	return redirect(Urls.register)
