#/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import flash, redirect, render_template

from models import User
from config import Urls, Msgs


def view() :
	return render_template("register.html")

def register(form) :
	User.session.set(User.getByRegister(form))
	if User.session.exists() :
		flash(u"Willkommen, {name}. Hier findest du eine Übersicht deiner Kurse. Bei Fragen wende dich bitte an <a href=\"mailto:{mail}\">{mail}</a>.".format(name = User.session.get().username, mail = Urls.mail), Msgs.success)
		return redirect(Urls.home)
	else :
		flash("Der Benutzername ist bereits vergeben.", Msgs.warn)
	return redirect(Urls.register)
