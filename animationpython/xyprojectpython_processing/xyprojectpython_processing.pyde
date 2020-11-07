x = 0
mode = 1
y1 = 0



def setup():
    size(420,510)
    
    
    
def draw():
    background(0)
    
    
    global x
    global mode
    global y1
   
    stroke(255)
    fill(255)
    ellipse(x,y1,40,40)
    y1 = y1 + 6*mode
    x = x + 5*mode
    if x >= 490:
        mode = -1
    if x <= 0:
        mode = 1
    
  
    
       
        
