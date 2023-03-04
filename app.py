marks = [
    [
        [6, 8, 8, 9, 10],
        [9, 9, 9, 9, 9],
        [7, 7, 7, 7, 8],

    ],
    [
        [9, 8, 8, 8, 9],
        [9, 5, 6, 2, 9],
        [1, 7, 7, 7, 6],
    ],
]

for gi, group in enumerate(marks, start=1):
    print(f"group {gi}")
    print("------------------------")
    print(f"{'lesson:':11}", end="")
    for li, _ in enumerate(group[0]):
        print(f"{li+1:<3}", end="")
    print("\n")
    for si, student in enumerate(group, start=1):
        print(f"{'student '+str(si):<11}", end="")
        for mark in student:
            print(f"{mark:<3}", end="")
        print()
    print()
