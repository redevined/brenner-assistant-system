#/usr/bin/env python
# -*- coding: UTF-8 -*-


class ViewInterface() :

	from flask import request
	from datetime import datetime

	from models import User, Course
	from config import Urls
