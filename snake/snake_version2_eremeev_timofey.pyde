asize = 0
bsize = 0
csize = 0
dsize = 0

def setup():
    size(600,400)
    background(100)
    frameRate(60)

    
def draw():
    global asize
    global bsize
    global csize
    global dsize
    fill(255)
    stroke(0)
    rect(asize,bsize,40,40)

    
    if keyPressed:
        
            
            
        if key == "r" or key == "R" or key == u"к" or key == u"К":
            
            
            background(100)
            

            
        if key == "d" or key == "D" or key == u"в" or key == u"В":
            
            asize = asize + 1
            
        if key == "s" or key == "S" or key == u"ы" or key == u"Ы":
            
            bsize = bsize + 1
            
        if key == "a" or key == "A" or key == u"ф" or key == u"Ф":
            
            asize = asize - 1
            
        if key == "w" or key == "W" or key == u"ц" or key == u"Ц":
            
            bsize = bsize - 1
            
    
            
        
            
            

            
            

        
            
