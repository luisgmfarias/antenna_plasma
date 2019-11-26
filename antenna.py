import meep as mp
import math
import numpy as np

def create_antenna(tamx, tamy, angulo, x, y):  

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
                        material=mp.metal),
               mp.Block(mp.Vector3(tamx,tamy,0),
                        center=mp.Vector3(b1x,-b1y),
                        material=mp.metal),
               mp.Cylinder(radius=tamy/2,
                            height=tamx,
                            axis=mp.Vector3(np.cos(math.radians(angulo)),np.sin(math.radians(angulo)),0),
                            center=mp.Vector3(dx,dy),
                            material=mp.metal),
               mp.Cylinder(radius=tamy/2,
                           height=tamx,
                           axis=mp.Vector3(np.cos(math.radians(-angulo)),np.sin(math.radians(-angulo)),0),
                           center=mp.Vector3(dx,-dy),
                           material=mp.metal)]

    

    return antenna

if __name__ == "__main__":
    criar_antena(5, .5, 50, 15, 15)
    