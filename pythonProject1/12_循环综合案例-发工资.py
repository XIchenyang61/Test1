# 某公司，账户余额有1w元，给20名员工发工资

money = 10000       # 定义账户余额变量

# for循环对20位员工发工资
for num in range(1, 21):
    import random
    score = random.randint(1, 10)
    # 判断绩效是否小于5
    if score < 5:
        print(f"员工{num}，绩效分{score},低于5，不发工资，下一位。")
        continue        # continue跳过发放，即绩效低于5的，不进行下面的语句
    # 判断账户余额是否足够
    if money >= 1000:
        money -= 1000
        print(f"向员工{num}发放工资1000元，账户余额还剩余{money}")
    else:
        print(f"公司当前余额{money}元，余额不足以发工资，下个月再来。")
        break       # break结束发放，余额不足，跳出整个for循环
