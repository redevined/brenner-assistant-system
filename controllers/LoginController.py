#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import flash, redirect, render_template
from config import Config
from models import User


def view() :
	return render_template("login.html")

def login(form) :
	User.session.set(User.getByLogin(form))
	if User.session.exists() :
		if form.get("remember") :
			User.session.remember(True)
		flash(u"Willkommen, {name}.".format(name = User.session.get().username), Config.Flash.success)
		return redirect(Config.Urls.App.home)
	else :
		flash(u"Ungültige Anmeldedaten.", Config.Flash.error)
	return redirect(Config.Urls.App.login)

def logout() :
	if User.session.exists() :
		User.session.remove()
		flash(u"Du wurdest erfolgreich abgemeldet.", Config.Flash.success)
	return redirect(Config.Urls.App.login)
