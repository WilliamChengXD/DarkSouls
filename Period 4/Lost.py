

from gamelib import*

game=Game(800,600,"Lost Souls")
#titlescreen
bk1=Image("cave entrance.jpeg",game)
bk1.resizeTo(800,600)
title1=Image("lost Souls.png",game)
play=Image("play.png",game)
title1.moveTo(400,150)
play.moveTo(400,300)


while not game.over:
    game.processInput()
    bk1.draw()
    title1.draw()
    play.draw()
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over=True

    game.update(60)

game.over = False

bk2=Image("Background.png",game)
game.setBackground(bk2)
bk2.resizeTo(800,600)
Ghoul=Image("Monster.png",game)
Ghost=Image("Ghost.png",game)
Ghoul.resizeBy(-70)
Ghoul.setSpeed(5)
Ghost.resizeBy(-50)

jumping = False
landed = False
factor = 1  
count = 0

guyR = Animation("guyR.png",8,game,864/8,138,3)
guyL = Animation("guyL.png",8,game,864/8,138,3)
guyR.y = 500
guyR.visible = False
plat3 = Image("platform3.png",game)
plat3.resizeBy(-80)
onplat3 = False 
plat3.setSpeed(8,90)
while not game.over:
    game.processInput()
    game.scrollBackground("left",6)
    plat3.move()
    guyL.moveTo(guyR.x,guyR.y)
    guyR.draw()

    if keys.Pressed[K_RIGHT]:
        guyR.visible = True
        guyL.visible = False
        guyR.x+=7
        guyL.x+=7
        
    if keys.Pressed[K_LEFT]:
        guyR.visible = False
        guyL.visible = True
        guyR.x-=7
        guyL.x-=7
        
    if keys.Pressed[K_UP]:
        guyR.y-=1
       
    if keys.Pressed[K_DOWN]:
       guyR.y+=1
        
    if guyR.y< 500 and not onplat3:
        landed = False
     
    else:
        landed = True

    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping = True

    if jumping:
        guyR.y -=40*factor
        factor*=.95
        landed = False
        onplat3 = False
        if factor < .18:
            jumping = False
            factor = 1

    if not landed:
        guyR.y +=11

    if guyR.collidedWith(plat3,"rectangle")and guyR.x>plat3.left and guyR.x<plat3.right and guyR.y>plat3.top and guyR.y<plat3.y+50:
        onplat3 = True

    if guyL.collidedWith(plat3,"rectangle")and guyL.x>plat3.left and guyL.x<plat3.right and guyL.y>plat3.top and guyL.y<plat3.y+50:
        onplat3 = True

    if onplat3 and guyR.x>plat3.right and not jumping:
        onplat3 = False
        guyR.y +=8

    if onplat3 and guyL.x<plat3.left and not jumping:
        onplat3 = False
        guyL.y +=8
    #moving platforms
    if plat3.isOffScreen("left"):
        plat3.moveTo(900,randint(250,450))

    if guyR.collidedWith(Ghoul) or guyL.collidedWith(Ghoul):
        Ghoul.moveTo(guyR.x,guyR.y)
        game.over = False

    game.update(30)

game.over = False

gameover=Image("game over.png",game)
gameover.moveTo(400,450)
jumpscare=Image("jumpscare.jpg",game)
jumpscare.resizeTo(game.width, game.height)
while not game.over:
    game.processInput()
    jumpscare.draw()
    gameover.draw()

    game.update(60)
    
