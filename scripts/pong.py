"""
Copyright Kinvert All Rights Reserved
If you would like to use this code for
business or education please contact
us for permission at:
www.kinvert.com/
Free for personal use
"""

import anki_vector
from anki_vector.util import degrees
import random
import sys
import time

try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit("Cannot import from PIL. Do `pip3 install --user Pillow` to install")


def npc_vector(bx, by, bvx, bvy):
    return by + random.randint(-5, 5)


def draw_face(x, y, bx, by, px, py, vx, vy):
    dimensions = (184, 96)
    face_image = Image.new(
        'RGBA', dimensions, (0, 0, 0, 255))
    dc = ImageDraw.Draw(face_image)
    dc.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=(255, 255, 0, 255))
    dc.rectangle([px - 3, py - 10, px, py + 10], fill=(0, 0, 255, 255))
    dc.rectangle([vx + 3, vy - 10, vx, vy + 10], fill=(255, 0, 0, 255))
    return face_image


def impact(bx, by, bvx, bvy, paddleY):
    if abs(paddleY - by) < 10:
        bvx = bvx * -1
        bvy += (0.5 * (by - paddleY))
        if abs(bvy) < 0.2:
            bvy = 0.5
        bvx = bvx * 1.1
    return bvx, bvy


args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial) as robot:
    robot.behavior.set_head_angle(degrees(45.0))
    robot.say_text("Don't touch me yet")
    untouchTotal = 0
    for i in range(20):
        untouchTotal += robot.touch.last_sensor_reading.raw_touch_value
    untouched = untouchTotal / 20.0
    time.sleep(1.0)
    robot.say_text("touch my whole back")
    while not robot.touch.last_sensor_reading.is_being_touched:
        time.sleep(0.1)
    time.sleep(1.0)
    touchTotal = 0
    for i in range(20):
        touchTotal += robot.touch.last_sensor_reading.raw_touch_value
    touched = touchTotal / 20.0
    diff = touched - untouched
    robot.say_text("OK you can stop. Get ready. You are blue.")

    over = 0
    bx = 90
    by = 40
    bvx = -5
    bvy = -1
    px = 10
    vx = 173
    while not over:
        py = 95 * ((robot.touch.last_sensor_reading.raw_touch_value - untouched) / diff)
        vy = npc_vector(bx, by, bvx, bvy)
        if by <= 0:
            bvy = bvy * -1
        if by > 95:
            bvy = bvy * -1
        if bx <= px and bx >= 0:
            bvx, bvy = impact(bx, by, bvx, bvy, py)
        if bx >= vx and bx <= 183:
            bvx, bvy = impact(bx, by, bvx, bvy, vy)
        bx += bvx
        by += bvy
        if bx < 0:
            robot.say_text("I win")
            over = 1
        elif bx > 183:
            robot.say_text("You win")
            over = 1

        face_image = draw_face(0, 0, bx, by, px, py, vx, vy)
        screen_data = anki_vector.screen.convert_image_to_screen_data(
            face_image)
        robot.screen.set_screen_with_image_data(
            screen_data, 0.1, interrupt_running=True)
        if bvx < 0 and bx < 90:
            time.sleep(0.1)
        else:
            time.sleep(0.01)