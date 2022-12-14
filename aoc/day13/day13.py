import json
from functools import cmp_to_key

def main():
    count, index, total, packets = 0,0,0,[]

    with open("day13\\input.txt") as f:
        for line in f:
            match count:
                case 0:
                    left = json.loads(line.strip())
                    packets.append(left)
                    count +=1
                case 1: 
                    index += 1
                    right = json.loads(line.strip())
                    count +=1
                    packets.append(right)
                    result = modCompare(left,right)
                    if result == 1:
                        total += index
                case 2:
                    count = 0
    packets.append([6])
    packets.append([2])
    packets.sort(key=cmp_to_key(modCompare), reverse=True)
    i1,i2 = 0, 0
    for x in range(len(packets)):
        try:
            if packets[x][0] == 2 and len(packets[x]) == 1:
                i1 = x + 1
            elif packets[x][0] == 6 and len(packets[x]) == 1:
                i2 = x + 1
        except IndexError:
            pass
    print('Part 1: ' + str(total))
    print('Part 2: ' + str(i1 * i2))
    

def modCompare(left,right):
    result = compare(left,right)
    if result is None or result is True:
        return 1
    else:
        return -1

def compare(left, right):
    current = None
    try:
        if len(left) == 0 and len(right) != 0:
                return True
        for x in range(len(left)):
            if isinstance(left[x], int) and isinstance(right[x], int):
                if left[x] < right[x]:
                    return True
                elif left[x] > right[x]: 
                    return False
            elif isinstance(left[x], list) and isinstance(right[x], list):
                current = compare(left[x],right[x])
                if current is not None:
                    return current
            else:
                if isinstance(left[x], int):
                    l = [left[x]]
                    r = right[x]
                elif isinstance(right[x], int):
                    r = [right[x]]
                    l = left[x] 
                current = compare(l,r)
                if current is not None:
                    return current                 
    except IndexError:
        return False


main()