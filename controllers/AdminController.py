#/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import abort, flash, redirect, render_template

from models import User
from utils import Database, Log
from config import Config


def view(query = u"SELECT * FROM users; -- or courses, sheets", res = None) :
	if User.session.exists() :
		if User.session.get().isAdmin() :
			return render_template("admin.html", query = query, result = res)
		else :
			abort(403)
	return redirect(Config.Urls.App.home)

def execute(form) :
	query = form.get("query")
	res = None
	try :
		Log.debug("Executing sql")
		Log.debug(query = query, byte_query = query.encode(Config.coding))
		res = Database.exeq(query.encode(Config.coding))
		Log.debug(result = res)
	except Exception as e :
		flash(e, Config.Flash.error)
	else :
		flash(u"Befehl erfolgreich ausgeführt!", Config.Flash.success)
	return view(query, res)
