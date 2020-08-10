from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.setTilePos()
mc.setBlock(pos,15)