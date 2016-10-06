from time import sleep
import pyscreenshot as ImageGrab
from pymouse import PyMouse
from pykeyboard import PyKeyboard

# Insert here the coordinates (x, y) on your screen,
# so the script can click on the "play" button
play_button = (1617, 963)

# Inset here the coordinates to get the tree branches,
# in format (x, 0, x+1, y), where
# x - the X "axis" that sections/cut the branches
# y - Any pixel below the lowest branch (in case of doubt,
#     put the height of the screen, in pixels)
bbox = (1554, 0, 1555, 671)

# Insert here the Y coordinates to look for the branches. You HAVE to put six
# values. If you can't see 6 branches at time on your screen, try to zoom out
# the browser. Usually, the values will be equally spaced.
heights = [170, 270, 370, 470, 570, 670]

mouse = PyMouse()
keyboard = PyKeyboard()


def right():
    keyboard.tap_key(keyboard.right_key)


def left():
    keyboard.tap_key(keyboard.left_key)


def play():
    x, y = play_button
    mouse.click(x, y, 1)


def get_steps():
    im = ImageGrab.grab(bbox=bbox).convert('RGB')

    def get_step(h):
        color_ = im.getpixel((0, h))
        return right if sum(color_) < 350 else left

    return [get_step(heights[0]),
            get_step(heights[1]),
            get_step(heights[2]),
            get_step(heights[3]),
            get_step(heights[4]),
            get_step(heights[5])]


if __name__ == "__main__":
    play()
    sleep(0.5)

    while True:
        steps = get_steps()
        while steps:
            for i in range(0, 5):
                f = steps.pop()
                f()
                f()

            # ======================== 6
            f = steps.pop()
            f()
            sleep(0.03)
            f()
        sleep(0.21)
