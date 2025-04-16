import pygame
import time
from random import randint
import sys

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Reaction():
    def __init__(self,width,height):
        self.font = pygame.font.Font('Glitchy_font.otf',40)
        self.width = width
        self.height = height
            
    def main_screen(self,screen):
        press_start_text = self.font.render('Press Space to check you Reaction time',False,'White')
        press_start_text_rect = press_start_text.get_rect(center = (self.width/2,self.height/2))
        screen.fill('red')
        screen.blit(press_start_text,press_start_text_rect)

    def wait(self,screen):
        wait_text = self.font.render('Wait for the green color to appear',False,'White')
        wait_text_rect = wait_text.get_rect(center=(self.width/2,self.height/2))
        screen.fill('blue')
        screen.blit(wait_text,wait_text_rect)

    def reaction_screen(self,screen):
        tap_fast = self.font.render('Tap Here',False,'white')
        screen.fill('green')
        screen.blit(tap_fast,(300,20))

    def result(self,screen,time_ms):
        try:
            font = pygame.font.Font('Pixeltype.ttf',50)
        except:
            font = pygame.font.SysFont(None,50)
        res = font.render(f'Reaction Time: {time_ms} ms',False,'black')
        res_rect = res.get_rect(center = (self.width/2, self.height/2))
        screen.fill('pink')
        screen.blit(res,res_rect)

    def failed(self,screen):
        failed_text = self.font.render('Too early',False,'white')
        failed_text_rect = failed_text.get_rect(center = (self.width/2, self.height/2))
        screen.fill('black')
        screen.blit(failed_text,failed_text_rect)

rn = Reaction(width,height)
state = 'main' 
random_delay = randint(4000,8000)
delay_event = pygame.USEREVENT + 1
pygame.time.set_timer(delay_event,random_delay)
running = True
first_taped_time = 0
green_appeared_time = 0
rn_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == 'main':
            if event.type == pygame.MOUSEBUTTONDOWN:
                first_taped_time = pygame.time.get_ticks()
                state = 'wait'
        
        elif state == 'wait':
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = 'failed'

            elif event.type == delay_event:
                green_appeared_time = pygame.time.get_ticks()
                state = 'react'
        
        elif state == 'failed':
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = 'main'

        elif state == 'react':
            if event.type == pygame.MOUSEBUTTONDOWN:
                rn_time = (pygame.time.get_ticks()) - green_appeared_time
                state = 'result'

        elif state == 'result':
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = 'main'

    if state == 'main':
        rn.main_screen(screen)
    elif state == 'wait':
        rn.wait(screen)
    elif state == 'react':
        rn.reaction_screen(screen)
    elif state == 'failed':
        rn.failed(screen)
    elif state == 'result':
        rn.result(screen,rn_time)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
