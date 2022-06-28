import pygame

FPS = 60


class Ball:
    def __init__(self, radius, color: list, init_pos):
        self.radius = radius
        self.color = color
        self.pos = init_pos
        self.x_vel = 0
        self.y_vel = 0
        self.at_rest=False

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos, self.radius)
        self._update()

    def _update(self):
        self.pos[0] += self.x_vel
        self.pos[1] += self.y_vel
        if not self.at_rest:
            self.y_vel += 0.5
        if self.pos[1] >= 801 - 7:
            self.y_vel = (-self.y_vel)/1.5
        if abs(self.y_vel)<1 and self.pos[1]<15:
            self.y_vel=0
            self.pos[1]=801-7
            self.at_rest=True
        print(self.y_vel)


def main(win, vid, attacker_color, defender_color):
    pygame.init()
    clock = pygame.time.Clock()
    attacker_ball = Ball(7, attacker_color, [1536 / 2, 25])
    defender_ball = Ball(7, defender_color, [1536 / 2, (801 / 2) + 25])
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        win.fill((89, 86, 83))
        attacker_ball.draw(win)
        defender_ball.draw(win)
        vid.update(pygame.surfarray.pixels3d(win).swapaxes(0, 1))
        pygame.display.update()
