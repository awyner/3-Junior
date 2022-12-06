def main():
    with open("day6\\input.txt") as f:
        for line in f:
            line = line.strip()
            used = [None] * 14
            count = 0
            for x in range(len(line)):
                if line[x] not in used:
                    used[count] = line[x]
                    count += 1
                    if count == 14:
                        print(used, x+1)
                        break
                else:
                    print(used, line[x], count)
                    for i in range(len(used)):
                        if used[i-1] == line[x]:
                            print(used)
                            for j in range(i, 14):
                                used[j-i] = used[j]
                            for j in range(count+1, 14):
                                used[j] = None
                            used[count] = line[x]
                            count+=1
                            print(used, count)
                            print()
                            break
                        else:
                            count-=1
                            if x >= 1998:
                                pass

                    #used[0] = line[x]
                    
main()