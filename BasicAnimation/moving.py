# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:17:55 2024

@author: axeve

Alexis Evans
CS 120
Prof Harris
Mar. 22, 2024
Basic Animation

"""

import pygame

def main():
    pygame.init()
    
    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Six seasons and a movie.")
    
    #Entities
    # background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((26, 72, 163))
    
    #night sky input
    night = pygame.image.load("night.sky.png")
    night = night.convert_alpha()
    night = pygame.transform.scale(night, (640, 480))
    
    #batman
    bat = pygame.image.load("bat.png")
    bat = bat.convert_alpha()
    bat = pygame.transform.scale(bat, (100, 100))
    
    
    # set up some box variables
    bat_x = 0
    bat_y = 200
    
    #ACTION
    
        #Assign
    clock = pygame.time.Clock()
    keepGoing = True
    
        #Loop
    while keepGoing:
    
        #Time
        clock.tick(30)
    
        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
    
        #modify box value
        bat_x += 5
        #check boundaries
        if bat_x > screen.get_width():
            bat_x = 0
    
        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(night, (0, 0))
        screen.blit(bat, (bat_x, bat_y))
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()