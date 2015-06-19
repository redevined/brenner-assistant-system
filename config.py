#/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, urlparse

from utils import ConfigObject


# Database connection
urlparse.uses_netloc.append("postgres")
Connection = urlparse.urlparse(
	os.environ["DATABASE_URL"]
)

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
