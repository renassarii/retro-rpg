import arcade
import random

WIDTH = 500
HEIGHT = 400


class Kampf(arcade.Window):
    def __init__(self, player_hp=100, enemy_hp=80):
        super().__init__(WIDTH, HEIGHT, "RPG KAMPF")

        arcade.set_background_color(arcade.color.DARK_SLATE_BLUE)

        self.player_hp = player_hp
        self.enemy_hp = enemy_hp

        self.menu = ["SCHLAG", "MAGIE", "ITEMS", "FLUCHTEN"]
        self.selected = 0

        self.message = ""
        self.finished = False

    def on_draw(self):
        self.clear()

        # HP Anzeige
        arcade.draw_text(f"DU: {self.player_hp} HP", 20, 350, arcade.color.WHITE, 16)
        arcade.draw_text(f"ENEMY: {self.enemy_hp} HP", 20, 320, arcade.color.RED, 16)

        # Nachricht
        arcade.draw_text(self.message, 20, 250, arcade.color.YELLOW, 14)

        # Menü
        y = 100
        for i, item in enumerate(self.menu):
            color = arcade.color.GREEN if i == self.selected else arcade.color.WHITE
            arcade.draw_text(item, 50, y, color, 20)
            y -= 30

        if self.finished:
            arcade.draw_text("KAMPF ENDE", 180, 200, arcade.color.GOLD, 24)

    # =========================
    # INPUT
    # =========================
    def on_key_press(self, key, modifiers):

        if self.finished:
            return

        # Menü hoch/runter
        if key == arcade.key.UP:
            self.selected = (self.selected - 1) % len(self.menu)

        if key == arcade.key.DOWN:
            self.selected = (self.selected + 1) % len(self.menu)

        # Auswahl
        if key == arcade.key.SPACE:
            self.execute_action()

    # =========================
    # KAMPF LOGIK
    # =========================
    def execute_action(self):

        action = self.menu[self.selected]

        # ================= SCHLAG =================
        if action == "SCHLAG":
            dmg = random.randint(10, 20)
            self.enemy_hp -= dmg
            self.message = f"Du schlägst für {dmg} Schaden!"

        # ================= MAGIE =================
        elif action == "MAGIE":
            dmg = random.randint(15, 30)
            self.enemy_hp -= dmg
            self.message = f"Magie! {dmg} Schaden!"

        # ================= ITEMS =================
        elif action == "ITEMS":
            heal = random.randint(10, 25)
            self.player_hp += heal
            self.message = f"Du heilst dich +{heal} HP"

        # ================= FLUCHTEN =================
        elif action == "FLUCHTEN":
            if random.random() < 0.5:
                self.message = "Du bist geflohen!"
                self.finished = True
                return
            else:
                self.message = "Flucht fehlgeschlagen!"

        # ================= ENEMY TURN =================
        if self.enemy_hp > 0:
            enemy_dmg = random.randint(5, 15)
            self.player_hp -= enemy_dmg
            self.message += f" | Gegner macht {enemy_dmg}"

        # ================= CHECK END =================
        if self.enemy_hp <= 0:
            self.message = "GEWONNEN!"
            self.finished = True

        if self.player_hp <= 0:
            self.message = "VERLOREN!"
            self.finished = True