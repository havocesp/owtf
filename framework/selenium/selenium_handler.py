#!/usr/bin/env python
'''
owtf is an OWASP+PTES-focused try to unite great tools and facilitate pen testing
Copyright (c) 2011, Abraham Aranguren <name.surname@gmail.com> Twitter: @7a_ http://7-a.org
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;

The random module allows the rest of the framework to have access to random functionality
'''
from framework.lib.general import *

class Selenium:
	def __init__(self, Core):
		self.Core = Core
		self.Init = False

	def SetDisplay(self):
		cprint("Setting Selenium's display ..")
		from pyvirtualdisplay import Display
                self.Display = Display(visible=0, size=(800, 600))
                self.Display.start()

	def SetDriver(self):
		cprint("Setting Selenium's driver ..")
		from selenium import webdriver
                self.Driver = webdriver.Firefox()
                self.Driver.implicitly_wait(30)

	def InitSelenium(self):
		if not self.Init: # Perform this expensive operation only once
			self.Init = True
			cprint("Initialising Selenium please wait ..")
			self.SetDisplay()
			self.SetDriver()

	def CreateURLLauncher(self, Args):
		self.InitSelenium()
		from framework.selenium import url_launcher
		return url_launcher.URLLauncher(self, Args['BASE_URL'], Args['INPUT_FILE'])
