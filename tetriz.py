from enum import Enum

class Movement(Enum):
    DOWN = 1
    LEFT = 2
    RIGTH = 3
    ROTATE = 4
def tetriz():
    screen = [["🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
              ["🔳","🔳","🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
              ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
              ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
              ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
              ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
              ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
              ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
              ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
              ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"]]
    print_screen(screen)

def move_piece(movement:Movement):
    match movement:
        case Movement.DOWN: 
            pass   
        case Movement.RIGTH:
            pass  
        case Movement.LEFT:  
            pass  
        case Movement.ROTATE: 
            pass
           

def print_screen(screen:list):
    for row in screen:
        print("".join(map(str,row)))
        
tetriz()