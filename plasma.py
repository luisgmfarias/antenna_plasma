import meep as mp
import math
import numpy as np

def create_plasma(max_eps, lx, ly, resolution):  

    tamx = 1/resolution
    tamy = ly
    var = int((lx/2)*resolution)

    plasma = []

    for i in range(var):
        bloco = mp.Block(mp.Vector3(tamx,tamy,0),
                        center=mp.Vector3(tamx*i,0),
                        material=mp.Medium(epsilon=1+(i*max_eps/var)))
        plasma.append(bloco)
    
    return plasma

if __name__ == "__main__":
    print(len(plasma(10,30,30,30)))


#parabola perfil de plasma
#parabola x2 ou exponencial ou tang hiperbolica
    