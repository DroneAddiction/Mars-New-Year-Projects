from time import sleep

from djitellopy import tello

import KeyPressModule as kp

import json

def run(inp):
    print("Loading Program...")

    rawrf = open(inp + ".txt", "r")
    rf = rawrf.read()
    rawrf.close()

    rawfa = open("Function Aliases.json", "r")
    fa = json.loads(rawfa.read())
    rawfa.close()

    print("Compiling...")

    forward = "forward"
    back = "forward"
    left = "forward"
    right = "forward"
    up = "forward"
    down = "forward"

    # Compile Code
    program = rf.split("\n")

    parsedprogram = []

    e = 0

    for line in program:
        if e >= len(program): break
        elif ("#" in line) | (line == ""): continue
        else:
            params = line.split(" ")
            parameters = "(" + ",".join(params[1:]) + ")"
            parsedprogram.append(fa[params[0]] + parameters)

    print(parsedprogram)
    print("Success!")

    me = tello.Tello()
    me.connect()

    bat = me.get_battery()

    batreport = "{0} Percent, Starting {1}..."
    print(batreport.format(bat, inp))

    me.send_rc_control(0, 0, 0, 0)

    kp.init()

    def moveheight(height):
        target = height - me.get_height()
        if target > 0:
            me.move_up(target)

    sleep(0.1)

    me.takeoff()

    i = 0 
    running = True
    while (i < len(parsedprogram)) & running:
        line = parsedprogram[i]
        print(line)
        eval(line)
        i += 1
        if kp.getKey("SPACE"): running = False

    me.land()


def main():
    inp = input("Type name of program: ")
    run("Programs/" + inp)


if __name__ == '__main__':
    main()
