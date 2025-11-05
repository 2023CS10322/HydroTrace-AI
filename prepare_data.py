import segyio
import numpy as np

# Install segyio first: pip install segyio

# Load SEG-Y file
with segyio.open('data/F3_seismic.segy', ignore_geometry=True) as f:
    seismic_3d = segyio.tools.cube(f)
    
# Extract one 2D slice (a single vertical cross-section)
seismic_slice = seismic_3d[:, :, 0]  # First slice in Z direction

# Normalize to 0-1 range (important for neural networks)
seismic_slice = (seismic_slice - seismic_slice.min()) / (seismic_slice.max() - seismic_slice.min())

# Add batch and channel dimensions (required by Keras)
seismic_data = np.expand_dims(np.expand_dims(seismic_slice, axis=0), axis=-1)

# Save as numpy file
np.save('data/your_seismic_slice.npy', seismic_data)

print(f"Seismic data shape: {seismic_data.shape}")
