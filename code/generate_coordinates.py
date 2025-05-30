import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u

def convert_coordinates(ra, dec):
    """
    Convert RA, Dec coordinates to Galactic and Ecliptic coordinates
    
    Parameters:
    ra (array): Right Ascension in degrees
    dec (array): Declination in degrees
    
    Returns:
    dict: Dictionary containing Galactic (l,b) and Ecliptic (lon,lat) coordinates
    """
    # Create SkyCoord object with the input coordinates in ICRS frame
    coords = SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='icrs')
    
    # Convert to Galactic coordinates
    galactic = coords.galactic
    
    # Convert to Ecliptic coordinates
    ecliptic = coords.barycentrictrueecliptic
    
    return {
        'gal_l': galactic.l.degree,
        'gal_b': galactic.b.degree,
        'ecl_lon': ecliptic.lon.degree,
        'ecl_lat': ecliptic.lat.degree
    }

# Set random seed for reproducibility
np.random.seed(42)

# Generate 500 random coordinates
n_points = 500

# Generate RA (0 to 360 degrees)
ra = np.random.uniform(0, 360, n_points)

# Generate Dec (-90 to +90 degrees)
dec = np.random.uniform(-90, 90, n_points)

# Convert coordinates to Galactic and Ecliptic
converted_coords = convert_coordinates(ra, dec)

# Create a DataFrame with all coordinate systems
df = pd.DataFrame({
    'RA': ra,
    'Dec': dec,
    'Galactic_l': converted_coords['gal_l'],
    'Galactic_b': converted_coords['gal_b'],
    'Ecliptic_lon': converted_coords['ecl_lon'],
    'Ecliptic_lat': converted_coords['ecl_lat']
})

# Save to CSV
df.to_csv('../coordinates.csv', index=False)
print("Coordinates saved to coordinates.csv with RA/Dec, Galactic, and Ecliptic coordinates")
