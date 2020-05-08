from mcpi.minecraft import Minecraft
import time

#mc=Minecraft.create()
mc=Minecraft.create("47.100.46.95",4782)

entityId= mc.getPlayerEntityId("wzy")
pos=mc.entity.getTilePos(entityId)

stayed_time=0
while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.entity.getTilePos(entityId)
 #   mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("way x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x==-30 and pos.z==-40 and pos.y==-6:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.entity.setTilePos(-29,9,-45)
            stayed_time=0
    else:
        stayed_time=0
