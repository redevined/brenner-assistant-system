#/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import flash, redirect, render_template

from models import User
from config import Config


def view() :
	return render_template("register.html")

def register(form) :
	User.session.set(User.getByRegister(form))
	if User.session.exists() :
		flash(u"Willkommen, {name}. Hier findest du eine Übersicht deiner Kurse. Bevor du beginnst, lies dir bitte das <a href=\"{link}\">FAQ</a> durch!".format(name = User.session.get().username, link = Config.Urls.App.about), Config.Flash.success)
		return redirect(Config.Urls.App.home)
	else :
		flash(u"Der Benutzername ist bereits vergeben.", Config.Flash.warn)
	return redirect(Config.Urls.App.register)
