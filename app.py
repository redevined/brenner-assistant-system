#/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, request

from controllers import AdminController, CourseController, HomeController, LoginController, RegisterController
from models import User
from utils.Interface import ViewInterface
from config import Config


app = Flask(__name__)
app.secret_key = Config.secret_key
app.jinja_env.globals.update(_ = ViewInterface())


@app.route(Config.Urls.App.home)
def home() :
	return HomeController.view()

@app.route(Config.Urls.App.about)
def about() :
	return HomeController.about()

@app.route(Config.Urls.App.admin, methods = ["GET", "POST"])
def admin() :
	if request.method == "POST" :
		return AdminController.execute(request.form)
	return AdminController.view()


@app.route(Config.Urls.App.login, methods = ["GET", "POST"])
def login() :
	if request.method == "POST" :
		return LoginController.login(request.form)
	return LoginController.view()

@app.route(Config.Urls.App.register, methods = ["GET", "POST"])
def register() :
	if request.method == "POST" :
		return RegisterController.register(request.form)
	return RegisterController.view()

@app.route(Config.Urls.App.logout)
def logout() :
	return LoginController.logout()


@app.route(Config.Urls.App.course_add, methods = ["POST"])
def courseAdd() :
	return CourseController.add(request.form)

@app.route(Config.Urls.App.course_delete + "/<int:id>")
def courseDelete(id) :
	return CourseController.delete(id)

@app.route(Config.Urls.App.course_submit, methods = ["POST"])
def courseSubmit() :
	return CourseController.submit(request.form)

@app.route(Config.Urls.App.download_sheet)
def downloadSheet() :
	return CourseController.download()


@app.errorhandler(403)
def error403(e) :
	return HomeController.error(403, e)

@app.errorhandler(404)
def error404(e) :
	return HomeController.error(404, e)

@app.errorhandler(405)
def error405(e) :
	return HomeController.error(405, e)

@app.errorhandler(500)
def error500(e) :
	return HomeController.error(500, e)


if __name__ == "__main__" :
	app.run(debug = Config.debug)
