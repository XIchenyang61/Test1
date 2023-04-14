# 猜猜心里数字

num = 5

if int(input("请猜猜我心里想的数字是：")) == num:
    print("恭喜你，第一次就猜对了！")
elif int(input("猜错了，再猜一次：")) == num:
    print("恭喜你，第二次猜对了！")
elif int(input("猜错了，再猜一次：")) == num:
    print("恭喜你，最后一次机会，猜对了！")
else:
    print(f"Sorry，全部猜错了，我想的是：{num}")
