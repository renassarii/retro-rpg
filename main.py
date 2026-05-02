"""Entry point for Köpek RPG. Run with `python main.py` from the project root."""

import arcade

from src.game import Game


def main():
    Game()
    arcade.run()


if __name__ == "__main__":
    main()
