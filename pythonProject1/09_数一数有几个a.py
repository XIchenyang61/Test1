# 遍历字符串，统计有多少个英文字母

name = "itheima is a brand of itcast"
i = input("请输入要统计的字母：")
count = 0
for x in name:
    if x == i:
        count += 1
print(f"被统计的字符串中有多少个字母a：{count}个")
