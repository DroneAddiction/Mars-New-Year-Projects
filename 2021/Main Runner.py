from time import sleep

from djitellopy import tello

import KeyPressModule as kp

import json

inp = input("Type name of program: ")

rawrf = open("Programs/" + inp + ".txt", "r")
rawfa = open("Function Aliases.json", "r")

print("Loading Program...")

print("Compiling...")

# Load Additional Files

fa = json.loads(rawfa.read())
rawfa.close()

rf = rawrf.read()
rawrf.close()

forward = "forward"
back = "forward"
left = "forward"
right = "forward"
up = "forward"
down = "forward"

# Compile Code
program = rf.split("\n")

e = 0
for line in program:
    params = line.split(" ")
    parameters = "(" + ",".join(params[1:]) + ")"
    program[e] = fa[params[0]] + parameters
    e += 1

print(program)
print("Success!")

me = tello.Tello()
me.connect()

bat = me.get_battery()

batreport = "{0} Percent, Starting {1}..."
print(batreport.format(bat, inp))

me.send_rc_control(0, 0, 0, 0)

kp.init()

sleep(0.1)

me.takeoff()

i = 0

while i < len(program):
    print(program[i])
    eval(program[i])
    i += 1
    if kp.getKey("SPACE"): i = len(program)

me.land()
