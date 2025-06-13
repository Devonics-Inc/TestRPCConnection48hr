import time
from fairino import Robot
robot = Robot.RPC('192.168.58.2')
for i in range(4320):
    ret = robot.Mode(1) #Robot cut to manual mode
    print("Robot cut to manual mode", ret)
    time.sleep(4)
    ret = robot.Mode(0)
    print("Robot cut to automatic mode", ret)
    time.sleep(4)
    desc_pos1 = [36.794,-475.119, 65.379, -176.938, 2.535, -179.829]
    desc_pos2 = [136.794,-475.119, 65.379, -176.938, 2.535, -179.829]
    desc_pos3 = [236.794,-475.119, 65.379, -176.938, 2.535, -179.829]
    tool = 0 #Tool coordinate system number
    user = 0 #Workpiece coordinate system number
    ret = robot.MoveL(desc_pos1, tool, user) # Cartesian space linear motion
    print("Cartesian space linear motion point 1: error code", ret)
    time.sleep(4)
    robot.MoveL(desc_pos2, tool, user, vel=20, acc=100)
    print("Cartesian space linear motion point 2: error code", ret)
    time.sleep(4)
    robot.MoveL(desc_pos3, tool, user, offset_flag=1, offset_pos=[10,10,10,0,0,0])
    print("Cartesian space linear motion point 3: error code", ret)
    time.sleep(4)
    hour = i%1800
    if hour == 0:
        print(f"\n Hour {hour} passed okay \n")
