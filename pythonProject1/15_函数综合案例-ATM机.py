# 定义全局变量money
money = 5000000
# 要求客户输入姓名
name = input("请输入您的姓名：")
# 定义主菜单函数
def menu():
    print("----------------主菜单----------------\n"
          f"{name}，您好，欢迎使用ATM机。请选择操作:\n"
          "查询\t[输入1]\n"
          "存款\t[输入2]\n"
          "取款\t[输入3]\n"
          "退出\t[输入4]\n")
    return input("请输入您的选择：")
# 定义查询函数
def query(show_header):
    if show_header:
        print("----------------查询----------------")
    print(f"{name}，您好，您的余额剩余：{money}元")
# 定义存款函数
def save_money(num):
    global money
    money += num
    print("----------------存款----------------")
    print(f"{name}，您好，您存款{num}元成功")
    query(False)        # 调用query函数查询余额
# 定义取款函数
def get_money(num):
    global money
    money -= num
    print("----------------取款----------------")
    print(f"{name}，您好，您取款{num}元成功")
    query(False)        # 调用query函数查询余额

while True:
    keyboard_input = menu()
    if keyboard_input == "1":
        query(True)
        continue        # 通过continue 继续下一次循环，继续进入主菜单
    elif keyboard_input == "2":
        num = int(input("您想要存入多少钱？请输入："))
        save_money(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取入多少钱？请输入："))
        get_money(num)
        continue
    else:
        print("退出ATM机")
        break       # 通过break退出循环
