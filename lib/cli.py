
from helpers import (
    function_1, function_2,
    function_3, function_4, 
    function_5, function_6, 
    function_7, function_8, 
    function_9, function_10, 
)
import debug

def main():
    print('Welcome to my CLI!') #greetings
    debud.log_info('CLI started')
    
    function_1()
    
    x = 0
    while not x: 
        x = function_2(x)
        debug.check_variable('x',x)
        
    if x < 0:
        y = function_3(x) 
        debug.check_variable('y',y) 
    else:
        y = function_4(x)  
        debug.check_variable('y',y) 
        
        
    z = function_5(y)  
    debug.check_variable('z',z) 
    z = function_6(z)
    z = function_7(z)
    z = function_8(z)
    
    
    function_9(z)  
    function_10(x,y,z)
    
    print('Thanks for using my CLI!')#closing message
    
    if __name__ == '__main__':
        main()
        