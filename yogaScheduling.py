classes = [
    (9, 10, "Yoga Beginner"),
    (10, 11, "Yoga Intermediate"),
    (9.5, 10.5, "Yoga Flow"),
    (11, 12, "Power Yoga"),
    (10, 11.5, "Yoga Stretch"),
    (12, 13, "Yoga Relax"),
]

def greedy_schedule(classes):
    sorted_classes = sorted(classes, key=lambda x: x[1])
    selected = []
    last_end = 0
    for start, end, name in sorted_classes:
        if start >= last_end:
            selected.append((start, end, name))
            last_end = end
    return selected

def divide_and_conquer_schedule(classes):
    if not classes:
        return []

    sorted_classes = sorted(classes, key=lambda x: x[0])
    rooms = []

    for start, end, name in sorted_classes:
        placed = False
        for room in rooms:
            if room[0][1] <= start:
                room.pop(0)
                room.append((start, end, name))
                placed = True
                break
        if not placed:
            rooms.append([(start, end, name)])
    return rooms

print("Greedy Schedule:")
for cls in greedy_schedule(classes):
    print(f"{cls[2]}: {cls[0]} - {cls[1]}")

print("\nDivide and Conquer Schedule:")
rooms = divide_and_conquer_schedule(classes)
for i, room in enumerate(rooms, 1):
    print(f"Room {i}:")
    for cls in room:
        print(f"  {cls[2]}: {cls[0]} - {cls[1]}")