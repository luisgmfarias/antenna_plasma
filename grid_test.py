import meep as mp
import math
import numpy as np
import matplotlib.pyplot as plt

'''

@authors: Luís Farias and Ph.D.Cassio Amador

UTFPR/CP 2019

'''

#def criar_antena(height = 12, radius = 5):
#PARAMETRIZAR VALORES DA ANTENA
#GERAR FONTE DE DENTRO DA ANTENA
#FAZER GRAFICO DE CAMPO ELETRICO DENTRO DE PONTO NA CELULA
#VARIAR O ANGULO DA ANTENA


lx=30
ly=30
cell = mp.Vector3(lx,ly,0)


x = lx/2
y = ly/2

vector = mp.Vector3(12,1,mp.inf)
vectorRot = vector.rotate(mp.Vector3(0,0,1),math.radians(30))
#vectorRot = mp.get_rotation_matrix(mp.Vector3(0,0,1),math.radians(45)) * vector

def criar_antena(tamx,tamy,angulo):  

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
               #mp.Cylinder(radius=tamy/2,
                #            height=tamx,
                 #           axis=mp.Vector3(np.cos(math.radians(angulo)),np.sin(math.radians(angulo)),0),
                  #          center=mp.Vector3(dx,dy),
                   #         material=mp.Medium(epsilon=12)),
               #mp.Cylinder(radius=tamy/2,
                #           height=tamx,
                 #          axis=mp.Vector3(np.cos(math.radians(-angulo)),np.sin(math.radians(-angulo)),0),
                  #         center=mp.Vector3(dx,-dy),
                   #        material=mp.Medium(epsilon=12))
                   ]

    return antenna

""" antenna = [mp.Block(mp.Vector3(10,1,mp.inf),
                     center=mp.Vector3(-10,-6),
                     material=mp.Medium(epsilon=12)),    
           mp.Cylinder(radius = .5 ,
                     height = 12 ,
                     axis=mp.Vector3(np.cos(math.radians(30)),np.sin(math.radians(30)),0),   
                     center=mp.Vector3(0,9),
                     material=mp.Medium(epsilon=12)),
           mp.Block(mp.Vector3(10,1,mp.inf),
                     center=mp.Vector3(-10,6),
                     material=mp.Medium(epsilon=12)), #metal
           mp.Cylinder(radius = .5,
                     height = 12,
                     axis=mp.Vector3(np.cos(math.radians(-30)),np.sin(math.radians(-30)),0),   
                     center=mp.Vector3(0,-9),
                     material=mp.Medium(epsilon=12))]
 """

pml_layers = [mp.PML(1.0)]

resolution = 20

symmetries = [mp.Mirror(mp.Y,phase=+1)]


fcen = 0.5
df = 0.4
src_cmpt = mp.Ez
sources = [mp.Source(src=mp.GaussianSource(fcen,fwidth=df),
                    center=mp.Vector3(-x + (5/2),0,0),
                    component=src_cmpt)]


sim = mp.Simulation(cell_size=cell,
                    resolution=resolution,
                    geometry=criar_antena(5,.5,50),
                    sources=sources,
                    symmetries=symmetries,
                    boundary_layers=pml_layers)


def get_slice(sim):    
    plt.imshow(sim.get_array(component=mp.Ez),interpolation="spline36")
    plt.draw()
    plt.pause(0.05)

sim.run(mp.at_every(0.6, get_slice), until=100)
#sim.run(until=100)

eps_data = sim.get_array(component=mp.Dielectric)

plt.figure()
plt.imshow(eps_data.transpose(), interpolation='spline36', cmap='binary')
plt.show()