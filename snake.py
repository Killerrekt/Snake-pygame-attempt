from calendar import c
from this import d
import pygame
import random

screen = pygame.display.set_mode((900,500))
pygame.display.set_caption("snake")

food=[0,0]

red = (255,0,0)

x,y=0,0
c,d=0,0
snake = pygame.Rect(x,y,10,10)
yellow = (255,255,0)

black=(0,0,0)

v=[0]

fps = pygame.time.Clock()

def rand():
    food[0]=random.randrange(0,499,10)
    food[1]=random.randrange(0,899,10)

def draw(a,b):
    screen.fill(black)
    pygame.draw.rect(screen,red,(food[1],food[0],10,10))
    pygame.draw.rect(screen,yellow,(b,a,10,10))
    pygame.display.update()

def main(c,d):
    boolean = True
    a,b=0,0
    while boolean:
        if v[0]==0:
            rand()
            v[0]=1
            print(food[1],food[0])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                boolean=False
            if event.type==pygame.MOUSEMOTION:
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    a-=5
                elif event.key == pygame.K_DOWN:
                    a+=5
                elif event.key == pygame.K_RIGHT:
                    b+=5
                elif event.key == pygame.K_LEFT:
                    b-=5
            draw(a,b)
            fps.tick(30)

            print(event)
    pygame.quit()

main(c,d)     