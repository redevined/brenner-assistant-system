#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import abort, flash, redirect, render_template
from config import Config
from models import User
from utils import Hash, Log


def view() :
	if User.session.exists() :
		return render_template("user.html")
	else :
		return abort(403)

def update(form) :
	if User.session.exists() :
		user = User.session.get()
		un, un_repeat = form.get("username"), form.get("username-repeat")
		pw, pw_repeat = form.get("password"), form.get("password-repeat")
		if un != un_repeat :
			flash(u"Bitte wiederhole den neuen Benutzernamen korrekt!", Config.Flash.error)
		elif pw != pw_repeat :
			flash(u"Bitte wiederhole das neue Passwort korrekt!", Config.Flash.error)
		elif not (un or pw) :
			flash(u"Keine Änderungen eingegeben.", Config.Flash.warn)
		else :
			Log.debug("Updating user", username = un, password = pw)
			user.update(username = un, password = Hash.hash(pw))
			Log.debug("User updated, setting session", user = user.__dict__)
			User.session.set(user)
			Log.debug("Session set", user = User.session.get().__dict__)
			flash(u"Neue Eingaben wurden erfolgreich übernommen.", Config.Flash.success)
	return redirect(Config.Urls.App.user)
