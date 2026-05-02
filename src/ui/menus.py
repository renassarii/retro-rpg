"""Battle menu, item/magic popups, and the level-choice screen."""

import arcade

from src.data.items import (
    BATTLE_MENU,
    ITEM_NAMES,
    LEVEL_UP_OPTIONS,
    MAGIC_BP_COST,
    MAGIC_NAMES,
)


def draw_main_battle_menu(game, base_x=200, y=70):
    """Bottom-of-screen action list (Punch / Magic / Item / Escape)."""
    for i, item in enumerate(BATTLE_MENU):
        if i == game.selected:
            color = _selected_color(item)
        else:
            color = arcade.color.WHITE
        arcade.draw_text(item, base_x + i * 150, y, color, 18)


def _selected_color(item):
    if item == "Magic":
        return (160, 80, 255)
    if item == "Escape":
        return (255, 16, 240)
    if item == "Punch":
        return (150, 0, 24)
    return (255, 255, 0)


def draw_magic_popup(game):
    popup_x = 250
    popup_y = 200
    popup_width = 200
    popup_height = 160

    arcade.draw_rect_filled(
        arcade.rect.XYWH(popup_x, popup_y, popup_width, popup_height),
        arcade.color.BLACK,
    )

    start = game.magic_scroll
    end = start + game.visible_magic

    for i, magic in enumerate(MAGIC_NAMES[start:end]):
        real_index = start + i
        y = popup_y + 70 - i * 45
        is_selected = real_index == game.selected_3

        if is_selected:
            arcade.draw_rect_filled(
                arcade.rect.XYWH(popup_x, y, popup_width, 40),
                (160, 80, 255, 180),
            )
            arcade.draw_rect_filled(
                arcade.rect.XYWH(popup_x, y, 220, 40),
                (190, 120, 255, 140),
            )

        texture = game.magic_textures[magic]
        arcade.draw_texture_rect(
            texture, arcade.rect.XYWH(popup_x - 80, y, 30, 30)
        )

        text_color = arcade.color.WHITE if is_selected else arcade.color.LIGHT_GRAY
        arcade.draw_text(magic, popup_x - 40, y - 8, text_color, 12)

        cost_color = arcade.color.WHITE if is_selected else arcade.color.GRAY
        arcade.draw_text(
            f"-{MAGIC_BP_COST[magic]} BP",
            popup_x + 60,
            y - 8,
            cost_color,
            12,
        )

        if is_selected:
            arcade.draw_text("▶", popup_x - 110, y - 10, arcade.color.BLACK, 18)

    if game.magic_scroll > 0:
        arcade.draw_text("↑", popup_x + 70, popup_y + 80, arcade.color.WHITE, 16)
    if game.magic_scroll + game.visible_magic < len(MAGIC_NAMES):
        arcade.draw_text("↓", popup_x + 70, popup_y - 60, arcade.color.WHITE, 16)


def draw_item_popup(game):
    popup_x = 250
    popup_y = 200
    popup_width = 200
    popup_height = 160

    arcade.draw_rect_filled(
        arcade.rect.XYWH(popup_x, popup_y, popup_width, popup_height),
        arcade.color.BLACK,
    )

    start = game.item_scroll
    end = start + game.visible_item

    for i, item in enumerate(ITEM_NAMES[start:end]):
        real_index = start + i
        y = popup_y + 70 - i * 45
        is_selected = real_index == game.selected_2

        if is_selected:
            arcade.draw_rect_filled(
                arcade.rect.XYWH(popup_x, y, popup_width, 40),
                (255, 220, 0, 180),
            )
            arcade.draw_rect_filled(
                arcade.rect.XYWH(popup_x, y, 220, 40),
                (255, 220, 0, 180),
            )

        texture = game.item_textures[item]
        arcade.draw_texture_rect(
            texture, arcade.rect.XYWH(popup_x - 80, y, 30, 30)
        )

        text_color = arcade.color.BLACK if is_selected else arcade.color.WHITE
        count = game.inventory[item]
        arcade.draw_text(
            f"{count}x {item}",
            popup_x - 50,
            y - 8,
            text_color,
            12,
        )

        if is_selected:
            arcade.draw_text("▶", popup_x - 110, y - 10, arcade.color.BLACK, 18)

    if game.item_scroll > 0:
        arcade.draw_text("↑", popup_x + 70, popup_y + 80, arcade.color.WHITE, 16)
    if game.item_scroll + game.visible_item < len(ITEM_NAMES):
        arcade.draw_text("↓", popup_x + 70, popup_y - 60, arcade.color.WHITE, 16)


def draw_level_choice(game):
    arcade.draw_texture_rect(
        game.level_ui_bg,
        arcade.rect.XYWH(game.width // 2, game.height // 2, game.width, game.height),
    )

    arcade.draw_text(
        "LEVEL UP! Pick your upgrade",
        game.width / 2,
        380,
        arcade.color.WHITE,
        24,
        anchor_x="center",
    )

    for i, option in enumerate(LEVEL_UP_OPTIONS):
        x = 600 + i * 300
        y = 200

        if game.selected_4 == i:
            box_color = (150, 0, 24) if option == "Health points" else (40, 60, 180)
        else:
            box_color = arcade.color.BLACK

        arcade.draw_rect_filled(
            arcade.rect.XYWH(x, y, 200, 180),
            box_color,
        )

        arcade.draw_texture_rect(
            game.level_icons[option],
            arcade.rect.XYWH(x, y + 40, 80, 80),
        )

        arcade.draw_text(
            option, x, y - 50, arcade.color.WHITE, 18, anchor_x="center"
        )

        if game.selected_4 == i:
            arcade.draw_text("▲", x - 17, y - 80, arcade.color.WHITE, 30)

    arcade.draw_text(
        "Press Space to confirm your choice",
        game.width / 2,
        330,
        arcade.color.LIGHT_GRAY,
        14,
        anchor_x="center",
    )
