import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RedBall(by Kaliyev Dair)")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
move_distance = 20

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - ball_radius - move_distance >= 0:
                    ball_y -= move_distance
            elif event.key == pygame.K_DOWN:
                if ball_y + ball_radius + move_distance <= HEIGHT:
                    ball_y += move_distance
            elif event.key == pygame.K_LEFT:
                if ball_x - ball_radius - move_distance >= 0:
                    ball_x -= move_distance
            elif event.key == pygame.K_RIGHT:
                if ball_x + ball_radius + move_distance <= WIDTH:
                    ball_x += move_distance

    pygame.display.flip()
    clock.tick(60)
