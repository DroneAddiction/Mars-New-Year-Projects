from djitellopy import tello
from time import sleep
import Coordinates as coords

global i, contents, limit, scan, jumptags
coords.set = {"x": 0,"y": 0,"alt": 0}
jumptags = {}
contents = []
i = 0
limit = 40
scan = {"id": 0, "busy": True}

inp = input("Type name of program: ")

rf = open("Programs/" + inp + ".txt", "r")

print("Loading Program...")

while scan['busy']:
    line = rf.readline()
    contents.append(line)
    scan['id'] += 1

    if line == "end":
        scan['busy'] = False

    if line == "jump":
        params = line.split(" ")
        jumptags[scan["id"]]
        jt["current"] = 0
        jt["target"] = params[2]

    if scan['id'] >= limit:
        print("Program is longer than $limit lines or missing an 'end' command")

print("Success!")

me = tello.Tello()
# me.connect()

bat = 100  # me.get_battery()

batreport = "{0} Percent, Starting {1}..."
print(batreport.format(100, inp))

if bat < 10:
    print("Please change out the battery!")
    exit(5)

# me.send_rc_control(0, 0, 0, 0)

# me.takeoff()

coords.init(me.get_height())

while (i < len(contents)) | (i == -1):
    params = contents[i].split(" ")

    switch params[0]:

        case "move":
            me.move(params[1], params[2])

            i += 1
            break

        case "moveadv":



        case "sleep":
            if true:
                sleep(float(params[1]))
            else:
                print("Attempted to use a string in place of an int")
                i += 1
            break

        case "jump":
            jt = jumptags[i]
            if jt[current] < jt[target]:
                i = params[1]
                jt[current] += 1
            else:
                i += 1
            break

        case "log":
            print("Program: " + params[1])
            break

        case "end":
            i = -1
            break

    if not (params[0] == "end") | (params[0] == "jump"): i += 1

me.land()
