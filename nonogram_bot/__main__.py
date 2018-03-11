"""Main class for bot."""

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

    LOG = BOT_SKELETON.log

    FILENAME = f"nonogrid_{datetime.now()}.jpg"

    while True:
        LOG.info("Generating a puzzle")
        grid = nonogen.nono.NonoGrid(random.choice(range(5, 21)), random.choice(range(5, 21)))

        LOG.info(f"Generated a {len(grid.squares[0])} by {len(grid.squares)} puzzle.")

        LOG.info("Putting stuff in the puzzle.")
        nonogen.gen_perlin(grid)

        LOG.info("Generating hints for the stuff.")
        grid.gen_hints()

        LOG.info("Printing the hints and stuff.")
        grid.to_picture(FILENAME)

        LOG.info("Saving with solutions as well.")
        grid.to_picture(f"solved_{FILENAME}", has_value_color="black")

        encoded = grid.encode()
        LOG.info(f"Puzzle code is: {encoded}")
        BOT_SKELETON.store_extra_info("encoded_puzzle", encoded)

        solution_url = f"https://andrewmichaud.com/nonogram?board={encoded}&solved=true"
        url = f"https://andrewmichaud.com/nonogram?board={encoded}"

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
                f"You can see the bare puzzle (not playable) at {url}")
        status = BOT_SKELETON.send_with_one_media(TEXT, FILENAME)

        BOT_SKELETON.nap()
