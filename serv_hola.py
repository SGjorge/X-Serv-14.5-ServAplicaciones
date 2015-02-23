#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp

class holaApp(webapp.webApp):
	def process(self, parsedRequest):
		return ("200 OK", "<html><body><h1>Hola mundo</h1></body></html>")

if __name__ == "__main__":
	web = holaApp("localhost", 1234)
