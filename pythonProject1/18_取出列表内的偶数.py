my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2 = []
my_list3 = []


def list_while_func():
    index = 0
    while index < len(my_list1):
        element = my_list1[index]
        if element % 2 == 0:
            my_list2.append(element)
        index += 1
    print(f"通过while循环，从列表：{my_list1}中取出偶数，组成新列表：{my_list2}")


list_while_func()


def list_for_func():
    for element in my_list1:
        if element % 2 == 0:
            my_list3.append(element)
    print(f"通过for循环，从列表：{my_list1}中取出偶数，组成新列表：{my_list3}")


list_for_func()
