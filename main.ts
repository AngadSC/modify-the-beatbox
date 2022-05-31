let tune = 0
music.setTempo(300)
basic.forever(function () {
    tune = pins.analogReadPin(AnalogPin.P1)
    if (tune >= 725 && tune <= 1023) {
        pins.digitalWritePin(DigitalPin.P13, 1)
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.pause(100)
        pins.digitalWritePin(DigitalPin.P13, 0)
        basic.pause(100)
    } else if (tune >= 350 && tune < 725) {
        pins.digitalWritePin(DigitalPin.P14, 1)
        music.playTone(247, music.beat(BeatFraction.Whole))
        basic.pause(100)
        pins.digitalWritePin(DigitalPin.P14, 0)
        basic.pause(100)
    } else if (tune >= 50 && tune < 350) {
        pins.digitalWritePin(DigitalPin.P15, 1)
        music.playTone(220, music.beat(BeatFraction.Whole))
        basic.pause(100)
        pins.digitalWritePin(DigitalPin.P15, 0)
        basic.pause(100)
    }
})
