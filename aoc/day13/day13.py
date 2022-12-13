import json

def main():
    count=0
    index = 0
    total = 0
    with open("day13\\input.txt") as f:
        for line in f:
            match count:
                case 0:
                    left = json.loads(line.strip())
                    count +=1
                case 1: 
                    index += 1
                    right = json.loads(line.strip())
                    count +=1
                    result = compare(left,right)
                    if result is None or result:
                        total += index
                        #print(total,index)
                    # print(left, right)
                    print(index, total, compare(left,right))
                case 2:
                    count = 0
    print(total)


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
        return current                     
    except IndexError:
        return False

main()