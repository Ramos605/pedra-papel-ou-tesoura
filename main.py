def on_gesture_shake():
    basic.show_string("Hello!")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

music.play_melody("E G D F B A E G ", 120)

def on_forever():
    pass
basic.forever(on_forever)
