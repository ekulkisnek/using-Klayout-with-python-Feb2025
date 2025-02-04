import pya
import math

def demonstrate_shape_creation():
    """
    Shows various shape creation and manipulation techniques:
    - Basic shapes
    - Complex polygons
    - Paths and edges
    - Shape transformations
    """
    # Create a new layout
    layout = pya.Layout()
    layout.dbu = 0.001

    # Create a main cell
    main_cell = layout.create_cell("ShapeDemo")
    layer1 = layout.layer(1, 0)

    # 1. Create a complex polygon (star shape)
    points = []
    center = pya.Point(2000, 2000)
    outer_radius = 1000
    inner_radius = 400

    for i in range(10):
        angle = i * 36 * (math.pi / 180)  # Convert to radians
        radius = outer_radius if i % 2 == 0 else inner_radius
        x = center.x + int(radius * math.cos(angle))
        y = center.y + int(radius * math.sin(angle))
        points.append(pya.Point(x, y))

    star = pya.Polygon(points)
    main_cell.shapes(layer1).insert(star)

    # 2. Create a path
    path_points = [
        pya.Point(0, 0),
        pya.Point(1000, 1000),
        pya.Point(2000, 1000),
        pya.Point(3000, 0)
    ]

    # Create a path with width 200nm
    path = pya.Path(path_points, 200)
    # Convert path to polygon without arguments
    path_polygon = path.polygon()
    main_cell.shapes(layer1).insert(path_polygon)

    # 3. Create a donut shape using direct polygon creation
    outer_points = []
    inner_points = []
    num_points = 32
    outer_radius = 1000
    inner_radius = 600

    # Create points for outer and inner circles
    for i in range(num_points):
        angle = i * 2 * math.pi / num_points
        # Outer circle points
        x_outer = int(outer_radius * math.cos(angle))
        y_outer = int(outer_radius * math.sin(angle))
        outer_points.append(pya.Point(x_outer, y_outer))
        # Inner circle points (in reverse order)
        x_inner = int(inner_radius * math.cos(angle))
        y_inner = int(inner_radius * math.sin(angle))
        inner_points.insert(0, pya.Point(x_inner, y_inner))

    # Combine points to create donut
    donut_points = outer_points + inner_points
    donut = pya.Polygon(donut_points)

    # Move the donut to a different location
    trans = pya.Trans(pya.Point(5000, 2000))
    main_cell.shapes(layer1).insert(donut.transform(trans))

    # Save the layout
    layout.write("shape_creation.gds")

def main():
    print("Demonstrating shape creation...")
    demonstrate_shape_creation()
    print("Layout saved as 'shape_creation.gds'")

if __name__ == "__main__":
    main()