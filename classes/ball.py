from vsss_client import FIRASim

class Ball:
    def __init__(self):
        self.fira = FIRASim("config.ini")

    def x(self):
        return self.fira.ball().x
    
    def y(self):
        return self.fira.ball().y