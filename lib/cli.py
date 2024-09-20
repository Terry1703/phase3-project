from helpers import (
    function_1, function_2,
    function_3, function_4, 
    function_5, function_6, 
    function_7, function_8, 
    function_9, function_10, 
)
import debug

class MyCLI:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def start(self):
        print('Welcome to my CLI!')  # greetings
        debug.log_info('CLI started')
        
        function_1()
        
        self.run_loop()
        self.process_values()
        
        print('Thanks for using my CLI!')  # closing message

    def run_loop(self):
        while not self.x:
            self.x = function_2(self.x)
            debug.check_variable('x', self.x)

    def process_values(self):
        if self.x < 0:
            self.y = function_3(self.x) 
            debug.check_variable('y', self.y) 
        else:
            self.y = function_4(self.x)  
            debug.check_variable('y', self.y) 

        self.z = function_5(self.y)  
        debug.check_variable('z', self.z) 
        self.z = function_6(self.z)
        self.z = function_7(self.z)
        self.z = function_8(self.z)

        function_9(self.z)  
        function_10(self.x, self.y, self.z)

if __name__ == '__main__':
    cli = MyCLI()
    cli.start()
