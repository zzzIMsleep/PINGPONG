from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed
   
win_width = 700
win_height = 500
FPS = 60
clock= time.Clock()
window = display.set_mode((win_width, win_height))
display.set_caption('PingPong')
background = transform.scale(image.load('stol.jpg'),(win_width, win_height))
run = True

speed_x =3
speed_y =3
finish = False
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render(' Player 1 LOSE!', True, (180,0,0))
font2 = font.Font(None, 35)
lose2 = font2.render(' Player 2 LOSE!', True, (180,0,0))

ball = GameSprite('boll.png', 380, 50, 10, 105, 75)
player1 = Player('PLA1.jpg', 10, 300, 10, 30, 130)
player2 = Player('PLA1.jpg', 670, 300, 10, 30, 130)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0, 0))

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2,ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
    if ball.rect.x > win_width - 50:
        finish = True
        window.blit(lose2, (200,200))
    if ball.rect.y > win_height-50 or ball.rect.y <0:
        speed_y *= -1
    ball.reset()
    player1.update_l()
    player1.reset()
    player2.update_r()
    player2.reset()
    
    display.update()
    time.delay(50)
