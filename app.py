#/usr/bin/env python

import os
from flask import Flask, request

from controllers import *
from config import Urls, Logger


app = Flask(__name__)
app.secret_key = os.urandom(32)

Logger.set(app.logger)


@app.route(Urls.home)
def home() :
	return homeController.view()

@app.route(Urls.login, methods = ["GET", "POST"])
def login() :
	if request.method == "POST" :
		return loginController.login(request.form)
	return loginController.view()

@app.route(Urls.register, methods = ["GET", "POST"])
def register() :
	if request.method == "POST" :
		return registerController.register(request.form)
	return registerController.view()

@app.route(Urls.logout)
def logout() :
	return loginController.logout()

@app.route(Urls.courseAdd, methods = ["POST"])
def courseAdd() :
	return courseController.add(request.form)

@app.route(Urls.courseDelete, methods = ["POST"])
def courseDelete(id) :
	return courseController.add(id)

@app.route(Urls.courseUpdate, methods = ["POST"])
def courseUpdate(id) :
	return courseController.add(id, request.form)

@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
def throw(error) :
	return homeController.error(error.code)


if __name__ == "__main__" :
	app.run(debug = True)
