tune = 0
music.set_tempo(300)

def on_forever():
    global tune
    tune = pins.analog_read_pin(AnalogPin.P1)
    if tune >= 725 and tune <= 1023:
        pins.digital_write_pin(DigitalPin.P13, 1)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.pause(100)
        pins.digital_write_pin(DigitalPin.P13, 0)
        basic.pause(100)
    elif tune >= 350 and tune < 725:
        pins.digital_write_pin(DigitalPin.P14, 1)
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        basic.pause(100)
        pins.digital_write_pin(DigitalPin.P14, 0)
        basic.pause(100)
    elif tune >= 50 and tune < 350:
        pins.digital_write_pin(DigitalPin.P15, 1)
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
        basic.pause(100)
        pins.digital_write_pin(DigitalPin.P15, 0)
        basic.pause(100)
basic.forever(on_forever)
