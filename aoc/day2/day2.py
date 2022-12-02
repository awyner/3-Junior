

def main():
    total = 0
    with open("input.txt") as f:
        """for line in f:
            line = line.split()
            if line[1] == "X":
                total += 1
            elif line[1] == "Y":
                total += 2
            elif line[1] == "Z":
                total += 3
            if line[0] == "A":
                if line[1] == "X":
                    total += 3
                if line[1] == "Y":
                    total += 6       
            elif line[0] == "B":
                if line[1] == "Y":
                    total += 3
                if line[1] == "Z":
                    total += 6  
            elif line[0] == "C":
                if line[1] == "X":
                    total += 6
                if line[1] == "Z":
                    total += 3      """
        for line in f:
            line = line.split()
            if line[1] == "Z":
                if line[0] == "A":
                    total += 8
                elif line[0] == "B":
                    total += 9
                elif line[0] == "C":
                    total += 7
            elif line[1] == "Y":
                if line[0] == "A":
                    total += 4
                elif line[0] == "B":
                    total += 5
                elif line[0] == "C":
                    total += 6        
            elif line[1] == "X":
                if line[0] == "A":
                    total += 3
                elif line[0] == "B":
                    total += 1
                elif line[0] == "C":
                    total += 2
    print(total)
main()