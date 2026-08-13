from abc import ABC, abstractmethod
import math
import pygame

CENTER_X = 400
CENTER_Y = 300

class Shape(ABC):
    def __init__(self, x: float, y: float, base_speed: float):
        self.x = x
        self.y = y
        self.base_speed = base_speed

        dx = CENTER_X - x
        dy = CENTER_Y - y

        distance = math.hypot(dx, dy)

        self.dir_x = dx / distance
        self.dir_y = dy / distance

    def get_speed(self, elapsed_time):
        return (
            self.base_speed
            + 0.02 * elapsed_time
            + 0.00002 * elapsed_time**2
        )

    def update(self, elapsed_time):
        speed = self.get_speed(elapsed_time)

        self.x += self.dir_x * speed
        self.y += self.dir_y * speed

    @abstractmethod
    def reached_center(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def hit_player(self, mouse_x, mouse_y):
        pass

class Circle(Shape):
    def __init__(self, x: float, y: float, radius: int):
        super().__init__(x, y, 3)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "yellow",
            (int(self.x), int(self.y)),
            self.radius,
            3
        )

    def reached_center(self):
        distance = math.hypot(
            self.x - CENTER_X,
            self.y - CENTER_Y
        )
        return distance <= self.radius

    def hit_player(self, mouse_x, mouse_y):
        distance = math.hypot(
            self.x - mouse_x,
            self.y - mouse_y
        )

        return distance <= self.radius

class Square(Shape):
    def __init__(self, x: float, y: float, length: int):
        super().__init__(x, y, 2)
        self.length = length

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            "green",
            (
            self.x - self.length / 2,
            self.y - self.length / 2,
            self.length,
            self.length
            ),
            3
        )

    def reached_center(self):
        left = self.x - self.length / 2
        right = self.x + self.length / 2
        top = self.y - self.length / 2
        bottom = self.y + self.length / 2

        return (
            left <= CENTER_X <= right
            and
            top <= CENTER_Y <= bottom
        )

    def hit_player(self, mouse_x, mouse_y):
        left = self.x - self.length / 2
        right = self.x + self.length / 2
        top = self.y - self.length / 2
        bottom = self.y + self.length / 2

        return (
            left <= mouse_x <= right
            and
            top <= mouse_y <= bottom
        )

    
class Triangle(Shape):
    def __init__(self, x: float, y: float, length: int):
        super().__init__(x, y, 4.5)
        self.length = length

    def draw(self, screen):
        height = math.sqrt(3) / 2 * self.length
        points = [
            (self.x, self.y - 2 * height / 3),                    
            (self.x - self.length / 2, self.y + height / 3),      
            (self.x + self.length / 2, self.y + height / 3)       
        ]

        pygame.draw.polygon(
            screen,
            "red",
            points,
            3
        )

    def reached_center(self):
        height = math.sqrt(3) / 2 * self.length
        collision_radius = height / 2
        distance = math.hypot(
            self.x - CENTER_X,
            self.y - CENTER_Y
        )

        return distance <= collision_radius

    def hit_player(self, mouse_x, mouse_y):
        height = math.sqrt(3) / 2 * self.length
        collision_radius = height / 2

        distance = math.hypot(
            self.x - mouse_x,
            self.y - mouse_y
        )

        return distance <= collision_radius