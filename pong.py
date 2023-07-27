import pygame

pygame.init()

COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
}
score_font = pygame.font.Font('freesansbold.ttf', 48)

W, H = 700, 700
SCR = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pong Game v0.01")
CLK = pygame.time.Clock()
FPS = 30


class Player:
    def __init__(self, x, y, w, h, s, c) -> None:
        self.posx = x
        self.posy = y
        self.width = w
        self.height = h
        self.speed = s
        self.color = c
        self.player_rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.striker = pygame.draw.rect(SCR, self.color, self.player_rect)

    def display(self):
        self.striker = pygame.draw.rect(SCR, self.color, self.player_rect)

    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac
        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= H:
            self.posy = H - self.height
        self.player_rect = pygame.Rect(self.posx, self.posy, self.width, self.height)

    def get_rect(self):
        return self.player_rect

    def display_score(self, text, score, x, y, color):
        text = score_font.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        SCR.blit(text, textRect)


class Ball:
    def __init__(self, x, y, r, s, c) -> None:
        self.posx = x
        self.posy = y
        self.radius = r
        self.speed = s
        self.color = c
        self.xFac = 1
        self.yFac = -1
        self.ball_circle = pygame.draw.circle(SCR, c, (x, y), r)
        self.trigger = 1

    def display(self):
        self.ball_circle = pygame.draw.circle(SCR, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac

        if 0 >= self.posy or self.posy >= H:
            self.yFac *= -1

        if self.posx <= 0 and self.trigger:
            self.trigger = 0
            return 1
        elif self.posx >= W and self.trigger:
            self.trigger = 0
            return -1
        else:
            return 0

    def hit(self):
        self.xFac *= -1

    def get_circle(self):
        return self.ball_circle

    def restart(self):
        self.posx = W // 2
        self.posy = H // 2
        self.xFac *= -1
        self.trigger = 1


def main():
    running = True
    p1 = Player(20, 0, 10, 100, 10, COLORS['green'])
    p2 = Player(W - 30, 0, 10, 100, 10, COLORS['red'])
    b = Ball(W // 2, H // 2, 7, 7, COLORS['white'])

    list_of_players = [p1, p2]
    p1_score, p2_score = 0, 0
    p1_yFac, p2_yFac = 0, 0

    while running:
        SCR.fill(COLORS["black"])

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    p2_yFac = -1
                if event.key == pygame.K_DOWN:
                    p2_yFac = 1
                if event.key == pygame.K_w:
                    p1_yFac = -1
                if event.key == pygame.K_s:
                    p1_yFac = 1
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    p2_yFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    p1_yFac = 0

        for p in list_of_players:
            if pygame.Rect.colliderect(b.get_circle(), p.get_rect()):
                b.hit()
        p1.update(p1_yFac)
        p2.update(p2_yFac)
        point = b.update()

        if point == -1:
            p1_score += 1
        elif point == 1:
            p2_score += 1

        if point:
            b.restart()

        p1.display()
        p2.display()
        b.display()
        p1.display_score("P1: ", p1_score, 100, 20, COLORS['white'])
        p1.display_score("P2: ", p2_score, W - 100, 20, COLORS['white'])

        pygame.display.update()
        CLK.tick(FPS)
