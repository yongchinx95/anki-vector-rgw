import threading
import anki_vector
import random
import os

with anki_vector.Robot() as robot:
    battery_state = robot.get_battery_state()
    if battery_state:
        print("Robot battery voltage: {0}".format(battery_state.battery_volts))
        print("Robot battery Level: {0}".format(battery_state.battery_level))
        print("Robot battery is charging: {0}".format(battery_state.is_charging))
        print("Robot is on charger platform: {0}".format(battery_state.is_on_charger_platform))
    
    #If Vector is on his charger, turn off the charger light
    if (battery_state.is_on_charger_platform == True):
        os.system("cd -/vector_sdk/ && ./codesend 3553014 -1 400")

    #If Vector's battery is over 3.62 volts, turn off the charger light
    elif (battery_state.battery_volts >= 3.62):
        os.system("cd -/vector_sdk/ && ./codesend 3553014 -1 400")

    #If Vector's battery is below 3.62 volts, say 2 random phrases then turn on the charger light
    elif (battery_state.battery_volts <= 3.62):
        Str = random.randint(1,3)
        print(Str)

        if Str==1:
                robot.say_text("Battery getting Low!!")
        
        if Str==2:
                robot.say_text("Energy almost depleted!!")
        
        if Str==3:
                robot.say_text("Voltage critical!!")
        
        Str = random.randint(4,6)
        print(Str)

        if Str==4:
                robot.say_text("Turning on charger light")

        if Str==5:
                robot.say_text("energize charger")

        if Str==6:
                robot.say_text("illuminating home base")
        
        os.system("cd -/vector_sdk/ && ./codesend 3553014 -1 400")