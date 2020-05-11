from mcpi.minecraft import Minecraft
import time
import csv

mc =Minecraft.create('47.100.46.95',4782)
entityId= mc.getPlayerEntityId("gch")
pos=mc.entity.getTilePos(entityId)
stayed_time=0

with open('house.csv',"r", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows=[row for row in reader]
    for a in range(6):
        if rows[a]["name"] == "center":
            x = rows[a]["x"]
            print(x)
            y = rows[a]["y"]
            print(y)
            z = rows[a]["z"]
            print(z)
        if rows[a]["name"] == "gch":
            xx = rows[a]["x"]
            yy = rows[a]["y"]
            zz = rows[a]["z"]
    x = int(x) + int(xx)
    y = int(y) + int(yy)
    z = int(z) + int(zz)

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.entity.getTilePos(entityId)
 #   mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x==-30 and pos.z==-40 and pos.y==-6:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.entity.setTilePos(-29,9,-45)
            stayed_time=0
    else:
        stayed_time=0

mc.setBlocks(x, y, z, x + 10, y + 10, z + 10, 79)
mc.setBlocks(x + 1, y + 1, z + 1, x + 9, y + 9, z + 9, 0)
print("hello,today is 5.11")