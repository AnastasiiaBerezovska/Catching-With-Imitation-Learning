import h5py
import matplotlib.pyplot as plt

# Load HDF5 file
file_path = 'robosuite/robosuite/scripts/DemonstrationsApril15/1713201006_866631/tested_run.hdf5'
with h5py.File(file_path, 'r') as hdf_file:
    # Assuming the trajectories are stored under a dataset named 'trajectories'
    trajectories = hdf_file['trajectories'][:]
    
    # Visualize trajectories (example using matplotlib)
    plt.figure()
    for trajectory in trajectories:
        plt.plot(trajectory[:, 0], trajectory[:, 1])  # Assuming 2D trajectories, adjust indexing as needed
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Trajectories Visualization')
    plt.show()
