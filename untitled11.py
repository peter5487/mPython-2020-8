from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
for i in range(10):
    x,y,z = mc.player.getTilePos()
    x = x+i
    for j in range(10):
        r = random.randrange(0,16)
        z = z+1
        mc.getBlock(x,y,z,35,r)