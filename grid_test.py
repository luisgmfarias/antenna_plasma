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

vector = mp.Vector3(12,1,mp.inf)
vectorRot = vector.rotate(mp.Vector3(0,0,1),math.radians(30))
#vectorRot = mp.get_rotation_matrix(mp.Vector3(0,0,1),math.radians(45)) * vector

def criar_antena(x,y,angulo):  

    px = np.cos(90-angulo)*y/2
    py = np.sin(90-angulo)*y/2
    cx = px + (x/2) * np.sin(90-angulo)
    cy = py + (x/2) * np.cos(90-angulo)


    antenna = [mp.Block(mp.Vector3(x,y,0),
                        center=mp.Vector3((-lx/2)+x/2,ly/4,0),
                        material=mp.Medium(epsilon=12)),
               mp.Block(mp.Vector3(x,y,0),
                        center=mp.Vector3((-lx/2)+x/2,-ly/4,0),
                        material=mp.Medium(epsilon=12)),
               mp.Cylinder(radius=(((y**2 * np.cos(angulo)**2) + y**2)/2),
                            height=x,
                            axis=mp.Vector3(np.cos(math.radians(angulo)),np.sin(math.radians(angulo)),0),
                            center=mp.Vector3(cx,cy),
                            material=mp.Medium(epsilon=12)),
               mp.Cylinder(radius=(((y**2 * np.cos(angulo)**2) + y**2)/2),
                            height=x,
                            axis=mp.Vector3(np.cos(math.radians(-angulo)),np.sin(math.radians(-angulo)),0),
                            center=mp.Vector3(cx,-cy),
                            material=mp.Medium(epsilon=12))]
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

resolution = 45

#symmetries = [mp.Mirror(mp.Y,phase=+1)]


fcen = 0.5
df = 0.4
src_cmpt = mp.Ez
sources = [mp.Source(src=mp.GaussianSource(fcen,fwidth=df),
                    center=mp.Vector3(1,1,0),
                    component=src_cmpt)]


sim = mp.Simulation(cell_size=cell,
                    resolution=resolution,
                    geometry=criar_antena(10,1,30),
                    boundary_layers=pml_layers)


#def get_slice(sim):    
#    plt.imshow(sim.get_array(component=mp.Ez),interpolation="spline36")
#    plt.draw()
#    plt.pause(0.05)

#sim.run(mp.at_every(0.6, get_slice), until=100)
sim.run(until=100)

eps_data = sim.get_array(component=mp.Dielectric)

plt.figure()
plt.imshow(eps_data.transpose(), interpolation='spline36', cmap='binary')
plt.show()

#tarefa fazer grid inclinado ou um x