#!/usr/bin/env python3
import numpy as np
import cv2
import time

SIZE = (50,50)
TICKS = 10
SCREEN_SIZE = (640, 480)
def main():

  grid = np.random.choice((np.uint8(1),np.uint8(0)), size=SIZE)
  wait_time = int(1000/TICKS)

  while True:
    it = np.nditer(grid, flags=['multi_index'])
    new_grid = np.zeros(grid.shape, dtype=np.uint8)
    while not it.finished:
      x = it.multi_index[0]
      y = it.multi_index[1]
      curr = grid[x, y]

      min_x = max(x-1,0)
      max_x = min(x+2, grid.shape[0])
      min_y = max(y-1,0)
      max_y = min(y+2, grid.shape[1])

      near = grid[min_x:max_x,min_y:max_y]
      population = np.sum(near)
      next_val = 0

      if curr == 1 and population < 2:
        next_val = 0
      elif curr == 1 and (population == 2 or population == 3):
        next_val = 1
      elif curr == 1 and population > 3:
        next_val = 0
      elif curr == 0 and population == 3:
        next_val = 1
      else:
        next_val = curr
      
      next_val = np.uint8(next_val)
      new_grid[x,y] = next_val

      it.iternext()
    grid = new_grid
    render(grid, wait_time)

def render(grid, wait_time):
  
  img = np.repeat(grid[:, :, np.newaxis].astype(np.float32), 3, axis=2)
  img = abs(img - 1)
  img = cv2.resize(img, dsize=SCREEN_SIZE, interpolation=cv2.INTER_NEAREST)
  cv2.imshow("Life", img)
  cv2.waitKey(wait_time)
if __name__ == "__main__":
  main()