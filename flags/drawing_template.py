import math
import pygame
import cv2

from google.colab.patches import cv2_imshow
from google.colab import output

import graphics_primitives

shapes = []
shape_methods = {
  "circle": graphics_primitives.draw_circle,
  "line": graphics_primitives.draw_line,
  "rectangle": graphics_primitives.draw_rectangle,
  "star": graphics_primitives.draw_star,
  "triangle": graphics_primitives.draw_triangle,
  "text": graphics_primitives.draw_text,
  "image": graphics_primitives.draw_image,
}


def draw_circle(x, y, color, radius):
  shapes.append(("circle", (x, y, color, radius), {}))


def draw_line(start_x, start_y, end_x, end_y, color):
  shapes.append(("line", (start_x, start_y, end_x, end_y, color), {}))


def draw_rectangle(x, y, width, height, color, rotation=0):
  shapes.append(("rectangle", (x, y, width, height, color), {
    "rotation": rotation
  }))


def draw_star(x, y, color, radius, points=5, rotation=0):
  shapes.append(("star", (x, y, color, radius), {
    "points": points,
    "rotation": rotation
  }))


def draw_text(text, x, y, color):
  shapes.append(("text", (text, x, y, color), {}))


def draw_triangle(x, y, color, width, height, rotation=0):
  shapes.append(("triangle", (x, y, color, width, height), {
    "rotation": rotation
  }))


def draw_image(image_name, x, y):
  shapes.append(("image", (image_name, x, y), {}))


def draw_shapes():
  for shape_name, shape_args, shape_kwargs in shapes:
    if shape_name not in shape_methods:
      raise ValueError(f"Got unexpected shape: {shape_name}")
    shape_methods[shape_name](*shape_args, **shape_kwargs)


def run_program():
  # Run until the user asks to quit
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # Fill the background with white
    graphics_primitives.screen.fill((255, 255, 255))
    draw_shapes()
    pygame.display.flip()

    #convert image so it can be displayed in OpenCV
    image = pygame.surfarray.array3d(graphics_primitives.screen)
    #  convert from (width, height, channel) to (height, width, channel)
    image = image.transpose([1, 0, 2])
    #  convert from rgb to bgr
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # clear the output
    output.clear(wait=True)
    #Display image
    cv2_imshow(image)

  pygame.quit()


__all__ = [
  "run_program",
  "draw_circle",
  "draw_line",
  "draw_rectangle",
  "draw_star",
  "draw_triangle",
  "draw_image",
  "draw_text",
]
