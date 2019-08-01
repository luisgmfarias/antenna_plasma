import meep as mp
import math
import numpy as np

def criar_antena(tamx, tamy, angulo, x, y):  

    b1x = -x + (tamx/2)
    b1y = y/7
    bfx = -x + tamx
    bfy = b1y - (tamy/2)
    ca = (tamx/2) * np.cos(math.radians(angulo))
    co = (tamx/2) * np.sin(math.radians(angulo))
    xx = (tamy/(2/np.sin(math.radians(angulo))))
    dx = ca - xx + bfx
    dy = co + b1y


    antenna = [mp.Block(mp.Vector3(tamx,tamy,0),
                        center=mp.Vector3(b1x,b1y),
                        material=mp.Medium(epsilon=12)),
               mp.Block(mp.Vector3(tamx,tamy,0),
                        center=mp.Vector3(b1x,-b1y),
                        material=mp.Medium(epsilon=12)),
               mp.Cylinder(radius=tamy/2,
                            height=tamx,
                            axis=mp.Vector3(np.cos(math.radians(angulo)),np.sin(math.radians(angulo)),0),
                            center=mp.Vector3(dx,dy),
                            material=mp.Medium(epsilon=12)),
               mp.Cylinder(radius=tamy/2,
                           height=tamx,
                           axis=mp.Vector3(np.cos(math.radians(-angulo)),np.sin(math.radians(-angulo)),0),
                           center=mp.Vector3(dx,-dy),
                           material=mp.Medium(epsilon=12))]

    return antenna