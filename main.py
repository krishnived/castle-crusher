import vidmaker
import pygame
import phase1

FPS = 60
win = pygame.display.set_mode((1536, 801))
pygame.display.set_caption("vidmaker test")


vid = vidmaker.Video("vidmaker.mp4", fps=FPS, resolution=(1536, 801))

phase1.main(win, vid, (0, 255, 0), (0, 0, 255))

vid.export(True)
