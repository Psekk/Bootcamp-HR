if __name__ == '__main__':
    shape_by_side_count = ["Triangle", "quadrilateral", "pentagon", "hexagon", "heptagon", "octagon", "nonagon",
                           "decagon"]
    sides = int(input("Sides: "))
    print(shape_by_side_count[sides - 3] if len(shape_by_side_count) > sides - 3 else "Amount of sides is out of range.")
