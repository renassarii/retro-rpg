import arcade
import random

WIDTH = 400
HEIGHT = 200
PLAYER_SPEED = 100

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Smooth Movement with Keys")
        arcade.set_background_color(arcade.color.BLACK)

        self.player = arcade.Sprite("character/gandalf.png", 1)
        self.player.center_x = 100
        self.player.center_y = 50

        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

        self.enemies = arcade.SpriteList()
        for _ in range(1):
            enemy = arcade.Sprite("character/Franz.png", 1)
            enemy.center_x = 300
            enemy.center_y = 100
            self.enemies.append(enemy)

        # Tasten-Tracking
        self.keys_held = set()

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.enemies.draw()

    '''def on_update(self, delta_time):
        # Geschwindigkeit zurücksetzen
        self.player.change_x = 0
        self.player.change_y = 0

        # Tasten prüfen
        if arcade.key.W in self.keys_held or arcade.key.UP in self.keys_held:
            self.player.change_y = PLAYER_SPEED
        if arcade.key.S in self.keys_held or arcade.key.DOWN in self.keys_held:
            self.player.change_y = -PLAYER_SPEED
        if arcade.key.A in self.keys_held or arcade.key.LEFT in self.keys_held:
            self.player.change_x = -PLAYER_SPEED
        if arcade.key.D in self.keys_held or arcade.key.RIGHT in self.keys_held:
            self.player.change_x = PLAYER_SPEED

        # Spieler bewegen
        self.player.center_x += self.player.change_x * delta_time
        self.player.center_y += self.player.change_y * delta_time

        # Gegner bewegen
        for enemy in self.enemies:
            enemy.center_x += random.randint(-2, 2)
            enemy.center_y += random.randint(-2, 2)

    def on_key_press(self, key, modifiers):
        self.keys_held.add(key)

    def on_key_release(self, key, modifiers):
        if key in self.keys_held:
            self.keys_held.remove(key)'''

if __name__ == "__main__":
    game = Game()
    arcade.run()