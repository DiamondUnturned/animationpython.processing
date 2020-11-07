animcolor1 = 0


def setup():
    size(600,400)

def draw():
    global animcolor1
    background(0, 232, 213)
    stroke(animcolor1)
    fill(animcolor1)
    ellipse(300,200,40,40)
     
    animcolor1 = animcolor1 + 1
    if animcolor1 >= 300:
        animcolor1 = 0
    
    
    
