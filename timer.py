import time

class Timer:
    def __init__(self):
        self.running = False
        self.start_time = 0
        self.end_time = -1
    
    def start(self):
        self.start_time = time.time()
        self.running = True
    
    def stop(self):
        if self.running:
            self.end_time = time.time()
            self.running = False
    
    def read(self):
        '''
        Will return -1 if the timer has not been run.
        '''
        return self.end_time - self.start_time
    
    def read_str(self):
        return f'{self.end_time - self.start_time} seconds'