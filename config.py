#/usr/bin/env python

import hashlib, pickle
from base64 import b64encode, b64decode


# Routing URLS
Urls = type(
	"config.Urls", (),
	{
		"home" 				: 	"/",
		"login" 			: 	"/login",
		"register"			:	"/register",
		"logout"			:	"/logout",
		"courseAdd"			:	"/course/add",
		"courseDelete"		:	"/course/delete/<int:id>",
		"courseUpdate"		:	"/course/update/<int:id>"
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
		"login_error" 		: 	"Ung&uml;ltige Benutzereingaben.",
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

# Various functions
Functions = type(
	"config.Functions", (),
	{
		"hash"				:	lambda _, s		: 	hashlib.sha1(s).hexdigest(),
		"newId" 			: 	lambda _		:	hex(0),
		"incId"				:	lambda _, i		:	hex(int(i, 16) + 1),
		"encode"			:	lambda _, o		: 	b64encode(pickle.dumps(o)),
		"decode" 			: 	lambda _, o		:	pickle.loads(b64decode(o))
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
