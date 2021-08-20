from djitellopy import tello

me = tello.Tello()
me.connect()

print(me.get_battery())

me.takeoff()

# Get to the desired height
me.go_xyz_speed(0, 0, 114, 10)

#Thru Gate
me.move_forward(100)

#Dive Gate
me.move_down(76)
me.move_forward(100)

#Ladder Gate
me.move_up(76)
me.move_back(50)
me.move_up(76)
me.move_forward(50)
me.move_back(250)
me.move_down(76)

me.land()
