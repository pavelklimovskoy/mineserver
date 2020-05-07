import mcpi.minecraft as minecraft
import mcpi.block as block
import minecraftstuff as minecraftstuff
import math
import datetime
import time

def GetPoint(cx,cy,r,angle):
    x = cx + r * math.sin(math.radians(angle))
    y = cy + r * math.cos(math.radians(angle))
    x = int(round(x,0))
    y = int(round(y,0))
    return x,y

def UpdateTime(hour,min,sec):
    angleMin = 6*min
    mx, my = GetPoint(cx,cy,r,angleMin)
    mcdrawind.drawLine(cx, cy, cz,
                       mx,my , cz,
                       block.WOOL.id, 12)

    angleH = 30 * hour
    hx, hy = GetPoint(cx, cy, r, angleH)
    mcdrawind.drawLine(cx, cy, cz - 1,
                       hx, hy, cz - 1,
                       block.WOOL.id, 6)

    angleS = 6 * sec
    sx, sy = GetPoint(cx, cy, r, angleS)
    mcdrawind.drawLine(cx, cy, cz - 2,
                       sx, sy, cz - 2,
                       block.WOOL.id, 1)

    time.sleep(1)

    mcdrawind.drawLine(cx, cy, cz,
                       mx, my, cz,
                       block.AIR, 1)

    mcdrawind.drawLine(cx, cy, cz - 1,
                       mx, my, cz - 1,
                       block.AIR, 1)

    mcdrawind.drawLine(cx, cy, cz - 2,
                       sx, sy, cz -2,
                       block.AIR, 1)

cx = 114
cy = 95
cz = 201
r = 40

mc = minecraft.Minecraft.create('beer.truepunks.club', 4711)
mcdrawind = minecraftstuff.MinecraftDrawing(mc)

mcdrawind.drawCircle(cx, cy, cz, r,  block.WOOL.id, 14)
mcdrawind.drawSphere(cx, cy, cz, 4, block.WOOL.id, 16)
while True:
    hour = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    sec = datetime.datetime.now().second
    if(hour >= 12 ):
        hour -= 12

    # print(str(hour)+':'+str(min)+':'+str(sec))
    UpdateTime(hour,min,sec)


