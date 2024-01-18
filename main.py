def on_button_pressed_a():
    Ship.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Laser
    Laser = game.create_sprite(Ship.get(LedSpriteProperty.X), Ship.get(LedSpriteProperty.Y))
    for index in range(5):
        basic.pause(100)
        Laser.change(LedSpriteProperty.Y, -1)
        if Laser.is_touching(alien):
            music.play(music.builtin_playable_sound_effect(soundExpression.mysterious),
                music.PlaybackMode.IN_BACKGROUND)
            game.add_score(1)
            Laser.delete()
            alien.delete()
    Laser.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Ship.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

alien: game.LedSprite = None
Laser: game.LedSprite = None
Ship: game.LedSprite = None
Ship = game.create_sprite(2, 4)
Time = 2000
game.set_score(0)

def on_forever():
    global alien, Time
    alien = game.create_sprite(randint(0, 4), 0)
    for index2 in range(4):
        basic.pause(Time)
        alien.change(LedSpriteProperty.Y, 1)
    if game.score() <= 5:
        Time = 2000
    elif game.score() <= 10:
        Time = 1000
    elif game.score() <= 15:
        Time = 500
    if alien.is_touching_edge():
        game.game_over()
basic.forever(on_forever)
