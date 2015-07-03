#/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, urlparse

from utils import ConfigObject, Log


# Database connection
try :
	urlparse.uses_netloc.append("postgres")
	Connection = urlparse.urlparse(
		os.environ["DATABASE_URL"]
	)
except Exception as e :
	Log.error("No environment variable with the name 'DATABASE_URL' found", exception = e.message)
	Connection = None

# Routing URLS
Urls = ConfigObject.create(
	{
		"home" 				: 	"/",
		"about"				:	"/about",
		"admin"				:	"/admin",
		"login" 			: 	"/login",
		"logout"			:	"/logout",
		"register"			:	"/register",
		"courseAdd"			:	"/course/add",
		"courseDelete"		:	"/course/delete",
		"courseSubmit"		:	"/course/submit",
		"downloadSheet"		:	"/course/download",
		"github"			:	"https://github.com/redevined/brenner-assistants-system",
		"mail"				:	"wirtholiv@gmail.com"
	}
)

# User roles
Roles = ConfigObject.create(
	{
		"user" 				: 	u"USER",
		"admin" 			: 	u"ADMIN"
	}
)

# Flash message categories
Msgs = ConfigObject.create(
	{
		"success"			: 	"success",
		"warn"				: 	"warn",
		"error"				: 	"error"
	}
)

# Localized month names
Months = ConfigObject.create(
	{
		"get" 				: 	[
									u"Januar",
									u"Februar",
									u"März",
									u"April",
									u"Mai",
									u"Juni",
									u"Juli",
									u"August",
									u"September",
									u"Oktober",
									u"November",
									u"Dezember"
								]
	}
)
