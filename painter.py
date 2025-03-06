from pykkar import *

def paint_square(robot):
    
    if not is_painted():
        paint()  
     
    for _ in range(4):
        if not is_wall():
            step()  
        if not is_painted():
            paint()  
        right()  
