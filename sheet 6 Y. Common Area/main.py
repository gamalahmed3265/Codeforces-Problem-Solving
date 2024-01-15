def find_common_area(rectangles):
    common_x1 = max(rect[0] for rect in rectangles)
    common_y1 = max(rect[1] for rect in rectangles)
    common_x2 = min(rect[2] for rect in rectangles)
    common_y2 = min(rect[3] for rect in rectangles)

    if common_x1 < common_x2 and common_y1 < common_y2:
        return (common_x2 - common_x1) * (common_y2 - common_y1)
    else:
        return 0

def main():
    T = int(input().strip())

    for case in range(1, T + 1):
        N = int(input().strip())
        rectangles = []

        for _ in range(N):
            x1, y1, x2, y2 = map(int, input().split())
            rectangles.append((x1, y1, x2, y2))

        result = find_common_area(rectangles)
        print("Case #{}: {}".format(case, result))

if __name__ == "__main__":
    main()
