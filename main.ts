input.onButtonPressed(Button.A, function () {
    Ship.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.AB, function () {
    Laser = game.createSprite(Ship.get(LedSpriteProperty.X), Ship.get(LedSpriteProperty.Y))
    for (let index = 0; index < 5; index++) {
        basic.pause(100)
        Laser.change(LedSpriteProperty.Y, -1)
        if (Laser.get(LedSpriteProperty.X) == alien.get(LedSpriteProperty.X) && Laser.get(LedSpriteProperty.Y) == alien.get(LedSpriteProperty.Y)) {
            game.addScore(1)
            alien.delete()
        }
    }
    Laser.delete()
})
input.onButtonPressed(Button.B, function () {
    Ship.change(LedSpriteProperty.X, 1)
})
let Laser: game.LedSprite = null
let alien: game.LedSprite = null
let Ship: game.LedSprite = null
Ship = game.createSprite(2, 4)
alien = game.createSprite(0, 0)
alien.set(LedSpriteProperty.Blink, 8)
game.setScore(0)
basic.forever(function () {
    alien.move(1)
    alien.ifOnEdgeBounce()
    basic.pause(500)
    if (alien.isDeleted()) {
        alien = game.createSprite(0, 0)
        alien.set(LedSpriteProperty.Blink, 8)
    }
})
