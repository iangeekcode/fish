import pygame as py

py.init()
screen_info = py.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)

screen = py.display.set_mode(size)
clock = py.time.Clock()
color = (0, 127, 255)

fish_image = py.image.load("fish.png")
fish_image = py.transform.smoothscale(fish_image, (80,80))
fish_rect = fish_image.get_rect()
fish_rect.center = (width // 2, height // 2)

def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    screen.blit(fish_image, fish_rect)
    py.display.flip()

if __name__=="__main__":
  main()
