#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib
import sys

from welcome_page import WelcomePage
from browser_page import BrowserPage	
from extras_page import ExtrasPage
from office_page import OfficePage

office = None
browser = None
extras = []

class MainWindow(Gtk.ApplicationWindow):
	def __init__(self, app):
		super().__init__(application=app)
		self.set_title("Yavix Setup")
		self.set_default_size(600, 400)
		self.set_resizable(False)

		self.stack = Gtk.Stack()
		self.set_child(self.stack)

		self.welcome_page = WelcomePage()
		self.browser_page = BrowserPage()
		self.extras_page = ExtrasPage()
		self.office_page = OfficePage()

		self.stack.add_named(self.welcome_page, "welcome")
		self.stack.add_named(self.browser_page, "browser")
		self.stack.add_named(self.extras_page, "extras")
		self.stack.add_named(self.office_page, "office")


		self.welcome_page.start_button.connect("clicked", self.show_browser_page)
		self.browser_page.next_button.connect("clicked", self.show_extras_page)
		self.extras_page.next_button.connect("clicked", self.show_office_page)
		
		self.stack.set_visible_child_name("welcome")

	def show_browser_page(self, button):
		self.stack.set_visible_child_name("browser")
	
	def show_extras_page(self, button):
		self.stack.set_visible_child_name("extras")

	def show_office_page(self, button):
		self.stack.set_visible_child_name("office")

class SetupApp(Adw.Application):
	def __init__(self):
		super().__init__(application_id="com.luigiano-code.Yavix-installer")

	def do_activate(self):
		win = MainWindow(self)
		win.present()

if __name__ == "__main__":
	app = SetupApp()
	app.run(sys.argv)
