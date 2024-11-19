#!/usr/bin/env python3

# 

"""Hello World

Make Vector say 'Hello World' in this simple Vector SDK example program.
"""
import os
import sys
import time

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps

anims = [
		 	"anim_dancebeat_cantdothat_01",
		 	"anim_dancebeat_eyebeat_01",
			"anim_dancebeat_eyebeat_left_01",
			"anim_dancebeat_eyebeat_right_01",
			"anim_dancebeat_eyehold_01",
			"anim_dancebeat_getin_01",
			"anim_dancebeat_getin_02",
			"anim_dancebeat_getout_01",
			"anim_dancebeat_getout_02",
			"anim_dancebeat_getready_01",
			"anim_dancebeat_headlift_01",
			"anim_dancebeat_headliftbody_back_01",
			"anim_dancebeat_headliftbody_fwd_01",
			"anim_dancebeat_headliftbody_left_large_01",
			"anim_dancebeat_headliftbody_left_med_01",
			"anim_dancebeat_headliftbody_left_small_01",
			"anim_dancebeat_headliftbody_right_large_01",
			"anim_dancebeat_headliftbody_right_med_01",
			"anim_dancebeat_headliftbody_right_small_01",
			"anim_dancebeat_headnod_01",
			"anim_dancebeat_headnod_down_01",
			"anim_dancebeat_idle_01",
			"anim_dancebeat_listening_01",
			"anim_dancebeat_listening_02",
			"anim_dancebeat_listening_03",
			"anim_dancebeat_pivot_left_01",
			"anim_dancebeat_pivot_right_01",
			"anim_dancebeat_quit_01",
			"anim_dancebeat_scoot_left_01",
			"anim_dancebeat_scoot_right_01"
		]

steps = [
			["anim_dancebeat_headnod_01",1],
			["anim_dancebeat_headnod_01",1],
			["anim_dancebeat_headnod_01",1],
			["anim_dancebeat_headnod_01",1],

			["anim_dancebeat_headnod_01",1],
			["anim_dancebeat_headnod_01",1],
			["anim_dancebeat_headnod_01",1],
			["anim_dancebeat_headnod_01",1],
			
			["anim_dancebeat_headliftbody_back_01",1],
			["anim_dancebeat_headliftbody_fwd_01",1],
			["anim_dancebeat_headliftbody_back_01",1],
			["anim_dancebeat_headliftbody_fwd_01",1],

			["anim_dancebeat_headliftbody_back_01",1],
			["anim_dancebeat_headliftbody_fwd_01",1],
			["anim_dancebeat_headliftbody_back_01",1],
			["anim_dancebeat_headliftbody_fwd_01",1],


			["anim_dancebeat_headliftbody_left_large_01",1],
			["anim_dancebeat_headliftbody_right_large_01",1],
			["anim_dancebeat_headliftbody_right_large_01",1],
			["anim_dancebeat_headliftbody_left_large_01",1],

			
			["anim_dancebeat_headliftbody_left_large_01",1],
			["anim_dancebeat_headliftbody_right_large_01",1],
			["anim_dancebeat_headliftbody_right_large_01",1],
			["anim_dancebeat_headliftbody_left_large_01",1],


			["anim_dancebeat_headliftbody_left_large_01",1],
			["anim_dancebeat_headliftbody_right_large_01",1],
			["anim_dancebeat_headliftbody_right_large_01",1],
			["anim_dancebeat_headliftbody_left_large_01",1],

			
			["anim_dancebeat_headliftbody_left_large_01",1],
			["anim_dancebeat_headliftbody_right_large_01",1],
			["anim_dancebeat_headliftbody_right_large_01",1],
			["anim_dancebeat_headliftbody_left_large_01",1],


			#"anim_dancebeat_headliftbody_left_large_01":3,
			#"anim_dancebeat_headliftbody_left_med_01":4,
			#"anim_dancebeat_headliftbody_left_small_01":5,
			#"anim_dancebeat_headliftbody_right_large_01":6,
			#"anim_dancebeat_headliftbody_right_med_01":7,
			#"anim_dancebeat_headliftbody_right_small_01":8,
			#"anim_dancebeat_headnod_01":9,
			#"anim_dancebeat_headnod_down_01":10	
		]	

# list of robot serial numbers. Replace with your serials
serials = ["00001234","00002345", "00003456", "00004567","00005678"] 


robots = []

for serial in serials:
    print(serial)
    robots.append(anki_vector.AsyncRobot(serial))

# Connect to the Robot
for robot in robots:
    robot.connect()
    
for robot in robots:
	robot.behavior.drive_off_charger()

# If necessary, move Vector's Head and Lift to make it easy to see his face
for robot in robots:
	robot.behavior.set_head_angle(degrees(0.0))
time.sleep(1)

for robot in robots:
	robot.behavior.set_lift_height(0.0)
time.sleep(1)


time.sleep(5)
#print("Say 'Hello World'...")
robot.behavior.say_text("Ready to Rock?")
time.sleep(2)

#for ani in anims:
#	print(ani)
#	robot.anim.play_animation(ani)
#	time.sleep(2)

robot.audio.stream_wav_file("smoothcriminal.wav",100)
#robot.audio.stream_wav_file("smooth_.wav",100)


for step in steps:
	print(step[0])
	print(step[1])
	for robot in robots:
		robot.anim.play_animation(step[0])
	time.sleep(step[1])

print("front")
for robot in robots:
	robot.behavior.drive_straight(distance_mm(50), speed_mmps(100))
time.sleep(2)

print("back")
for robot in robots:
	robot.behavior.drive_straight(distance_mm(-50), speed_mmps(100))
time.sleep(2)

print("front")
for robot in robots:
	robot.behavior.drive_straight(distance_mm(70), speed_mmps(100))
time.sleep(2)

print("back")
for robot in robots:
	robot.behavior.drive_straight(distance_mm(-70), speed_mmps(100))
time.sleep(2)

print("spin")
for robot in robots:
	robot.behavior.turn_in_place(degrees(360))
time.sleep(2)

print("spin")
for robot in robots:
	robot.behavior.turn_in_place(degrees(-360))
time.sleep(2)

print("spin45")
for robot in robots:
	robot.behavior.set_lift_height(1.0)
	robot.behavior.turn_in_place(degrees(45))
time.sleep(2)

print("spin45")
for robot in robots:
	robot.behavior.set_lift_height(0.0)
	robot.behavior.turn_in_place(degrees(-45))
time.sleep(2)

print("spin45")
for robot in robots:
	robot.behavior.set_lift_height(1.0)
	robot.behavior.turn_in_place(degrees(-45))
time.sleep(2)

print("spin45")
for robot in robots:
	robot.behavior.set_lift_height(0.0)
	robot.behavior.turn_in_place(degrees(45))
time.sleep(2)

print("front")
for robot in robots:
	robot.behavior.set_lift_height(1.0)
	robot.behavior.drive_straight(distance_mm(70), speed_mmps(100))
time.sleep(2)

print("back")
for robot in robots:
	robot.behavior.set_lift_height(0.0)
	robot.behavior.drive_straight(distance_mm(-70), speed_mmps(100))
time.sleep(2)

time.sleep(10)
for robot in robots:
	robot.disconnect()

