import geopandas as gpd

def find_intersection():
    try:
        # Load the files
        illinois = gpd.read_file('illinois_boundary.geojson')
        cook_county = gpd.read_file('cook_county_boundary.geojson')
        # Ensure same CRS
        if illinois.crs != cook_county.crs:
            cook_county = cook_county.to_crs(illinois.crs)
        # Perform intersection
        intersection = gpd.overlay(illinois, cook_county, how='intersection')

        if not intersection.empty:
            print("Intersection geometry:")
            print(intersection.geometry)
            # Get coordinates

            if intersection.geometry.iloc[0].geom_type == 'Polygon':
                coords = list(intersection.geometry.iloc[0].exterior.coords)
            elif intersection.geometry.iloc[0].geom_type == 'MultiPolygon':
                coords = [list(poly.exterior.coords) for poly in intersection.geometry.iloc[0].geoms]

            print("\nCoordinates:")
            print(coords)
            print("\n\n INTERASECTION \n")
            print(intersection)

            # Save intersection to GeoJSON file
            intersection.to_file('cook_intersection_result.geojson', driver='GeoJSON')
            print("\nSaved intersection to 'cook_intersection_result.geojson'")

            return intersection
        else:
            print("No intersection found")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    find_intersection()
