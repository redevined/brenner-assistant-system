#/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import flash, redirect, render_template

from models import User
from config import Urls, Msgs


def view() :
	return render_template("login.html")

def login(form) :
	User.session.set(User.getByLogin(form))
	if User.session.exists() :
		if form.get("remember") :
			User.session.remember(True)
		return redirect(Urls.home)
	else :
		flash(u"Ungültige Anmeldedaten.", Msgs.error)
	return redirect(Urls.login)

def logout() :
	if User.session.exists() :
		User.session.remove()
		flash("Du wurdest erfolgreich abgemeldet.", Msgs.success)
	return redirect(Urls.login)
