class daynames:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Wed')
e3 = daynames('Tue')
e4 = daynames('Thu')

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

thisval = e1
while thisval:
    print(thisval.dataval)
    thisval = thisval.nextval