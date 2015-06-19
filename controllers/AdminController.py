#/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import abort, flash, redirect, render_template

from models import User
from utils import Database
from config import Urls


def view(q = "SELECT table_name FROM information_schema.tables;", res = None) :
	if User.session.exists() or True : # Remove this!
		if True or User.session.get().isAdmin() : # And this!
			return render_template("admin.html", query = q, result = res)
		else :
			abort(403)
	return redirect(Urls.home)

def execute(form) :
	query = form.get("query")
	res = None
	try :
		res = Database.exeq(query)
	except Exception as e :
		flash(e, "danger")
	else :
		flash(u"Befehl erfolgreich ausgeführt!", "success")
	return view(query, res)
