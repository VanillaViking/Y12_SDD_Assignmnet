import pygame
import threading
from button import *
from text_input import *

class starting_screen():
    def __init__(DISPLAY):
        self.display = DISPLAY
        self.exit_btn = button()

