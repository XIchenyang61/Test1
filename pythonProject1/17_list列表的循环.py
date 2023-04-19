def list_while_func():
    """
    使用while循环遍历列表的函数
    :return: None
    """
    my_list = [10, 20, 30, 40, 50]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的元素是：{element}")
        index += 1


list_while_func()


def list_for_func():
    """
    使用for循环遍历列表的函数
    :return: None
    """
    my_list = [60, 70, 80, 90, 100]
    for element in my_list:
        print(f"列表的元素是：{element}")


list_for_func()
