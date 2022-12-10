def main():
    with open("day10\\input.txt") as f:
        register = 1
        cycle = 0
        strength = 0
        interest = 20
        for line in f:
            line = line.strip().split()
            match line[0]:
                case 'noop':
                    cycle +=1
                    pos = cycle% 40-1
                    if pos == register or pos == register-1 or pos == register+1:
                        print('#', end = '')
                    else:
                        print('.', end='')
                    if cycle % 40 == 0:
                        print()
                    if cycle == interest:
                        strength += (interest*register)
                        interest += 40
                case 'addx':
                    for x in range(2):
                        cycle+=1
                        pos = cycle% 40-1
                        if pos == register or pos == register-1 or pos == register+1:
                            print('#', end = '')
                        else:
                            print('.', end='')
                        if cycle % 40 == 0:
                            print()
                        if cycle == interest:
                            strength += (interest*register)
                            interest += 40
                    register+=int(line[1])
    print(register, cycle, strength)

main()