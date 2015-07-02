#/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import abort, flash, redirect, render_template

from models import User, Course, Sheet
from utils import Log
from config import Urls, Months, Msgs


def view(pdf = "") :
	user = User.session.get()
	courses = Course.getAll(user.username)
	months = { u"{0} {1}".format(Months.get[int(course.date.split(".")[1]) - 1], course.date.split(".")[2]) for course in courses }
	if pdf :
		return dowload({ "pdf" : pdf })
	return render_template("courses.html", user = user, courses = courses, months = months, pdf = pdf)

def add(form) :
	if User.session.exists() :
		user = User.session.get()
		Course.add(user.username, form)
	return redirect(Urls.home)

def delete(id) :
	if User.session.exists() :
		user = User.session.get()
		Course.delete(user.username, id)
	return redirect(Urls.home)

def submit(form) :
	if User.session.exists() :
		user = User.session.get()
		courses = Course.getAll(user.username)
		selected = [ pair.split() for pair in form.getlist("selected[]") ]
		if selected :
			pdf = Sheet.generate(user, courses, selected, form.get("destructive"))
			flash(u"Kurs-Auflistung erfolgreich erstellt, der Download beginnt in Kürze.", Msgs.success)
			return view(Sheet.encode(pdf))
		else :
			flash(u"Keine Monate ausgewählt!", Msgs.warn)
	else :
		return abort(403)
	return redirect(Urls.home)

def download(form) :
	if User.session.exists() :
		pdf = Sheet.decode(form.get("pdf"))
		return pdf.render()
	else :
		return abort(403)
