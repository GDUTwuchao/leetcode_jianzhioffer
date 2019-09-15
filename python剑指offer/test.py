
def findMax():
    info = {}
    n = int(input())
    while n:
        inputs = input().split()
        a = inputs[0]
        b = int(inputs[1])
        if a in info:
            info[a] = info[a] + b
        else:
            info[a] = b
        n -= 1
    max = 0
    maxid = ''
    for name in info:
        if info[name] > max:
            maxid = name
            max = info[name]

    print("name is {}, socre is {}".format(maxid, max))


def printZhengfangxing():
    n, char = input().split()
    n = int(n)
    if n % 2 == 0:
        row = n // 2
    else:
        row = n // 2 + 1
    for i in range(0, n):
        print(char, end='')
    print('')

    for hang in range(2, row):
        print(char, end='')
        for j in range(0, n-2):
            print(' ', end='')
        print(char)
    for i in range(0, n):
        print(char, end='')


def sumJinzhi():
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    sum = a + b
    if sum == 0:
        print('0')
    result = []
    while sum:
        q = sum % c
        q = str(q)
        result.insert(0, q)
        sum = sum // c
    result = int(''.join(result))
    print(result)

# findMax()
# printZhengfangxing()

sumJinzhi()