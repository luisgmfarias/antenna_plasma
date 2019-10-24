import numpy as np
import h5py

data_to_write = np.linspace(0,1)

with h5py.File('epsilon.h5', 'w') as hf:
    hf.create_dataset("Epsilon",  data=data_to_write)