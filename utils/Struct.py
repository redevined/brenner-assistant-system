#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Easy accessable dict supporting 'object.key' syntax
class Struct(dict) :

	def __init__(self, obj, *args, **kwargs) :
		for key, val in obj.items() :
			if isinstance(val, dict) :
				obj[key] = Struct(val)
		super(Struct, self).__init__(obj, *args, **kwargs)

	def __getattribute__(self, attr) :
		if attr[0] == "_" :
			return object.__getattribute__(self, attr[1:])
		else :
			return self[attr]

	def __setattr__(self, attr, val) :
		if attr[0] == "_" :
			object.__setattr__(self, attr[1:], val)
		else :
			self[attr] = val

	def __iter__(self) :
		for key, val in self._items() :
			yield (key, val)