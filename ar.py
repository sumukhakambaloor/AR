import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hotel AR Interface")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Load images
hotel_image = pygame.image.load("C:/Users/gurup/OneDrive/Desktop/ARVR/images/test.jpeg")  # Replace with your image

hotel_image = pygame.transform.scale(hotel_image, (WIDTH, HEIGHT))
menu_image = pygame.image.load("C:/Users/gurup/OneDrive/Desktop/ARVR/images/images (11).jpg")  # Replace with your menu image

  # Replace with your menu image
menu_image = pygame.transform.scale(menu_image, (400, 300))

# States
state = "hotel"  # Can be 'hotel', 'menu', or 'order_successful'

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if state == "hotel":
                # Check if specific part of the image is clicked
                if 200 < x < 400 and 300 < y < 400:  # Adjust coordinates as needed
                    state = "menu"

            elif state == "menu":
                # Check if menu is clicked
                if 100 < x < 500 and 100 < y < 400:  # Adjust coordinates for menu
                    state = "order_successful"

    # Display content based on the state
    if state == "hotel":
        screen.blit(hotel_image, (0, 0))
        pygame.draw.rect(screen, GREEN, (200, 300, 200, 100), 3)  # Highlight clickable area

    elif state == "menu":
        screen.blit(menu_image, (200, 150))  # Display menu

    elif state == "order_successful":
        font = pygame.font.Font(None, 74)
        text = font.render("Order Successful!", True, BLACK)
        screen.blit(text, (150, 250))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
