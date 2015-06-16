#/usr/bin/env python

from flask import flash, redirect, render_template

from models import User
from config import Notifications, Urls


def view() :
	return render_template("login.html")

def login(form) :
	User.session.set(User.getByLogin(form))
	if User.session.exists() :
		if form.get("remember") :
			User.session.remember(True)
		return redirect(Urls.home)
	else :
		flash(Notifications.login_error)
	return redirect(Urls.login)

def logout() :
	if User.session.exists() :
		User.session.remove()
		flash(Notifications.logout)
	return redirect(Urls.login)
