#/usr/bin/env python

from flask import flash, redirect, render_template

from models import User
from config import Urls


def view() :
	return render_template("register.html")

def register(form) :
	User.session.set(User.getByRegister(form))
	if User.session.exists() :
		return redirect(Urls.home)
	else :
		flash("Der Benutzername ist bereits vergeben.")
	return redirect(Urls.register)