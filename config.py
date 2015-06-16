#/usr/bin/env python
# -*- coding: UTF-8 -*-

import hashlib, pickle
from base64 import b64encode, b64decode

from utils import ConfigObject


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
		"github"			:	"https://github.com/redevined/brenner-assistants-system"
	}
)

# Redis connection
Connection = ConfigObject.create(
	{
		"host"				:	"localhost",
		"port"				:	6379
	}
)

# Session and database keys
Keys = ConfigObject.create(
	{
		"session"			:	"user",
		"user_data" 		: 	"USERDATA",
		"course_incr"		:	"COURSEINCR"
	}
)

# Flash messages
Notifications = ConfigObject.create(
	{
		"login_error" 		: 	u"Ungültige Anmeldedaten.",
		"register_error"	:	"Der Benutzername ist bereits vergeben.",
		"logout" 			: 	"Du wurdest erfolgreich abgemeldet."
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
									"März",
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
