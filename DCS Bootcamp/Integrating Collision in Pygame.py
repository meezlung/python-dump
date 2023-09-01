import pygame
from typing import Self

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
running = True
dt = 0 

class Interval:
    def __init__(self, lower: float, upper: float):
        assert upper > lower
        self.lower = lower
        self.upper = upper

    def __contains__(self, value: float): 
        return self.lower <= value <= self.upper

    def is_behind(self, value: float):
        return self.upper < value
    
    def is_ahead(self, value: float):
        return value < self.lower

    def is_disjoint_from(self, other: Self):
        return self.is_behind(other.lower) or self.is_ahead(other.upper)
    
class Point:
    x: float = 0
    y: float = 0

class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.width = Interval(top_left.x, bottom_right.x)
        self.height = Interval(bottom_right.y, top_left.y)

    def __contains__(self, point: Point):
        return point.x in self.width and point.y in self.height
    
    def is_disjoint_from(self, other: Self):
        return self.height.is_disjoint_from(other.height) or self.width.is_disjoint_from(other.width)

# rectangle 1
top_left1 = Point()
top_left1.x = 10
top_left1.y = 60

bottom_right1 = Point()
bottom_right1.x = 60
bottom_right1.y = 10

# rectangle 2
top_left2 = Point()
top_left2.x = 20
top_left2.y = 70

bottom_right2 = Point()
bottom_right2.x = 70
bottom_right2.y = 20

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('light blue')

    rectangle1 = Rectangle(top_left1, bottom_right1)
    rectangle2 = Rectangle(top_left2, bottom_right2)

    rectangle1_rect = pygame.Rect(top_left1.x, top_left1.y, abs(top_left1.x - bottom_right1.x), abs(top_left1.y - bottom_right1.y))
    rectangle2_rect = pygame.Rect(top_left2.x, top_left2.y, abs(top_left2.x - bottom_right2.x), abs(top_left2.y - bottom_right2.y))

    pygame.draw.rect(screen, "red", rectangle1_rect)
    pygame.draw.rect(screen, "green", rectangle2_rect)

    keys = pygame.key.get_pressed() # wsad
    if keys[pygame.K_w]:
        top_left1.y -= 200 * dt
        bottom_right1.y -= 200 * dt
    if keys[pygame.K_s]:
        top_left1.y += 200 * dt
        bottom_right1.y += 200 *dt
    if keys[pygame.K_a]:
        top_left1.x -= 200 * dt
        bottom_right1.x -= 200 * dt
    if keys[pygame.K_d]:
        top_left1.x += 200 * dt
        bottom_right1.x += 200 * dt

    if keys[pygame.K_UP]:
        top_left2.y -= 200 * dt
        bottom_right2.y -= 200 * dt
    if keys[pygame.K_DOWN]:
        top_left2.y += 200 * dt
        bottom_right2.y += 200 * dt
    if keys[pygame.K_LEFT]:
        top_left2.x -= 200 * dt
        bottom_right2.x -= 200 * dt
    if keys[pygame.K_RIGHT]:
        top_left2.x += 200 * dt
        bottom_right2.x += 200 * dt

    collision = (not rectangle1.is_disjoint_from(rectangle2))

    if collision:
        screen.blit(font.render("Collided", True, 'Black'), (10, 80))

    else:
        screen.blit(font.render("Not Yet Collided", True, 'Black'), (10, 80))

    rectangle1_cords = font.render(f'Top Left: ({int(top_left1.x)}, {int(top_left1.y)}) | Bottom Right: ({int(bottom_right1.x)}, {int(bottom_right1.y)})', True, (255, 255, 255))
    screen.blit(rectangle1_cords, (10, 10))

    rectangle2_cords = font.render(f'Top Left: ({int(top_left2.x)}, {int(top_left2.y)}) | Bottom Right: ({int(bottom_right2.x)}, {int(bottom_right2.y)})', True, (255, 255, 255))
    screen.blit(rectangle2_cords, (10, 40))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()