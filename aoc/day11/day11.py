class Monkey():
    def __init__(self, items, op, test, yes, no):
        self.items = items  # List of starting items
        self.test = test    # Divisible by test
        self.yes = yes      # Target monkey if yes
        self.no = no        # Target monkey if no
        self.op = op        # Operation 
        self.inspected = 0

    def runTest(self, item): 
        return (item % self.test) == 0
    
    def operation(self,item):
        old = item
        old = eval(self.op)
        return old % (13*3*7*2*19*5*11*17)
    
    def addItem(self, item):
        self.items.append(item)
    
    def pop(self):
        item = self.items[0]
        self.items.pop(0)
        return item

    
def main():
    numMonkes = 8
    m0 = Monkey([89, 73, 66, 57, 64, 80],'old * 3',13,6,2)
    m1 = Monkey([83, 78, 81, 55, 81, 59, 69],'old + 1',3,7,4)
    m2 = Monkey([76, 91, 58, 85],'old * 13',7,1,4)
    m3 = Monkey([71, 72, 74, 76, 68],'old * old',2,6,0)
    m4 = Monkey([98, 85, 84],'old + 7',19,5,7)
    m5 = Monkey([78],'old + 8',5,3,0)
    m6 = Monkey([86, 70, 60, 88, 88, 78, 74, 83],'old + 4',11,1,2)
    m7 = Monkey([81,58],'old + 5',17,3,5)
    monks = [m0,m1,m2,m3,m4,m5,m6,m7]
    for round in range(10000):
        for monke in monks:
            while len(monke.items) > 0:
                item = monke.pop()
                item = monke.operation(item)
                result = monke.runTest(item)
                if result:
                    monks[monke.yes].addItem(item)
                else:
                    monks[monke.no].addItem(item)
                monke.inspected += 1
    numInspected = []
    for monke in monks:
        numInspected.append(monke.inspected)
    numInspected.sort(reverse=True)
    monkeBusiness = numInspected[0] * numInspected[1]
    print(monkeBusiness)
main()