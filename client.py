import pygame
from network import Network
from player import Player

width  = 500
height = 500
win    = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


clientNumber = 0



def read_pos(s):
    s = s.split(",")
    return int(s[0]), int(s[1])

def make_pos(tup):
    return str(str(tup[0]) + "," + str(tup[1]))

def redrawWindow(win, player1, player2):
    win.fill((255,255,255))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p1 = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(0,0,255))
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        p2Pos = read_pos( n.send( make_pos( (p1.x, p1.y) ) ) )
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redrawWindow(win, p1, p2)
    
    pygame.display.update()

main()