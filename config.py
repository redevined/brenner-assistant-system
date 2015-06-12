#/usr/bin/env python
# -*- coding: UTF-8 -*-

import hashlib, pickle
from base64 import b64encode, b64decode


# Routing URLS
Urls = type(
	"config.Urls", (),
	{
		"home" 				: 	"/",
		"about"				:	"/about",
		"login" 			: 	"/login",
		"logout"			:	"/logout",
		"register"			:	"/register",
		"courseAdd"			:	"/course/add",
		"courseDelete"		:	"/course/delete/<int:id>",
		"courseUpdate"		:	"/course/update/<int:id>",
		"github"			:	"https://github.com/redevined/brenner-assistants-system"
	}
)()

# Redis connection
Db = type(
	"config.Db", (),
	{
		"host"				:	"localhost",
		"port"				:	6379
	}
)()

# Session and database keys
Keys = type(
	"config.Keys", (),
	{
		"session"			:	"user",
		"user_data" 		: 	"USERDATA",
		"course_incr"		:	"COURSEINCR"
	}
)()

# Flash messages
Notifications = type(
	"config.Notifications", (),
	{
		"login_error" 		: 	u"Ungültige Anmeldedaten.",
		"register_error"	:	"Der Benutzername ist bereits vergeben.",
		"logout" 			: 	"Du wurdest erfolgreich abgemeldet."
	}
)()

# User roles
Roles = type(
	"config.Roles", (),
	{
		"user" 				: 	"USER",
		"admin" 			: 	"ADMIN"
	}
)()

# Wrapper for app.logger for global accessability
Logger = type(
	"config.Logger", (),
	{
		"set"				:	lambda _, o		: 	setattr(_, "logger", o),
		"info" 				: 	lambda _, *a	:	_.logger.info(*a) if hasattr(_, "logger") else None,
		"warn"	 			: 	lambda _, *a	:	_.logger.warning(*a) if hasattr(_, "logger") else None,
		"debug" 			: 	lambda _, *a	:	_.logger.debug(*a) if hasattr(_, "logger") else None
	}
)()
