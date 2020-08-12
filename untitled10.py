from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
def plantTree(x,y,z):
    mc.setBlocks(x+1,y+5,z+1,x-1,y+3,z-1,41)
    mc.setBlocks(x,y,z,x,y+4,z,57)
for h in range(999):
    for i in range(999):
        plantTree(x+i,y,z+h)
   