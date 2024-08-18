import pygame
import sys
import random

# Initialize Pygame, which sets up the game environment.
pygame.init()

# Constants for screen dimensions and grid settings.
WIDTH, HEIGHT = 400, 400               # Screen width and height
GRID_SIZE = 60                         # Number of cells in a row
BOX_SIZE = WIDTH // GRID_SIZE          # Size of each cell in the grid
VELOCITY_MULTIPLIER = 1                # Multiplier for the velocity of the points

# Set up the display window with the specified width and height.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mesh Gradient")  # Set the window title

# Define some basic colors using RGB values.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 100, 0)

# Class to represent a point that contributes to the gradient in the grid.
class GradientPoint:
    def __init__(self, x, y, color, spread=0.5):
        self.x = x                      # X-coordinate of the point
        self.y = y                      # Y-coordinate of the point
        self.color = color              # Color of the point
        self.dragging = False           # Is the point currently being dragged by the mouse?
        self.spread = spread            # Spread factor for color influence
        self.visible = True             # Visibility of the point
        # Randomly set the initial velocity of the point, multiplied by a constant.
        self.vel_x = random.choice([-2, -1, 1, 2]) * VELOCITY_MULTIPLIER
        self.vel_y = random.choice([-2, -1, 1, 2]) * VELOCITY_MULTIPLIER

    def draw(self, surface):
        # Draw the point only if it is visible.
        if self.visible:
            # Draw a filled circle for the point.
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), 10)
            # Draw an outline around the circle to make it more distinct.
            pygame.draw.circle(surface, BLACK, (int(self.x), int(self.y)), 10, 2)

    def handle_event(self, event):
        # Handle mouse events for dragging the point or adjusting its spread.
        if self.visible:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    # Check if the mouse click is within the point's radius.
                    if (self.x - mouse_x)**2 + (self.y - mouse_y)**2 <= 300:
                        self.dragging = True
                elif event.button == 4:  # Mouse wheel up
                    self.spread += 0.1
                elif event.button == 5:  # Mouse wheel down
                    self.spread -= 0.1
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Release left mouse button
                    self.dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging:
                    # Update the point's position to the mouse position if dragging.
                    self.x, self.y = event.pos

    def move(self):
        # Update the position of the point based on its velocity.
        self.x += self.vel_x
        self.y += self.vel_y

        # Bounce off the walls by reversing direction when hitting an edge.
        if self.x <= 0 or self.x >= WIDTH:
            self.vel_x = -self.vel_x
        if self.y <= 0 or self.y >= HEIGHT:
            self.vel_y = -self.vel_y

# Function to interpolate between two colors.
# t is a value between 0 and 1 that determines the blend ratio.
def interpolate_color(color1, color2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(color1, color2))

# Create gradient points with specific initial positions and colors.
gradient_points = [
    GradientPoint(100, 100, WHITE),
    GradientPoint(WIDTH - 100, 100, BLUE),
    GradientPoint(100, HEIGHT - 100, RED),
    GradientPoint(WIDTH - 100, HEIGHT - 100, WHITE)
]

# Main function that runs the game loop.
def main():
    clock = pygame.time.Clock()  # Initialize a clock to control the frame rate.
    points_visible = True        # Control whether points are visible.

    while True:
        # Handle events such as quitting the game or pressing keys.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit the game if the close button is clicked.
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Toggle visibility of points when the spacebar is pressed.
                    points_visible = not points_visible
                    for point in gradient_points:
                        point.visible = points_visible

            # Pass the event to each gradient point to handle.
            for point in gradient_points:
                point.handle_event(event)

        # Clear the screen with a white background.
        screen.fill(WHITE)

        # Move each point according to its velocity.
        for point in gradient_points:
            point.move()

        # Draw the grid and calculate the color for each cell.
        for y in range(0, HEIGHT, BOX_SIZE):
            for x in range(0, WIDTH, BOX_SIZE):
                total_weight = 0
                r, g, b = 0, 0, 0
                # Calculate the weighted color influence of each point.
                for point in gradient_points:
                    dx = x + BOX_SIZE/2 - point.x
                    dy = y + BOX_SIZE/2 - point.y
                    distance = max(1, (dx**2 + dy**2)**0.5)
                    weight = 1 / (distance ** (2 * point.spread))
                    total_weight += weight
                    r += point.color[0] * weight
                    g += point.color[1] * weight
                    b += point.color[2] * weight
                
                if total_weight > 0:
                    # Normalize the colors by dividing by the total weight.
                    r = int(r / total_weight)
                    g = int(g / total_weight)
                    b = int(b / total_weight)
                
                color = (r, g, b)
                # Draw the cell with the calculated color.
                pygame.draw.rect(screen, color, (x, y, BOX_SIZE, BOX_SIZE))

        # Draw each gradient point.
        for point in gradient_points:
            point.draw(screen)

        pygame.display.flip()  # Update the display with the new frame.
        clock.tick(60)         # Cap the frame rate at 60 frames per second.

# Entry point to start the game.
if __name__ == "__main__":
    main()
