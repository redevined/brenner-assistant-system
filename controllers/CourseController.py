#/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import abort, flash, redirect, render_template

from models import User, Course, Sheet
from utils import Log
from config import Config


def view(pdf = u"") :
	user = User.session.get()
	courses = Course.getAll(user.username)
	months = Course.calcMonths(courses)
	return render_template("courses.html", user = user, courses = courses, months = months, pdf = pdf)

def add(form) :
	if User.session.exists() :
		user = User.session.get()
		Course.add(user.username, form)
	return redirect(Config.Urls.App.home)

def delete(id) :
	if User.session.exists() :
		user = User.session.get()
		Course.delete(user.username, id)
	return redirect(Config.Urls.App.home)

def submit(form) :
	if User.session.exists() :
		user = User.session.get()
		courses = Course.getAll(user.username)
		selected = [ pair.split() for pair in form.getlist("selected[]") ]
		if selected :
			sid = Sheet.generate(user, courses, selected, form.get("destructive")) # TODO: Save in session cookie
			flash(u"Kurs-Auflistung erfolgreich erstellt, der Download beginnt in Kürze.", Config.Flash.success)
			return view(sid)
		else :
			flash(u"Keine Monate ausgewählt!", Config.Flash.warn)
	else :
		return abort(403)
	return redirect(Config.Urls.App.home)

def download(id) :
	if User.session.exists() :
		Log.debug("Create PDF")
		pdf = Sheet.getById(User.session.get(), id)
		Log.debug(pdf = pdf)
		if not Config.Course.keep_sheets :
			Sheet.deleteById(id)
		return pdf.render()
	else :
		return abort(403)
