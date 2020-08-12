from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for j in range(3):
    for i in range(100):    
        mc.setBlock(x+i,y-1,z+i+j,57)