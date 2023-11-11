# This "from ... import ..." line needs to appear first.
# You'll learn more about this in later lessons.
# ====================================================
from drawing_template import *
import pygame
import constants

# ====================================================


def test_rects_rotation():
  for i in range(0, 91, 15):
    draw_rectangle(0 + i, 0 + i, constants.SCREEN_WIDTH - (i * 2),
                   constants.SCREEN_HEIGHT - (i * 2),
                   pygame.Color(i * 2, 0, 100), i)


def test_rects():
  for i in range(0, 100, 10):
    draw_rectangle(0 + i, 0 + i, constants.SCREEN_WIDTH - (i * 2),
                   constants.SCREEN_HEIGHT - (i * 2),
                   pygame.Color(0, i * 2, 0), 0)


def test_rects_topleft():
  for i in range(0, 100, 10):
    width = constants.SCREEN_WIDTH - (i * 2)
    height = constants.SCREEN_HEIGHT - (i * 2)
    draw_rectangle(0, 240 - height, width, height, pygame.Color(200, i * 2, 0),
                   0)


def test_circle():
  for i in range(0, 100, 10):
    draw_circle(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                pygame.Color(100, 255 - (i * 2), i * 2), 120 - i)


def test_circle_bottomright():
  for i in range(0, 100, 10):
    draw_circle(0, 0, pygame.Color(200, 255 - (i * 2), i * 2), 120 - i)


def test_stars():
  star_dim = 20
  for x in range(10, constants.SCREEN_WIDTH, star_dim):
    for y in range(10, constants.SCREEN_HEIGHT, star_dim):
      draw_star(x, y, "blue", star_dim - 10)


def test_text():
  for x in range(0, constants.SCREEN_WIDTH, 80):
    for y in range(0, constants.SCREEN_HEIGHT, 80):
      draw_text(f"{x},{y}", x, y, "red")

def test_images():
  for x in range(0, constants.SCREEN_WIDTH, 80):
    for y in range(0, constants.SCREEN_HEIGHT, 80):
      draw_image("search.png", x, y)
