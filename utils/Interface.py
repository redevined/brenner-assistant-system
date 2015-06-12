#/usr/bin/env python


class ViewInterface() :

	from flask import request
	from datetime import datetime

	from models import User, Course
	from config import Urls
