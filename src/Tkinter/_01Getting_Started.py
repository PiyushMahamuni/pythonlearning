#!/usr/bin/env/python

import tkinter as tk

# in tkinter everything is a widget - button, text, frame
# the first thing you create is sort of the root widget - window for GUI

root = tk.Tk()

# Hello world of tkinter

# you want to print hello world inside a window, basically a label
# So we'll use label widget

# To create anything in tkinter, is almost always two step process.
# You define the thing and create it and then you put it up on the screen.

# creating label
HelloLabel = tk.Label(root, text="Hello World!", font=20)
# params - where the label goes, what is it's text

# Now we have to display or put this widget in our root window
# There are couple of different ways to put things on the screen. The first one is
# pack. Packing is placing the widget at the first available spot, very basic not so sophisticated

HelloLabel.pack() # packing the label in the root widget, line 19

# The last thing we want to create is the event loop, and what an event loop is, when you
# have a GUI, the program is always looping constantly BTS and tracking inputs from user
# to figure out what to do next

root.mainloop() # the main loop of the widget