# These are library and modules for game with python3.

import curses
import random
import time

class Player:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.char = '🟦'

    def move_up(self):
        self.y = max(1, self.y - 1)

    def move_down(self, max_y):
        self.y = min(max_y - 2, self.y + 1)

class Obstacle:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.char = '🟥'

    def move(self):
        self.x -= 1

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    height, width = stdscr.getmaxyx()
    player = Player(height // 2, 5)
    obstacles = []
    score = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Score: {score}")

        key = stdscr.getch()
        if key == curses.KEY_UP:
            player.move_up()
        elif key == curses.KEY_DOWN:
            player.move_down(height)
        elif key == ord('q'):
            break

        if random.randint(1, 10) == 1:
            obstacles.append(Obstacle(random.randint(1, height - 2), width - 2))

        for obs in obstacles:
            obs.move()
            if obs.x == player.x and obs.y == player.y:
                stdscr.addstr(height // 2, width // 2 - 5, "GAME OVER")
                stdscr.refresh()
                time.sleep(2)
                return
            stdscr.addstr(obs.y, obs.x, obs.char)

        stdscr.addstr(player.y, player.x, player.char)
        obstacles = [obs for obs in obstacles if obs.x > 0]
        score += 1
        stdscr.refresh()

curses.wrapper(main)
