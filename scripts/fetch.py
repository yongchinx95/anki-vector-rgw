import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps
import time


def main():
    '''Play fetch with Vector

    Touch his back to signal to him that he can go get his cube

    Once he comes back, touch his back again to tell him to put down the cube
    '''
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_off_charger()

        robot.behavior.set_head_angle(degrees(-5.0))
        robot.behavior.set_lift_height(0.0)

        print("Connecting to a cube...")
        robot.world.connect_cube()

        robot.behavior.say_text("I am looking for my cube and trying to fetch it")

        for i in range(2):
            dock_response = False
            docking_result = None
            while not robot.touch.last_sensor_reading.is_being_touched:
                robot.motors.set_wheel_motors(-50, 50)
                time.sleep(0.1)
                robot.motors.set_wheel_motors(50, -50)
                time.sleep(0.1)
            robot.motors.set_wheel_motors(0, 0)
            time.sleep(0.25)
            dock_response = robot.behavior.dock_with_cube(
                robot.world.connected_light_cube,
                num_retries=3)
            if dock_response:
                docking_result = dock_response.result
                robot.motors.set_lift_motor(50)
                time.sleep(1)
                robot.behavior.turn_in_place(degrees(90))
                robot.behavior.drive_straight(distance_mm(100), speed_mmps(100))
                while not robot.touch.last_sensor_reading.is_being_touched:
                    robot.motors.set_wheel_motors(-50, 50)
                    time.sleep(0.1)
                    robot.motors.set_wheel_motors(50, -50)
                    time.sleep(0.1)
                robot.motors.set_wheel_motors(0, 0)
                time.sleep(0.25)
                robot.motors.set_lift_motor(-50)
                time.sleep(1)
                robot.behavior.say_text("Here is your cube!")
                robot.behavior.turn_in_place(degrees(180))

        robot.world.disconnect_cube()


if __name__ == "__main__":
    main()
