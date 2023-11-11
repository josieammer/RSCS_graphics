# You shouldn't have to edit anything in this file.
# But please look at the function definitions so that
# you know what functions are available to make your
# graphics functions.

import math
import pathlib

import pygame
import pygame.draw
import pygame.font
import pygame.image
import pygame.time

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def draw_circle(screen, x, y, color, radius):
  """Draw a circle, centered at x, y.
    
    Arguments:
      x (int/float):
        The x coordinate of the center of the circle.
      y (int/float):
        The y coordinate of the center of the circle.
      color (str):
        Name of the fill color, in HTML format.
      radius (int/float):
        The radius of the circle.
    """
  pygame.draw.circle(screen, color, (x, SCREEN_HEIGHT - y), radius)


def draw_line(screen, start_x, start_y, end_x, end_y, color):
  """Draw a line, starting at start_x, start_y and ending at end_x, end_y.

    Arguments:
      start_x (int/float):
        The x coordinate of the start.
      start_y (int/float):
        The y coordinate of the start.
      end_x (int/float):
        The x coordinate of the end.
      end_y (int/float):
        The y coordinate of the end.
      color (str):
        Name of the fill color, in HTML format.
    """
  pygame.draw.line(screen, color, (start_x, SCREEN_HEIGHT - start_y),
                   (end_x, SCREEN_HEIGHT - end_y))


def draw_image(screen, image_name, x, y):
  """Draw an image, positioned at x, y

    Arguments:
      image_name (str):
        The file name of the image, for example "bunny.png".
      x (int/float):
        The x coordinate of the left edge of the shape.
      y (int/float):
        The y coordinate of the bottom edge of the shape.  
    """
  image = images[image_name]
  image_height = image.get_height()
  left_x = x
  top_y = y + image_height
  screen.blit(image, (left_x, SCREEN_HEIGHT - top_y))


def draw_rectangle(screen, x, y, width, height, color, rotation=0):
  """Draw a rectangle, with left and bottom at x, y.

    Arguments:
      x (int/float):
        The x coordinate of the left of the shape.
      y (int/float):
        The y coordinate of the bottom of the shape.
      width (int/float):
        The width of the rectangle.
      height (int/float):
        The height of the rectangle.
      color (str):
        Name of the fill color, in HTML format.
    """
  # for calculating rotation, we adjust coordinates to be
  # center of the rectangle, in screen coordinates (top left)
  x = x + (width / 2)
  y = SCREEN_HEIGHT - (y + (height / 2))
  points = []
  radius = math.sqrt((height / 2)**2 + (width / 2)**2)
  angle = math.atan2(height / 2, width / 2)
  angles = [angle, -angle + math.pi, angle + math.pi, -angle]
  rot_radians = (math.pi / 180) * rotation
  for angle in angles:
    y_offset = -1 * radius * math.sin(angle + rot_radians)
    x_offset = radius * math.cos(angle + rot_radians)
    points.append((x + x_offset, y + y_offset))
  
  pygame.draw.polygon(screen, color, points)


def draw_star(screen, x, y, color, radius, points=5, rotation=0):
  """Draw a star, centered at x, y.
  
    Arguments:
      x (int/float):
        The x coordinate of the center of the shape.
      y (int/float):
        The y coordinate of the center of the shape.
      color (str):
        Name of the fill color, in HTML format.
      radius (int/float):
        The radius of the shape.
      rotation (int/float):
        Rotation of the shape in degrees.
    """
  y = SCREEN_HEIGHT - y
  point_coords = []
  theta = 2 * math.pi / points
  rot_radians = (math.pi / 180) * rotation
  for i in range(points):
    height = -1 * radius * math.cos(i * theta + rot_radians)
    width = radius * math.sin(i * theta + rot_radians)
    point_coords.append((x + width, y + height))
    height = -1 * (radius / 2) * math.cos((i + 0.5) * theta + rot_radians)
    width = (radius / 2) * math.sin((i + 0.5) * theta + rot_radians)
    point_coords.append((x + width, y + height))

  pygame.draw.polygon(screen, color, point_coords)


def draw_text(screen, text, x, y, color):
  """Draw text, with left and bottom at x, y

    Arguments:
      text (str):
        The text to write. For example, "Game Over".
      x (int/float):
        The x coordinate of the left of the shape.
      y (int/float):
        The y coordinate of the bottom of the shape.  
    """
  _default_font = pygame.font.Font(pygame.font.get_default_font(), 16)
  textsurface = _default_font.render(text, True, color)
  screen.blit(textsurface, (x, SCREEN_HEIGHT - y - textsurface.get_height()))


def draw_triangle(screen, x, y, color, width, height, rotation=0):
  """Draw a triangle, centered at x, y.
  
    Arguments:
      x (int/float):
        The x coordinate of the center of the shape.
      y (int/float):
        The y coordinate of the center of the shape.
      color (str):
        Name of the fill color, in HTML format.
      width (int/float):
        The width of the rectangle.
      height (int/float):
        The height of the rectangle.
      rotation (int/float):
        Rotation of the shape in degrees.
    """
  y = SCREEN_HEIGHT - y
  points = []
  starting_points = [(-width / 2, height / 2), (width / 2, height / 2),
                     (0, -height / 2)]
  rot_radians = (math.pi / 180) * rotation
  for i in range(3):
    # x' = x * cos(theta) - y * sin(theta)
    x_offset = starting_points[i][0] * math.cos(rot_radians) - \
    starting_points[i][1] * math.sin(rot_radians)
    # y' = y * cos(theta) + x * sin(theta)
    y_offset = starting_points[i][1] * math.cos(rot_radians) + \
    starting_points[i][0] * math.sin(rot_radians)
    points.append((x + x_offset, y + y_offset))
    
  pygame.draw.polygon(screen, color, points)


def init_images():
  """Load all images from the images directory."""
  global images

  images_dir = pathlib.Path(__file__).parent / "images"
  for image_path in images_dir.glob("*.png"):
    image = pygame.image.load(image_path)
    images[image_path.name] = image


images = {}
init_images()

__all__ = [
  "draw_circle",
  "draw_rectangle",
  "draw_star",
  "draw_text"
]
