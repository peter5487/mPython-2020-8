import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(20):
    r = random.randrange(1,7)    
    if r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,57)
        x = x+4
    elif r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,57)
        x = x-4
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z+4,57)
        z = z+4
    elif r == 4:
        mc.setBlocks(x,y,z,x,y,z-4,57)
        z = z-4
    elif r == 5:
        mc.setBlocks(x,y,z,x,y+4,z,57)
        y = y+4
    elif r == 6:
        mc.setBlocks(x,y,z,x,y-4,z,57)
        y = y-4