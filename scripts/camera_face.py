import anki_vector

import time

with anki_vector.Robot() as robot:
    robot.vision.enable_display_camera_feed_on_face()
    time.sleep(10.0)