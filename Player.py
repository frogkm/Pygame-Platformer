import pygame

class Player():
    def __init__(self, x, y, imagePath, sW, sH):
        self.sW = sW
        self.sH = sH
        self.gravity = 5
        self.x = x
        self.y = y
        self.w = 32
        self.h = 75
        self.onGround = False
        self.yVel = 0
        self.yAcc = 0
        self.jumpVal = 50
        self.speed = 10
        self.image = pygame.image.load(imagePath)

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))


    def jump(self):
        if self.onGround:
            self.yAcc = -self.jumpVal
            self.onGround = False

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_SPACE]:
            self.jump()



    def physics(self):
        if self.y + self.h > self.sH:
            self.y = self.sH - self.h
            self.onGround = True

        if not self.onGround:
            self.yVel += self.gravity
        else:
            self.yVel = 0

        self.yVel += self.yAcc
        self.yAcc = 0
        self.y += self.yVel

    def update(self):
        self.input()
        self.physics()
