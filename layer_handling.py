import pya

def demonstrate_layer_operations():
    """
    Demonstrates various layer operations including:
    - Layer creation
    - Layer manipulation
    - Layer properties
    """
    # Create a new layout
    layout = pya.Layout()
    layout.dbu = 0.001
    
    # Create a main cell
    main_cell = layout.create_cell("LayerDemo")
    
    # Create multiple layers with different purposes
    metal1 = layout.layer(1, 0, "Metal1")  # Metal 1 layer
    metal2 = layout.layer(2, 0, "Metal2")  # Metal 2 layer
    via = layout.layer(3, 0, "Via")        # Via layer
    
    # Create shapes on Metal1
    main_cell.shapes(metal1).insert(pya.Box(0, 0, 2000, 2000))
    
    # Create shapes on Metal2
    main_cell.shapes(metal2).insert(pya.Box(500, 500, 1500, 1500))
    
    # Create via connections
    via_size = 200
    for x in range(750, 1251, 500):
        for y in range(750, 1251, 500):
            main_cell.shapes(via).insert(
                pya.Box(x - via_size//2, y - via_size//2,
                       x + via_size//2, y + via_size//2)
            )
    
    # Demonstrate layer info retrieval
    for li in layout.layer_indices():
        info = layout.get_info(li)
        print(f"Layer {info.layer}/{info.datatype}: {info.name}")
    
    # Save the layout
    layout.write("layer_handling.gds")

def main():
    print("Demonstrating layer operations...")
    demonstrate_layer_operations()
    print("Layout saved as 'layer_handling.gds'")

if __name__ == "__main__":
    main()
