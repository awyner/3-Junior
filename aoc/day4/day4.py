def main():
    with open("day4\\input.txt") as f:
        count = 0
        for line in f:
            range1 = []
            range2 = []

            line = line.strip().split(",")
            pair1, pair2 = line[0].split("-"), line[1].split("-")
            for x in range(int(pair1[0]), int(pair1[1])+1):
                range1.append(x)
            for x in range(int(pair2[0]), int(pair2[1])+1):
                range2.append(x)
            
            for x in range1:
                # print(range1)
                # print(range2)
                if x in range2:
                    count += 1
                    break
        print(count)


main()