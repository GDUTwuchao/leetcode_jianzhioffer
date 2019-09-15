
import time

def displaytime(func): #func为传入的主函数，当函数带有参数的时候下面的wrapper必须加*args，如果函数有返回值，必须接受然后返回。
    def wrapper(*args):
        start = time.time()

        result = func(*args) # 这里参数也要传进来

        end = time.time()
        all = end - start
        print("use time : {:.4}".format(all))
        return result #  返回函数的返回值
    return wrapper # 返回wrapper



def is_prime(num):
    if num == 2:
        return True
    if num <2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

@displaytime  #表示装饰器，为下面的函数添加附加功能不改变下面主函数的主用功能。
def count_num_prim(maxnum):
    count = 0
    for i in range(2,maxnum):
        if is_prime(i):
            count += 1
    return count

count = count_num_prim(20000)
print(count)