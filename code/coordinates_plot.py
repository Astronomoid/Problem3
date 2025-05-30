import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the coordinates data
df = pd.read_csv('../coordinates.csv')

# Create figure with three subplots
fig = plt.figure(figsize=(15, 15))

# Convert coordinates to radians for Mollweide projection
# Note: Matplotlib's Mollweide projection expects longitude in range [-π, π]
def prepare_for_mollweide(lon, lat):
    # Convert longitude to range [-180, 180]
    lon = np.where(lon > 180, lon - 360, lon)
    # Convert to radians
    lon_rad = np.radians(lon)
    lat_rad = np.radians(lat)
    return lon_rad, lat_rad

# 1. RA vs Dec plot (Equatorial coordinates)
ax1 = plt.subplot(3, 1, 1, projection='mollweide')
ra_rad, dec_rad = prepare_for_mollweide(df['RA'], df['Dec'])
scatter1 = ax1.scatter(ra_rad, dec_rad, alpha=0.6, s=10)
ax1.set_title('Equatorial Coordinates (Mollweide Projection)')
ax1.grid(True)

# 2. Galactic coordinates plot
ax2 = plt.subplot(3, 1, 2, projection='mollweide')
gal_l_rad, gal_b_rad = prepare_for_mollweide(df['Galactic_l'], df['Galactic_b'])
scatter2 = ax2.scatter(gal_l_rad, gal_b_rad, alpha=0.6, s=10)
ax2.set_title('Galactic Coordinates (Mollweide Projection)')
ax2.grid(True)

# 3. Ecliptic coordinates plot
ax3 = plt.subplot(3, 1, 3, projection='mollweide')
ecl_lon_rad, ecl_lat_rad = prepare_for_mollweide(df['Ecliptic_lon'], df['Ecliptic_lat'])
scatter3 = ax3.scatter(ecl_lon_rad, ecl_lat_rad, alpha=0.6, s=10)
ax3.set_title('Ecliptic Coordinates (Mollweide Projection)')
ax3.grid(True)

# Adjust layout and save
plt.tight_layout()
plt.savefig('../plot/coordinate_systems_mollweide.png', dpi=300, bbox_inches='tight')
print("Plots saved as coordinate_systems_mollweide.png in the plot directory")
