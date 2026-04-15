import arcade
import random
from Sequenzen import dialogues

WIDTH = 400
HEIGHT = 200
PLAYER_SPEED = 100


class Game(arcade.Window):
    def __init__(self):
        # 🔥 Start im Fullscreen
        super().__init__(WIDTH, HEIGHT, "Smooth Movement with Keys", fullscreen=True)
        self.set_fullscreen(True)

        arcade.set_background_color(arcade.color.BLACK)

        # ===== PLAYER =====
        self.player = arcade.Sprite("assets/images/characters/gandalf.png", 2)
        self.player.center_x = 100
        self.player.center_y = 50

        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

        # ===== ENEMY =====
        self.enemies = arcade.SpriteList()
        for _ in range(1):
            enemy = arcade.Sprite("assets/images/characters/Franz.png", 2)
            enemy.center_x = 300
            enemy.center_y = 100
            self.enemies.append(enemy)

        # ===== MOVEMENT =====
        self.keys_held = set()

        # ===== DIALOG SYSTEM =====
        self.active_dialog = None
        self.dialog_index = 0
        self.showing_dialog = False

    # =========================
    # DRAW
    # =========================
    def on_draw(self):
        self.clear()

        self.player_list.draw()
        self.enemies.draw()

        # Dialog Box
        if self.showing_dialog:
            arcade.draw_rect_filled(
                arcade.rect.XYWH(200, 50, 100, 100),
                arcade.color.BLACK
            )

            arcade.draw_text(
                dialogues[self.active_dialog][self.dialog_index],
                20, 50,
                arcade.color.WHITE,
                14,
                width=360
            )

    # =========================
    # UPDATE (movement)
    # =========================
    def on_update(self, delta_time):

        self.player.change_x = 0
        self.player.change_y = 0

        if arcade.key.W in self.keys_held or arcade.key.UP in self.keys_held:
            self.player.change_y = PLAYER_SPEED
        if arcade.key.S in self.keys_held or arcade.key.DOWN in self.keys_held:
            self.player.change_y = -PLAYER_SPEED
        if arcade.key.A in self.keys_held or arcade.key.LEFT in self.keys_held:
            self.player.change_x = -PLAYER_SPEED
        if arcade.key.D in self.keys_held or arcade.key.RIGHT in self.keys_held:
            self.player.change_x = PLAYER_SPEED

        self.player.center_x += self.player.change_x * delta_time
        self.player.center_y += self.player.change_y * delta_time



    # =========================
    # INPUT
    # =========================
    def on_key_press(self, key, modifiers):

        self.keys_held.add(key)

        # 🔥 ESC = Fullscreen toggle
        if key == arcade.key.ESCAPE:
            self.set_fullscreen(not self.fullscreen)
            self.set_mouse_visible(True)

        # 🔥 E = Dialog starten
        if key == arcade.key.E:

            hit_list = self.player.collides_with_list(self.enemies)

            if hit_list:
                self.active_dialog = 1
                self.dialog_index = 0
                self.showing_dialog = True

        # 🔥 SPACE = weiter im Dialog
        if key == arcade.key.SPACE:

            if self.showing_dialog:
                self.dialog_index += 1

                if self.dialog_index >= len(dialogues[self.active_dialog]):
                    self.showing_dialog = False

    # =========================
    # KEY RELEASE
    # =========================
    def on_key_release(self, key, modifiers):
        if key in self.keys_held:
            self.keys_held.remove(key)


if __name__ == "__main__":
    game = Game()
    arcade.run()