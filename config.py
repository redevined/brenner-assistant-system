#/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, urlparse

from utils import ConfigObject # TODO: Combine to one object


# Database connection
try :
	urlparse.uses_netloc.append("postgres")
	Connection = urlparse.urlparse(
		os.environ["DATABASE_URL"]
	)
except Exception as e :
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

# System state flags
System = ConfigObject.create(
	{
		"debug"				:	True,
		"update"			:	False,
		"keep"				:	True,
		"encoding"			:	"UTF-8"
	}
)

# User roles
Roles = ConfigObject.create(
	{
		"user" 				: 	u"USER",
		"admin" 			: 	u"ADMIN"
	}
)

# Course roles
CourseRoles = ConfigObject.create(
	{
		"assistant" 		: 	u"Assistent",
		"trainer" 			: 	u"Lehrer"
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
		"01" 				: 	u"Januar",
		"02"				:	u"Februar",
		"03"				:	u"März",
		"04"				:	u"April",
		"05"				:	u"Mai",
		"06"				:	u"Juni",
		"07"				:	u"Juli",
		"08"				:	u"August",
		"09"				:	u"September",
		"10"				:	u"Oktober",
		"11"				:	u"November",
		"12"				:	u"Dezember"
	}
)
