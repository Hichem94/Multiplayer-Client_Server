import pygame
from network import Network
from player import Player

width  = 500
height = 500
win    = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


# Initialiser le module de police
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 36)

def redrawWindow(win, player1, player2, game):
    win.fill((255,255,255))
    player1.draw(win)
    #player2.draw(win)
    if game.ready:
        player2.draw(win)
    else:
        texte = font.render("Waiting for player 2", True, (0,0,0))
        win.blit(texte, (100,100))
    pygame.display.update()


def main():
    run = True
    n = Network()
    p1 = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        tup = n.send(p1)
        p2 = tup[0]
        game = tup[1]
        print(p2)
        #print("GAME ID = " + str(game.getID()) + " GAME READY = " + str(game.getReady()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redrawWindow(win, p1, p2, game)
    
    pygame.display.update()

main()