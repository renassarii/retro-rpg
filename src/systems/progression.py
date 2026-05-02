"""Level-up handling for the player character."""

from src.data.dialogues import DIALOGUES
from src.data.items import LEVEL_UP_OPTIONS

HP_LEVEL_UP_AMOUNT = 20
BP_LEVEL_UP_AMOUNT = 20
RUNTIME_LEVEL_DIALOG_ID = 99


def apply_level_choice(game):
    """Apply the upgrade highlighted in the level-choice menu."""
    choice = LEVEL_UP_OPTIONS[game.selected_4]

    if choice == "Health points":
        game.max_hp += HP_LEVEL_UP_AMOUNT
        game.player_hp += HP_LEVEL_UP_AMOUNT
    elif choice == "Mana":
        game.max_bp += BP_LEVEL_UP_AMOUNT
        game.bp += BP_LEVEL_UP_AMOUNT

    xp_to_next = max(0, game.player_max_xp - game.player_xp)
    DIALOGUES[RUNTIME_LEVEL_DIALOG_ID] = {
        "name": "System",
        "lines": [f"Noch {xp_to_next} XP bis zum nächsten Level"],
    }

    game.state = "dialog"
    game.current_dialog_id = RUNTIME_LEVEL_DIALOG_ID
    game.dialog_index = 0
