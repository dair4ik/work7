import pygame
import sys

pygame.init()
pygame.mixer.init()

playlist = ['track1.mp3', 'track2.mp3', 'track3.mp3']
current_track_index = 0

def load_track(index):
    pygame.mixer.music.load(playlist[index])

load_track(current_track_index)

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("MusicPlayer(by Kaliyev Dair)")

font = pygame.font.SysFont(None, 28)

def draw_text(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))
    draw_text("P: Play  S: Stop  N: Next  B: Previous", 20, 80)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
                print(f"Playing: {playlist[current_track_index]}")
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                print("Music stopped.")
            elif event.key == pygame.K_n:
                current_track_index = (current_track_index + 1) % len(playlist)
                load_track(current_track_index)
                pygame.mixer.music.play()
                print(f"Next: {playlist[current_track_index]}")
            elif event.key == pygame.K_b:
                current_track_index = (current_track_index - 1) % len(playlist)
                load_track(current_track_index)
                pygame.mixer.music.play()
                print(f"Previous: {playlist[current_track_index]}")

    pygame.display.flip()

pygame.quit()
sys.exit()
