"""Main class for bot."""

import os
import random
import sys
import time
from datetime import datetime
from os import path

import botskeleton
import nonogen

# Delay between tweets in seconds.
DELAY = 3600 * 6

if __name__ == "__main__":
    SECRETS_DIR = path.join(path.abspath(path.dirname(__file__)), "SECRETS")
    BOT_SKELETON = botskeleton.BotSkeleton(SECRETS_DIR, bot_name="nono_bot", delay=DELAY)

    FONT_NAME = path.join(SECRETS_DIR, "FreeMono.ttf")

    LOG = BOT_SKELETON.log

    FILENAME = f"nonogrid_{datetime.now()}.png"

    while True:
        LOG.info("Generating a puzzle")
        grid = nonogen.nono.NonoGrid(random.choice(range(5, 16)), random.choice(range(5, 16)))

        LOG.info(f"Generated a {len(grid.squares[0])} by {len(grid.squares)} puzzle.")

        LOG.info("Putting stuff in the puzzle.")
        nonogen.gen_perlin(grid)

        LOG.info("Generating hints for the stuff.")
        grid.gen_hints()

        LOG.info("Printing the hints and stuff.")
        grid.to_picture(filename=FILENAME, font_name=FONT_NAME)

        encoded = grid.encode()
        LOG.info(f"Puzzle code is: {encoded}")
        BOT_SKELETON.store_extra_info("encoded_puzzle", encoded)

        url = f"https://drew.life/nonogram?board={encoded}"
        solution_url = f"{url}&solved=true"

        LOG.info("Sending the picture, and hints and stuff.")
        LOG.info(f"The puzzle, without filled squares, is \n{grid}")

        message = random.choice([
            "Here's a puzzle!",
            "I've made a puzzle for you.",
            "I've made a puzzle for you!",
            "Please enjoy this puzzle.",

        ])
        TEXT = (f"{message}\n" +
                f"You can view the solution at {solution_url}.\n" +
                f"You can solve it yourself at {url}")
        CAPTION = f"An unsolved {grid.width} by {grid.height} cell nonogram board."
        status = BOT_SKELETON.send_with_one_media(TEXT, FILENAME, CAPTION)

        os.remove(FILENAME)

        BOT_SKELETON.nap()
