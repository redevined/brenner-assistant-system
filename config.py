#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, urlparse

from utils.Struct import Struct


def _getDbConnection(key) :
	try :
		urlparse.uses_netloc.append(key)
		return urlparse.urlparse(os.environ["DATABASE_URL"])
	except Exception as e :
		return None


Config = Struct(
	{
		"debug" 					:	True,
		"encoding"					:	"UTF-8",
		"secret_key"				:	"/\xfa-\x84\xfeW\xc3\xda\x11%/\x0c\xa0\xbaY\xa3\x89\x93$\xf5\x92\x9eW}",
		"Db" : {
			"Connection"			:	_getDbConnection("postgres")
		},
		"Urls" : {
			"App" : {
				"home" 				: 	"/",
				"about"				:	"/about",
				"admin"				:	"/admin",
				"login" 			: 	"/login",
				"logout"			:	"/logout",
				"register"			:	"/register",
				"course_add"		:	"/course/add",
				"course_delete"		:	"/course/delete",
				"course_submit"		:	"/course/submit",
				"download_sheet"	:	"/course/download",
			},
			"Ext" : {
				"github"			:	u"https://github.com/redevined/brenner-assistants-system",
				"email"				:	u"wirtholiv@gmail.com"
			}
		},
		"Log" : {
			"info"					:	u"INFO",
			"warn"					:	u"WARN",
			"error"					:	u"ERROR",
			"debug"					:	u"DEBUG"
		},
		"Flash" : {
			"success"				: 	"success",
			"warn"					: 	"warn",
			"error"					: 	"error"
		},
		"User" : {
			"Roles" : {
				"user" 				: 	u"USER",
				"admin" 			: 	u"ADMIN"
			}
		},
		"Course" : {
			"Roles" : {
				"assistant" 		: 	u"Assistent",
				"trainer" 			: 	u"Lehrer"
			},
			"keep_sheets"			:	True
		},
		"Months" : {
			"01" 					: 	u"Januar",
			"02"					:	u"Februar",
			"03"					:	u"März",
			"04"					:	u"April",
			"05"					:	u"Mai",
			"06"					:	u"Juni",
			"07"					:	u"Juli",
			"08"					:	u"August",
			"09"					:	u"September",
			"10"					:	u"Oktober",
			"11"					:	u"November",
			"12"					:	u"Dezember"
		}
	}
)
