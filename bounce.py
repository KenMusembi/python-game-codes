from tkinter import * 
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1000, height=800, bd=0, highlightthickness=0)
tk.update()

class Ball:
	def _init_(self, canvas, color):
		self.canvas = canvas

