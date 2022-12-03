def main():
    total = 0
    count = 0
    with open("day3\\input.txt") as f:
        arrLine = ["","",""]
        for line in f:
            arrLine[count%3] = line.strip()

            """halflen = len(line)//2
            first = line[:halflen]
            last = line[halflen:]"""

            if (count + 1) % 3 == 0:
                for x in arrLine[0]:
                    if x in arrLine[1] and x in arrLine[2]:
                        common = x
                        if common.isupper():
                            total += ord(common) - 38
                        else:
                            total += ord(common) - 96
                        break
            count +=1
    print(total)

            
main()