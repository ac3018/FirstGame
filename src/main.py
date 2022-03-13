import pygame
pygame.init()

# creates window
screenWidth = 850
screenHeight = 480
window = pygame.display.set_mode((screenWidth, screenHeight))

# set title of the window
pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

walkRight = [pygame.image.load('resources\R1.png'), pygame.image.load('resources\R2.png'), pygame.image.load('resources\R3.png'), pygame.image.load('resources\R4.png'), pygame.image.load('resources\R5.png'), pygame.image.load('resources\R6.png'), pygame.image.load('resources\R7.png'), pygame.image.load('resources\R8.png'), pygame.image.load('resources\R9.png')]
walkLeft = [pygame.image.load('resources\L1.png'), pygame.image.load('resources\L2.png'), pygame.image.load('resources\L3.png'), pygame.image.load('resources\L4.png'), pygame.image.load('resources\L5.png'), pygame.image.load('resources\L6.png'), pygame.image.load('resources\L7.png'), pygame.image.load('resources\L8.png'), pygame.image.load('resources\L9.png')]
bg = pygame.image.load(r'resources\bg.jpg')
char = pygame.image.load('resources\standing.png')


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.jumping = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpHeight = 8
        self.jumpCount = self.jumpHeight

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))


def redrawGameWindow(user):
    window.blit(bg, (0, 0))  # This will draw our background image at (0,0)
    user.draw(window)
    pygame.display.update()


def main():
    man = Player(0, screenHeight // 2, 64, 64)
    run = True
    while run:
        clock.tick(27)
        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and man.x >= man.vel:  # We can check if a key is pressed like this
            man.x -= man.vel
            man.left = True
            man.right = False
        elif keys[pygame.K_RIGHT] and man.x <= screenWidth - man.vel - 64:
            man.x += man.vel
            man.right = True
            man.left = False
        # when character is not moving
        else:
            man.walkCount = 0

        if not man.jumping:  # Checks is user is not jumping
            if keys[pygame.K_UP] and man.y >= man.vel:  # Same principles apply for the y coordinate
                man.y -= man.vel
                man.left = False
                man.right = False
            if keys[pygame.K_DOWN] and man.y <= screenHeight - 64 - man.vel:
                man.y += man.vel
                man.left = False
                man.right = False
            if keys[pygame.K_SPACE]:
                man.jumping = True
                man.walkCount = 0
        else:
            if man.jumpCount >= -1 * man.jumpHeight:
                man.y -= (man.jumpCount * abs(man.jumpCount))
                man.jumpCount -= 2
            else:
                man.jumpCount = man.jumpHeight
                man.jumping = False

        redrawGameWindow(man)

    pygame.quit()  # If we exit the loop this will execute and close our game


if __name__ == '__main__':
    main()
