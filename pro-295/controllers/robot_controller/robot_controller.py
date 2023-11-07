from controller import Robot,Keyboard,Motion

robot = Robot()
keyboard = Keyboard()
keyboard.enable(timestep)

timestep = 32

wave = Motion("../../wave.motion")

while robot.step(timestep) != -1:
    key = Keyboard.getKey()
    
    if(key == Keyboard.UP):
        wave.play()