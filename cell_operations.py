import pya

def demonstrate_cell_operations():
    """
    Shows various cell operations including:
    - Cell creation
    - Cell instantiation
    - Cell transformation
    - Hierarchy manipulation
    """
    # Create a new layout
    layout = pya.Layout()
    layout.dbu = 0.001  # 1nm database unit
    
    # Create a basic subcell with a rectangle
    sub_cell = layout.create_cell("SubCell")
    layer1 = layout.layer(1, 0)
    sub_cell.shapes(layer1).insert(pya.Box(0, 0, 1000, 1000))
    
    # Create a main cell
    main_cell = layout.create_cell("MainCell")
    
    # Create multiple instances of the subcell with different transformations
    
    # 1. Basic instance
    main_cell.insert(pya.CellInstArray(
        sub_cell.cell_index(),
        pya.Trans(pya.Point(0, 0))
    ))
    
    # 2. Rotated instance (45 degrees)
    main_cell.insert(pya.CellInstArray(
        sub_cell.cell_index(),
        pya.Trans(45, True, pya.Point(2000, 0))
    ))
    
    # 3. Array of instances (2x2)
    main_cell.insert(pya.CellInstArray(
        sub_cell.cell_index(),
        pya.Trans(pya.Point(0, 2000)),
        pya.Vector(1500, 0),  # X step
        pya.Vector(0, 1500),  # Y step
        2, 2  # nx, ny repetitions
    ))
    
    # Save the layout
    layout.write("cell_operations.gds")

def main():
    print("Demonstrating cell operations...")
    demonstrate_cell_operations()
    print("Layout saved as 'cell_operations.gds'")

if __name__ == "__main__":
    main()
