import meep as mp
import matplotlib.pyplot as plt
import antenna
import plasma
import numpy as np

'''

@authors: Luís Farias and Ph.D.Cassio Amador

UTFPR/CP 2019

'''

plot_animation = True
plot_slice = False
plot_eps = False
is_plasma = True

#criar bloco de altura do grid altura fixa
#largura da resoluão = 1/resolução
#posição x é variavel 

#Tempo total da simulação:
total_time=60

#Aqui estamos criando e definindo as proporções do grid da simulação
lx=30
ly=30
x = lx/2
y = ly/2
cell = mp.Vector3(lx,ly,0)

#Definindo a camada PML e seu tamanho
pml_layers = [mp.PML(1.0)]

#Resolução
resolution = 30

#Criando mirroring para paralelização
symmetries = [mp.Mirror(mp.Y, phase=+1)]

fcen = 0.5
df = 0.4
src_cmpt = mp.Ez
sources = [mp.Source(src=mp.GaussianSource(fcen,fwidth=df),
                    center=mp.Vector3(-x + (5/2),0,0),
                    component=src_cmpt)]

plasma_obj = plasma.create_plasma(10,30,30,30)
antenna_obj = antenna.create_antenna(5, .5, 50, 15, 15)

sim = mp.Simulation(cell_size=cell,
                    resolution=resolution,
                    geometry=antenna_obj + plasma_obj,
                    sources=sources,
                    symmetries=symmetries,
                    boundary_layers=pml_layers)

#Simulação da onda em animação

if plot_animation :

    def get_slice(sim):
        plt.imshow(sim.get_array(component=abs(mp.Ez)).transpose(),interpolation="spline36")
        plt.draw()
        plt.pause(0.5)



    sim.run(mp.at_every(10, get_slice), until=100)

if plot_slice : 

#Abaixo é gerado o gráfico da onda no ponto central do grid

    def gerar_grafico(Ez_point):
        plt.plot(Ez_point)
        plt.xlabel("Tempo")
        plt.ylabel("Amplitude")
        plt.show()

    Ez_point = np.zeros(int(total_time/0.05)+1)

    t=0

    y_point,x_point=int(100),int(100)

    def read_Ez(sim):
        global t
        Ez_point[t]=sim.get_array(component=mp.Ez)[y_point,x_point]
        t+=1

    sim.run(mp.at_every(0.05, read_Ez), until=total_time)

    if is_plasma:
        np.save("sem_plasma", Ez_point)
    else:
        np.save("com_plasma", Ez_point)
        
    gerar_grafico(Ez_point)

if plot_eps :
    sim.run(until=1)

    eps_data = sim.get_array(component=mp.Dielectric)

    plt.figure()
    plt.imshow(eps_data.transpose(), interpolation='spline36', cmap='binary')
    plt.show()
