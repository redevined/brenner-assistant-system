#/usr/bin/env python

from flask import flash, redirect, render_template

from models import User
from config import Notifications, Logger, Urls


def view() :
	return render_template("login.html")

def login(form) :
	User.session.set(User.getByLogin(form))
	if User.session.exists() :
		Logger.info("controllers::loginController::login User {0} logged in".format(form["username"]))
		return redirect(Urls.home)
	else :
		Logger.warn("controllers::loginController::login Failed login with username '{0}'".format(form["username"]))
		flash(Notifications.login_error)
	return redirect(Urls.login)

def logout() :
	if User.session.exists() :
		Logger.info("controllers::loginController::logout User {0} logged out".format(User.session.get().username))
		User.session.remove()
		flash(Notifications.logout)
	return redirect(Urls.login)
