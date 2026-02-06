#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib
import sys

from welcome_page import WelcomePage
from browser_page import BrowserPage	

browser = None

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

		self.stack.add_named(self.welcome_page, "welcome")
		self.stack.add_named(self.browser_page, "browser")

		self.welcome_page.start_button.connect("clicked", self.show_browser_page)
		
		self.stack.set_visible_child_name("welcome")

	def show_browser_page(self, button):
		self.stack.set_visible_child_name("browser")

class SetupApp(Adw.Application):
	def __init__(self):
		super().__init__(application_id="com.luigiano-code.Yavix-installer")

	def do_activate(self):
		win = MainWindow(self)
		win.present()

if __name__ == "__main__":
	app = SetupApp()
	app.run(sys.argv)
