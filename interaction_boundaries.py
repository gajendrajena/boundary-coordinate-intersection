import geopandas as gpd

# Load the files
illinois = gpd.read_file('illinois_boundary.geojson')
lake_county = gpd.read_file('lake_county_boundary.geojson')

# Make sure they're in the same coordinate reference system (CRS)
if illinois.crs != lake_county.crs:
    lake_county = lake_county.to_crs(illinois.crs)

# Since Lake County is entirely within Illinois, the intersection is Lake County itself
intersection = lake_county.copy()

# If you want to verify with an actual intersection operation:
intersection = gpd.overlay(illinois, lake_county, how='intersection')

# Export the coordinates
if not intersection.empty:
    # For Polygon
    if intersection.geometry.iloc[0].geom_type == 'Polygon':
        coords = list(intersection.geometry.iloc[0].exterior.coords)
    # For MultiPolygon
    elif intersection.geometry.iloc[0].geom_type == 'MultiPolygon':
        coords = [list(poly.exterior.coords) for poly in intersection.geometry.iloc[0].geoms]

    print(coords)
