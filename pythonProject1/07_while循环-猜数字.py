# 利用while循环实现猜数字

# 定义1-100的随机数
import random
num = random.randint(1, 100)
# count变量用于记录猜测次数
count = 0
# 设置一个布尔类型的变量，标记是否继续进行循环
flag = True
while flag:
    guess_num = int(input("输入你心里想的数字："))
    count += 1
    if guess_num == num:
        print("恭喜您，猜中了！")
        # 猜中后将布尔类型设置为False,是终止循环的标志
        flag = False
    else:
        if guess_num > num:
            print("不好意思，猜大了！")
        else:
            print("不好意思，猜小了！")

print(f"您共猜了{count}次")
