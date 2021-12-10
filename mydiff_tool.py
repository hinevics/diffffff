import sys
# from config import DEFAULT_PATH
# ! Хочу решить тут задачу на реализацию diff app
# TODO: 
# * алгоритмы, сложность
# * какие алгоритмы используются для реализации diff
import difflib

file1 = ['AA', 'ddd', 'dasdas', 'sds']
file2 = ['AAa', 'ddd', 'dwdw']

delta = difflib.unified_diff(file1, file2)
# print(delta)
sys.stdout.writelines(delta)
