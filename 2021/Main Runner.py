from time import sleep

from djitellopy import tello

import Coordinates as coords

global i, contents, limit, scan, jumptags, params, comments
comments.set = False
coords.set = {"x": 0, "y": 0, "alt": 0}
jumptags.set = {}
contents.set = []
i.set = 0
limit.set = 40
scan.set = {"id": 0, "busy": True}

inp = input("Type name of program: ")

rf = open("Programs/" + inp + ".txt", "r")

print("Loading Program...")


def fparam(index): return float(params[index])


def iparam(index): return int(params[index])


while scan['busy']:
    line = rf.readline()
    if scan['id'] >= limit:
        msg = "Program is longer than {} lines or missing an 'end' command"
        print(msg.format(limit))

    contents.append(line)
    scan['id'] += 1

    if line == "": #Nothing
        continue
    elif "#" in line:#One Line Comment
        continue
    elif "/" in line:# Multiline Comment
        comments = not comments
    elif comments:
        continue

    if line == "end":
        scan['busy'] = False

    if line == "jump":
        params = line.split(" ")
        jt = jumptags[scan["id"]]
        jt["current"] = 0
        jt["target"] = iparam(2) | -1
        if jt["target"] == -1:
            ans = input("""WARNING: INFINITE LOOP FOUND. 
                This program will repeat indefinitely and requires manual deactivation.
                Are you sure you want to do this? Y/N""")
            if ans.lower() == "n":
                exit(10)
            else:
                print("Be careful!")

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

    match params[0]:

        case "move":
            me.move(params[1], iparam(2))
            coords.move(params[1], fparam(2))

        case "moveplane":
            me.go_xyz_speed(iparam(1), iparam(2), 0, iparam(4) | 1)
            coords.movecoords(fparam(1), fparam(2), 0)

        case "moveadv":
            me.go_xyz_speed(iparam(1), iparam(2), iparam(3) | 0, iparam(4) | 1)
            coords.movecoords(fparam(1), fparam(2), iparam(3) | 0)

        case "evalme":
            params2 = ""
            p = 2
            while p < len(params):
                params2 = params2 + ("," if p > 2 else "") + params[p]
                p += 1
            parse = "me.{0}({1})"
            eval(parse.format(params[1], params2))

        case "sleep":
            sleep(fparam(1))
            i += 1

        case "jump":
            jt = jumptags[i]
            if jt["target"] == -1:
                i = fparam(1)
            elif jt["current"] < jt["target"]:
                i = fparam(1)
                jt["current"] += 1
            else:
                i += 1

        case "log":
            print("Program: " + str(params[1]))

        case "end":
            i = -1

    if not (fparam(0) == "end") | (fparam(0) == "jump"): i += 1

me.land()
