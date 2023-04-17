# 判断序列中有多少个偶数

num = int(input("请输入范围："))
count = 0
for x in range(1, num):
    if x % 2 == 0:
        count += 1
print(f"1到{num}(不含{num})范围内，有{count}个偶数")
