import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock_face = pygame.image.load("mickeyclock.jpeg")
right_hand = pygame.image.load("hand2.png")
left_hand = pygame.image.load("hand2.png")

clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))
right_hand = pygame.transform.scale(right_hand, (100, 20))
left_hand = pygame.transform.scale(left_hand, (120, 20))

center_x, center_y = WIDTH // 2, HEIGHT // 2

def blit_hand(screen, hand, angle, length):
    rotated_hand = pygame.transform.rotate(hand, angle)
    hand_rect = rotated_hand.get_rect(center=(center_x, center_y))
    screen.blit(rotated_hand, hand_rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))
    
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    
    sec_angle = -seconds * 6 + 90
    min_angle = -minutes * 6 + 90
    
    blit_hand(screen, left_hand, sec_angle, 0)
    blit_hand(screen, right_hand, min_angle, 0)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    time.sleep(1)

pygame.quit()