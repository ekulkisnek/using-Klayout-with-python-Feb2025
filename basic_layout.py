import pya

def create_basic_layout():
    """
    Demonstrates basic layout creation and manipulation using KLayout's Python API.
    Creates a simple layout with a single cell containing basic geometric shapes.
    """
    # Create a new layout
    layout = pya.Layout()
    
    # Define the database unit (1nm in this case)
    layout.dbu = 0.001
    
    # Create a new cell named "Basic"
    basic_cell = layout.create_cell("Basic")
    
    # Create a layer (layer 1, datatype 0)
    layer1 = layout.layer(1, 0)
    
    # Create some basic shapes
    # Rectangle: 1µm x 2µm
    basic_cell.shapes(layer1).insert(pya.Box(0, 0, 1000, 2000))
    
    # Create a polygon (triangle)
    points = [
        pya.Point(0, 0),
        pya.Point(1000, 0),
        pya.Point(500, 1000)
    ]
    basic_cell.shapes(layer1).insert(pya.Polygon(points))
    
    # Add a path
    path_points = [
        pya.Point(0, 3000),
        pya.Point(1000, 3000),
        pya.Point(1000, 4000)
    ]
    path = pya.Path(path_points, 100)  # 100nm width
    basic_cell.shapes(layer1).insert(path)
    
    # Save the layout
    layout.write("basic_layout.gds")

def main():
    print("Creating basic layout...")
    create_basic_layout()
    print("Layout saved as 'basic_layout.gds'")

if __name__ == "__main__":
    main()
