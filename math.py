# coding=gbk

# class Dog():
#     '''一次模拟小狗的简单尝试'''
#     def __init__(self,name,age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#     def sit(self):
#         # 模拟小狗被命令时蹲下
#         print(self.name.title() + 'is now sitting') #self.name.title()：将名字的首字母替换成大写
#
#     def roll_over(self):
#         # 模拟小狗被命令时打滚
#         print(self.name.title() + 'rolled over')
#
#
# my_dog = Dog('nacee',6)
#
# print("My Dog's name " + my_dog.name.title() + '.')
# print("My Dog is " + str(my_dog.age)  + 'years old')
# my_dog.sit()
# my_dog.roll_over()

import os, shutil
dirA='D:\My Documents\Desktop\olderA'
dirB='D:\My Documents\Desktop\olderB'
def cptxt(src, dst):
  for i in os.listdir(src):
    filepath = src + os.sep + i
    if os.path.isdir(filepath):
      cptxt(filepath, dst)
    elif i.endswith('.txt'):
      print('copy', filepath, 'to', dst)
      shutil.copy(filepath, dst)
if __name__ == '__main__':
    cptxt(dirA, dirB)

