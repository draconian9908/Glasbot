from glob import Globals
from player import *

# Creates a file which maintains the time in the game

class Timer():

    def __init__(self, interval):
        # Initializes the timer and interval - as well if on or off
        self.interval = interval
        self.value = 0
        self.last_int = 0
        self.active = False
        self.on_next = None

    def update(self):
        # Update the timer if on
        if self.active:
            # adds the time based on interval
            self.value += Globals.deltatime / self.interval
            if int(self.value) != int(self.last_int):
                # updates the values in the timer
                self.last_int = int(self.value)
                if self.on_next != None:
                    self.on_next()

    def start(self):
        # Begins the timer
        self.active = True

    def pause(self):
        # Pauses the timer
        self.active = False

    def stop(self):
        # Stops and resets the timer
        self.reset()
        self.active = False

    def reset(self):
        # Resets the timer value
        self.value = 0
        self.last_int = 0
        self.active = True
