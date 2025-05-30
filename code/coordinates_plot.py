import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.colors as mcolors

# Set the style for better aesthetics
plt.style.use('dark_background')

# Read the coordinates data
df = pd.read_csv('../coordinates.csv')

# Create custom colormaps
colors_eq = ['#FF9999', '#FF3366', '#CC0033']  # Red theme for equatorial
colors_gal = ['#99FF99', '#33FF66', '#00CC33']  # Green theme for galactic
colors_ecl = ['#9999FF', '#3366FF', '#0033CC']  # Blue theme for ecliptic

cmap_eq = LinearSegmentedColormap.from_list('custom_eq', colors_eq)
cmap_gal = LinearSegmentedColormap.from_list('custom_gal', colors_gal)
cmap_ecl = LinearSegmentedColormap.from_list('custom_ecl', colors_ecl)

# Create figure with three subplots
fig = plt.figure(figsize=(20, 24), facecolor='black')
fig.suptitle('Astronomical Coordinate Systems\nMollweide Projection', 
             fontsize=20, color='white', y=0.95, fontweight='bold')

# Set the spacing between subplots
plt.subplots_adjust(hspace=0.3)

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

# Create scatter plot with density-based coloring
density = np.ones(len(ra_rad))  # For color gradient
scatter1 = ax1.scatter(ra_rad, dec_rad, c=density, 
                      cmap=cmap_eq, alpha=0.7, s=30,
                      edgecolor='white', linewidth=0.5)

# Customize grid and labels
ax1.grid(color='gray', alpha=0.3, linestyle='-')
ax1.set_title('Equatorial Coordinates\nRight Ascension & Declination', 
              fontsize=16, color='white', pad=20)

# Add custom longitude labels (RA)
lon_labels = ['14h', '16h', '18h', '20h', '22h', '0h', '2h', '4h', '6h', '8h', '10h']
ax1.set_xticklabels(lon_labels, color='white')

# 2. Galactic coordinates plot
ax2 = plt.subplot(3, 1, 2, projection='mollweide')
gal_l_rad, gal_b_rad = prepare_for_mollweide(df['Galactic_l'], df['Galactic_b'])

# Create scatter plot with density-based coloring
density = np.ones(len(gal_l_rad))  # For color gradient
scatter2 = ax2.scatter(gal_l_rad, gal_b_rad, c=density,
                      cmap=cmap_gal, alpha=0.7, s=30,
                      edgecolor='white', linewidth=0.5)

# Customize grid and labels
ax2.grid(color='gray', alpha=0.3, linestyle='-')
ax2.set_title('Galactic Coordinates\nLongitude & Latitude', 
              fontsize=16, color='white', pad=20)

# Add custom longitude labels
lon_labels = ['150°', '120°', '90°', '60°', '30°', '0°', '-30°', '-60°', '-90°', '-120°', '-150°']
ax2.set_xticklabels(lon_labels, color='white')

# 3. Ecliptic coordinates plot
ax3 = plt.subplot(3, 1, 3, projection='mollweide')
ecl_lon_rad, ecl_lat_rad = prepare_for_mollweide(df['Ecliptic_lon'], df['Ecliptic_lat'])

# Create scatter plot with density-based coloring
density = np.ones(len(ecl_lon_rad))  # For color gradient
scatter3 = ax3.scatter(ecl_lon_rad, ecl_lat_rad, c=density,
                      cmap=cmap_ecl, alpha=0.7, s=30,
                      edgecolor='white', linewidth=0.5)

# Customize grid and labels
ax3.grid(color='gray', alpha=0.3, linestyle='-')
ax3.set_title('Ecliptic Coordinates\nLongitude & Latitude', 
              fontsize=16, color='white', pad=20)

# Add custom longitude labels
lon_labels = ['150°', '120°', '90°', '60°', '30°', '0°', '-30°', '-60°', '-90°', '-120°', '-150°']
ax3.set_xticklabels(lon_labels, color='white')

# Set y-axis labels color for all plots
for ax in [ax1, ax2, ax3]:
    ax.tick_params(colors='white')

# Add a text box with information
plt.figtext(0.02, 0.02, 
            'Generated using Python & Astropy\n500 Random Coordinates',
            color='gray', fontsize=10)

# Adjust layout and save
plt.tight_layout()
plt.savefig('../plot/coordinate_systems_mollweide.png', dpi=300, bbox_inches='tight')
print("Plots saved as coordinate_systems_mollweide.png in the plot directory")
