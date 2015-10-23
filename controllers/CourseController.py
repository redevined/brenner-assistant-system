#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import abort, flash, redirect, render_template
from config import Config
from models import User, Course, Sheet


def view() :
	user = User.session.get()
	courses = Course.getAll(user.username)
	months = Course.calcMonths(courses)
	pdf = User.session.hasTemp()
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
			sid = Sheet.generate(user, courses, selected, form.get("destructive"))
			User.session.setTemp(sid)
			flash(u"Kurs-Auflistung erfolgreich erstellt, der Download beginnt in Kürze.", Config.Flash.success)
		else :
			flash(u"Keine Monate ausgewählt!", Config.Flash.warn)
	else :
		return abort(403)
	return redirect(Config.Urls.App.home)

def downloadSheet(sid = None) :
	if User.session.exists() :
		if sid is None :
			sid = User.session.getTemp()
		if sid is not None :
			pdf = Sheet.getById(User.session.get(), sid)
			return pdf.render()
	return abort(403)

def deleteSheet(sid) :
	if User.session.exists() :
		user = User.session.get()
		Sheet.delete(user.username, sid)
	return redirect(Config.Urls.App.user)
