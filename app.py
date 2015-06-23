#/usr/bin/env python

from flask import Flask, request

from controllers import AdminController, CourseController, HomeController, LoginController, RegisterController
from models import User
from utils.Interface import ViewInterface
from config import Urls


app = Flask(__name__)
app.secret_key = "\xf5f\x92\xa9-,\xd6`\x1fvaa_\xed\xc0\xff\x8c\xd0\xb8\xac\xa6\xcb0\xa1"
app.jinja_env.globals.update(app = ViewInterface())


@app.route(Urls.home)
def home() :
	return HomeController.view()

@app.route(Urls.about)
def about() :
	return HomeController.about()


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

@app.route(Urls.courseUpdate + "/<int:id>", methods = ["POST"])
def courseUpdate(id) :
	return CourseController.update(id, request.form)

@app.route(Urls.courseSubmit)
def courseSubmit() :
	return CourseController.submit()


@app.route(Urls.admin, methods = ["GET", "POST"])
def admin() :
	if request.method == "POST" :
		return AdminController.execute(request.form)
	return AdminController.view()

@app.before_request
def refresh() :
	User.session.refresh()


@app.errorhandler(403)
def error403(e) :
	return HomeController.error(403)

@app.errorhandler(404)
def error404(e) :
	return HomeController.error(404)

@app.errorhandler(500)
def error500(e) :
	return HomeController.error(500)


if __name__ == "__main__" :
	app.run(debug = True)
