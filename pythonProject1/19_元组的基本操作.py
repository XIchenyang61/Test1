std_id = ('周杰伦', 11, ['football', 'music'])
age = std_id.index(11)
name = std_id[0]
print(f"学生的年龄下标为：{age}")
print(f"学生的姓名是：{name}")
del std_id[2][0]
std_id[2].append('coding')
print(f"修改后的元组为：{std_id}")
