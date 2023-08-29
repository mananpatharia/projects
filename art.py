import pygame
import os

pygame.init()
screen = pygame.display.set_mode((960,540))
pygame.display.set_caption("Kids' Art Gallery")

art_folder = r"C:\Users\user\Pictures\Screenshots"
art_files = os.listdir(art_folder)
art_files = [f for f in art_files if f.endswith('.png') or f.endswith('.jpg')]

current_art_index = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_art_index = (current_art_index - 1) % len(art_files)
            elif event.key == pygame.K_RIGHT:
                current_art_index = (current_art_index + 1) % len(art_files)

    screen.fill((255, 255, 255))  # Fill the screen with white

    if art_files:  # Check if there are any art files to display
        current_art_path = os.path.join(art_folder, art_files[current_art_index])
        art_image = pygame.image.load(current_art_path)
        screen.blit(art_image, (0, 0))

    pygame.display.flip()

pygame.quit()
