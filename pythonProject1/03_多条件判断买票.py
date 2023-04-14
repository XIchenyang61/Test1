# # if elif else 多条件判断语句的使用
#
# print("欢迎来到黑马动物园，入园前请先购票。")
#
# height = int(input("请输入您的身高（cm）："))
# vip_level = int(input("请输入您的VIP等级（1-5）："))
# day = int(input("请告诉我今天是几号："))
#
# if height < 120:
#     print("您的身高小于120cm，可以免费。")
# elif vip_level > 3:
#     print("您的VIP等级大于3，可以免费。")
# elif day == 1:
#     print("今天是1号免费日，可以免费。")
# else:
#     print("不好意思，您的条件不满足，需要购票10元。")

# 优化购票程序

print("欢迎来到黑马动物园，入园前请先购票。")

if int(input("请输入您的身高（cm）：")) < 120:
    print("您的身高小于120cm，可以免费。")
elif int(input("请输入您的VIP等级（1-5）：")) > 3:
    print("您的VIP等级大于3，可以免费。")
elif int(input("请告诉我今天是几号：")) == 1:
    print("今天是1号免费日，可以免费。")
else:
    print("不好意思，您的条件不满足，需要购票10元。")
