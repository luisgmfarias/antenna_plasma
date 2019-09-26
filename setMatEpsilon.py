import numpy as np
import h5py

data_to_write = np.random.random(size=(100,20))

with h5py.File('epsilon.h5', 'w') as hf:
    hf.create_dataset("Epsilon",  data=data_to_write)