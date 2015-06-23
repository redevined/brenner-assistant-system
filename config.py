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
		"login" 			: 	"/login",
		"logout"			:	"/logout",
		"register"			:	"/register",
		"courseAdd"			:	"/course/add",
		"courseDelete"		:	"/course/delete",
		"courseUpdate"		:	"/course/update",
		"courseSubmit"		:	"/course/submit",
		"admin"				:	"/admin",
		"github"			:	"https://github.com/redevined/brenner-assistants-system"
	}
)

# User roles
Roles = ConfigObject.create(
	{
		"user" 				: 	"USER",
		"admin" 			: 	"ADMIN"
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
									"Januar",
									"Februar",
									u"März",
									"April",
									"Mai",
									"Juni",
									"Juli",
									"August",
									"September",
									"Oktober",
									"November",
									"Dezember"
								]
	}
)
