import arcade

class Game(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Dialog System")

        self.dialogues = [
            "Willkommen, Abenteurer...",
            "Ich bin Gandalf.",
            "Deine Reise beginnt jetzt!",
            "Kubilays Füße stinken"
        ]
        self.current_dialog = 0
        self.show_dialog = True

    def on_draw(self):
        self.clear()

        if self.show_dialog:
            # Hintergrund Box
            arcade.draw_rect_filled(
                arcade.rect.XYWH(400, 100, 700, 150),
                arcade.color.BLACK
            )

            arcade.draw_rect_outline(
                arcade.rect.XYWH(400, 100, 700, 150),
                arcade.color.WHITE,
                border_width=3
            )

            # 👇 richtiger Dialogtext
            arcade.draw_text(
                self.dialogues[self.current_dialog],
                100, 100,
                arcade.color.WHITE,
                20,
                width=600
            )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.current_dialog += 1

            if self.current_dialog >= len(self.dialogues):
                self.show_dialog = False


Game()
arcade.run()