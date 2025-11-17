from panda_desk import Desk
import trio
import os
import json


async def main():
    robot_ip = "172.16.0.2" # Change this to your robot's IP address
    desk = Desk(robot_ip, platform="panda")

    username = os.environ.get("PANDA_USERNAME") # Change this to your username
    password = os.environ.get("PANDA_PASSWORD") # Change this to your password

    await desk.login(username=username, password=password)
    await desk.take_control(force=True)
    await desk.activate_fci()
    gripper_parameters = await desk.get_eef_parameters()
    print(gripper_parameters)
    gripper_parameters["parameters"]["mass"] = 0.9448
    response = await desk.set_eef_parameters(gripper_parameters)
    print(response)
    breakpoint()

    print(response)
    pass


if __name__ == "__main__":
    trio.run(main)
