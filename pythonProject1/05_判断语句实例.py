# 定义一个数字（1~10，随机产生），通过三次判断来猜出数字

# 1.构建一个随机的数字变量
import random
num = random.randint(1, 10)

guess_num = int(input("请输入你猜的数字："))

# 2.通过if语句进行数字的猜测
if guess_num == num:
    print("恭喜你，第一次就猜对了！")
else:
    if guess_num > num:
        print("不好意思，猜大了！")
    else:
        print("不好意思，猜小了！")
    guess_num = int(input("再次请输入你猜的数字："))

    if guess_num == num:
        print("恭喜你，第二次猜对了！")
    else:
        if guess_num > num:
            print("不好意思，猜大了！")
        else:
            print("不好意思，猜小了！")
        guess_num = int(input("第三次输入你猜的数字："))

        if guess_num == num:
            print("恭喜你，第三次猜对了！")
        else:
            print("不好意思，三次机会用完了，没有猜中！")
