import pygame
import datetime
import math

class MickeyClock:
    def __init__(self, width, height):
        self.center = (width // 2, height // 2)

        
        self.clock_face = pygame.image.load("C:\TT\Python\Practices\Practice9\mickeys_clock\images\clock.png").convert()
        self.clock_face.set_colorkey((255,255,255))
        self.minute_hand = pygame.image.load("C:\TT\Python\Practices\Practice9\mickeys_clock\images\long_hand.png").convert()
        self.minute_hand.set_colorkey((255,255,255))
        self.second_hand = pygame.image.load("Practices/Practice9/mickeys_clock/images/short_hand.png").convert()
        self.second_hand.set_colorkey((255,255,255))

        
        self.clock_face = pygame.transform.scale(self.clock_face, (600, 600))
        self.minute_hand = pygame.transform.scale(self.minute_hand, (300, 80))
        self.second_hand = pygame.transform.scale(self.second_hand, (300, 80))

    def get_angles(self):
        now = datetime.datetime.now()
        seconds = now.second
        minutes = now.minute

        sec_angle = 90 - (seconds * 6)
        min_angle = 90 - (minutes * 6) +18

        return min_angle, sec_angle

    def rotate(self, image, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        rect = rotated_image.get_rect(center=self.center)
        return rotated_image, rect

    def update(self):
        self.min_angle, self.sec_angle = self.get_angles()

    def draw(self, screen):
        
        face_rect = self.clock_face.get_rect(center=self.center)
        screen.blit(self.clock_face, face_rect)

        
        min_img, min_rect = self.rotate(self.minute_hand, self.min_angle)
        sec_img, sec_rect = self.rotate(self.second_hand, self.sec_angle)

        screen.blit(min_img, min_rect)
        screen.blit(sec_img, sec_rect)