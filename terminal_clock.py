#!/usr/bin/env python3
import pyfiglet
import curses
import time


def main(window):
    try:
        curses.curs_set(0)  # Invisible cursor
    except curses.error:
        pass
    try:
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    except ValueError:  # There are no colours; life goes on
        pass
    window.bkgd(" ", curses.color_pair(1))
    while True:
        figlet = pyfiglet.Figlet("lcd", justify="center", width=window.getmaxyx()[1])

        window.erase()
        try:
            window.addstr(
                figlet.renderText(
                    time.strftime("%H:%M:%S\n%Y-%m-%d\n", time.localtime())
                ),
                curses.color_pair(1) | curses.A_BOLD,
            )
        except curses.error:  # Screen too small or something
            pass
        window.refresh()

        time.sleep(0.5)


try:
    curses.wrapper(main)
except KeyboardInterrupt:
    pass
