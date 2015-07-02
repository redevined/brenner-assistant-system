#/usr/bin/env python

from flask import Flask, request

from controllers import AdminController, CourseController, HomeController, LoginController, RegisterController
from models import User
from utils import Log
from utils.Interface import ViewInterface
from config import Urls


app = Flask(__name__)
app.secret_key = "/\xfa-\x84\xfeW\xc3\xda\x11%/\x0c\xa0\xbaY\xa3\x89\x93$\xf5\x92\x9eW}"
app.jinja_env.globals.update(app = ViewInterface())


@app.route(Urls.home)
def home() :
	Log.debug("app::home")
	return HomeController.view()

@app.route(Urls.about)
def about() :
	return HomeController.about()

@app.route(Urls.admin, methods = ["GET", "POST"])
def admin() :
	if request.method == "POST" :
		return AdminController.execute(request.form)
	return AdminController.view()


@app.route(Urls.login, methods = ["GET", "POST"])
def login() :
	if request.method == "POST" :
		return LoginController.login(request.form)
	return LoginController.view()

@app.route(Urls.register, methods = ["GET", "POST"])
def register() :
	if request.method == "POST" :
		return RegisterController.register(request.form)
	return RegisterController.view()

@app.route(Urls.logout)
def logout() :
	return LoginController.logout()


@app.route(Urls.courseAdd, methods = ["POST"])
def courseAdd() :
	return CourseController.add(request.form)

@app.route(Urls.courseDelete + "/<int:id>")
def courseDelete(id) :
	return CourseController.delete(id)

@app.route(Urls.courseSubmit, methods = ["POST"])
def courseSubmit() :
	return CourseController.submit(request.form)

@app.route(Urls.downloadSheet, methods = ["POST"])
def downloadSheet() :
	return CourseController.download(request.form)


@app.errorhandler(403)
def error403(e) :
	Log.error(exception = e.message)
	return HomeController.error(403)

@app.errorhandler(404)
def error404(e) :
	Log.error(exception = e.message)
	return HomeController.error(404)

@app.errorhandler(500)
def error500(e) :
	Log.debug("Oh no!")
	Log.error(exception = e.message)
	return HomeController.error(500)


if __name__ == "__main__" :
	app.run(debug = True)
