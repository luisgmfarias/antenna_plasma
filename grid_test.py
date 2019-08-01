import meep as mp
import matplotlib.pyplot as plt
import antenna

'''

@authors: Luís Farias and Ph.D.Cassio Amador

UTFPR/CP 2019

'''

#GERAR FONTE DE DENTRO DA ANTENA
#FAZER GRAFICO DE CAMPO ELETRICO DENTRO DE PONTO NA CELULA

#Aqui estamos criando e definindo as proporções do grid da simulação
lx=30
ly=30
x = lx/2
y = ly/2
cell = mp.Vector3(lx,ly,0)

#Definindo a camada PML e seu tamanho
pml_layers = [mp.PML(1.0)]

#Resolução
resolution = 45

#Criando mirroring para paralelização
symmetries = [mp.Mirror(mp.Y, phase=+1)]

fcen = 0.5
df = 0.4
src_cmpt = mp.Ez
sources = [mp.Source(src=mp.GaussianSource(fcen,fwidth=df),
                    center=mp.Vector3(-x + (5/2),0,0),
                    component=src_cmpt)]

sim = mp.Simulation(cell_size=cell,
                    resolution=resolution,
                    geometry=antenna.criar_antena(5, .5, 50, x, y),
                    sources=sources,
                    symmetries=symmetries,
                    boundary_layers=pml_layers)


def get_slice(sim):    
    plt.imshow(sim.get_array(component=mp.Ez),interpolation="spline36")
    plt.draw()
    plt.pause(0.05)

sim.run(mp.at_every(0.6, get_slice), until=100)
sim.run(mp.at_every(0.6, get_slice), until=100)
#sim.run(until=100)

eps_data = sim.get_array(component=mp.Dielectric)


plt.figure()
plt.imshow(eps_data.transpose(), interpolation='spline36', cmap='binary')
plt.show()