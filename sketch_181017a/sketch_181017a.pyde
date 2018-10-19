
x = 0
y = 0
def setup():
    size(640,380)
def draw() :
    global x
    global y
    if x >= 640:
        x = 0
    x += 2
    if y >= 640 :
        y = 0
    y += 3    
    background("#87ceeb")
    fill(255)
    ellipse(x+120, height/5, 50, 50)
    ellipse(x+40+120, height/5, 50+15, 50)
    ellipse(x+80+120, height/5, 50, 50)
    ellipse(x+40+120, height/5-20, 70, 50)
    ellipse(y, height/5+80, 50, 50)
    ellipse(y+40, height/5+80, 50+15, 50)
    ellipse(y+80, height/5+80, 50, 50)
    ellipse(y+40, height/5+60, 70, 50)
    noStroke()
    fill(0, 128, 0)
    rect(0, height-50, 640, 380)
    
