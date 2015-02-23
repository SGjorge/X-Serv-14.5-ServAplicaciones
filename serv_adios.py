#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp

class adiosApp(webapp.webApp):
	def process(self, parsedRequest):
		return ("200 OK", "<html><body><h1>Adios mundo cruel</h1></body></html>")

if __name__ == "__main__":
	web = adiosApp("localhost", 1234)