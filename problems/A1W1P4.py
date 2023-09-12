widget = 75
gizmo = 112

if __name__ == '__main__':
    widget_count = int(input("Widgets: "))
    gizmo_count = int(input("Gizmos: "))
    print(f"The Total Weight of the Order: {widget_count * widget + gizmo_count * gizmo} grams")
