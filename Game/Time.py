from glob import Globals

class Timer():

    def __init__(self, interval):
        self.interval = interval
        self.value = 0
        self.last_int = 0
        self.active = False
        self.on_next = None

    def update(self):
        if self.active:
            self.value += Globals.deltatime / self.interval
            if int(self.value) != int(self.last_int):
                if self.on_next != None:
                    self.on_next()

    def start(self):
        self.active = True

    def pause(self):
        self.active = False

    def stop(self):
        self.reset()
        self.active = False

    def reset(self):
        self.value = 0
        self.last_int = 0
        self.active = True
