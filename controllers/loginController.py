#/usr/bin/env python

from flask import flash, redirect, render_template

from models import user
from config import Notifications, Logger


def view() :
	#return render_template("login.html")
	return "Come in!"

def login(form) :
	user.session.set(user.getByLogin(form))
	if user.session.exists() :
		Logger.info("controllers::loginController::login User {0} logged in".format(form["username"]))
		return redirect("/")
	else :
		Logger.warn("controllers::loginController::login Failed login with username '{0}'".format(form["username"]))
		flash(Notifications.login_error)
	return redirect("/login")

def logout() :
	if user.session.exists() :
		Logger.info("controllers::loginController::logout User {0} logged out".format(user.session.get().username))
		user.session.remove()
		flash(Notifications.logout)
	return redirect("/login")
