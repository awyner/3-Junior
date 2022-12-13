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
                    if compare(left,right):
                        total += index
                        #print(total,index)
                    # print(left, right)
                    #print(index, compare(left,right))
                case 2:
                    count = 0
    print(total)


def compare(left, right):
    current = True
    try:
        for x in range(len(left)):
            if isinstance(left[x], int) and isinstance(right[x], int):
                return left[x] < right[x]:
            elif isinstance(left[x], list) and isinstance(right[x], list):
                current = compare(left[x],right[x])
            else:
                if isinstance(left[x], int):
                    l = [left[x]]
                    r = right[x]
                else:
                    r = [right[x]]
                    l = left[x] 
                current = compare(l,r)
            if not current:
                return current
        return current                     
    except IndexError:
        return False

main()