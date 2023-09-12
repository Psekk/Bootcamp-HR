if __name__ == '__main__':
    shape_by_side_count = ["Triangle", "Quadrilateral", "Pentagon",
                           "Hexagon", "Heptagon", "Octagon",
                           "Nonagon", "Decagon"]  # -3 offset by index
    sides = int(input("Sides: "))
    print(shape_by_side_count[sides - 3])
