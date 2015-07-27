#-*-coding:utf-8-*-

from pylib.pypath import Path

p=Path()# 初始化p，路径默认初始化为当前目录
p.change_path("./f1")# 更换路径

# 路径下的输出文件
print(" 当前路径为： "+p.get_path())
print(" 当前路径下的所有文件： "+str(p.get_all_files()))
print(" 当前路径下无扩展名的文件有： "+str(p.get_attrib_files([''],'f')))
print(" 当前路径下扩展名为'ap'的文件有： "+str(p.get_attrib_files(['ap'],'f')))
print(" 当前路径下扩展名为'bp'的文件有： "+str(p.get_attrib_files(['bp'],'f')))
print(" 当前路径下扩展名为'cp'的文件有： "+str(p.get_attrib_files(['cp'],'f')))
print(" 当前路径下扩展名为'dp'的文件有： "+str(p.get_attrib_files(['dp'],'f')))
print(" 当前路径下具有文件(file)属性的文件有： "+str(p.get_attrib_files(attrib='f')))
print(" 当前路径下具有目录(direction)属性的文件有： "+str(p.get_attrib_files(attrib='d')))
print(" 当前路径下具有隐藏文件(hidden file)属性的文件有： "+str(p.get_attrib_files(attrib='hf')))
print(" 当前路径下具有隐藏目录(hidden direction)属性的文件有： "+str(p.get_attrib_files(attrib='hd')))

# 路径转换
print(" 将路径转换到'./f1/f2' ")
p.change_path('./f1/f2')
print(" 当前路径为： "+p.get_path())

print(" 将路径转换到'./f1/f2/f4' ")
p.change_path('./f1/f2/f4')
print(" 当前路径为： "+p.get_path())

print(" 返回到上一步 ")
p.back()
print(" 当前路径为： "+p.get_path())

print(" 再次返回到上一步 ")
p.back()
print(" 当前路径为： "+p.get_path())

print(" 再次返回到上一步 ")
p.back()
print(" 当前路径为： "+p.get_path())

print(" 再次返回到上一步 ")
p.back()
print(" 当前路径为： "+p.get_path())

print('前进到下一步')
p.front()
print(" 当前路径为： "+p.get_path())

print('再次前进到下一步')
p.front()
print(" 当前路径为： "+p.get_path())

print('再次前进到下一步')
p.front()
print(" 当前路径为： "+p.get_path())

print('再次前进到下一步')
p.front()
print(" 当前路径为： "+p.get_path())
