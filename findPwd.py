# Python的标准库linecache模块非常适合这个任务
import linecache

# linecache读取并缓存文件中所有的文本，
# 若文件很大，而只读一行，则效率低下。
# 可显示使用循环, 注意enumerate从0开始计数，而line_number从1开始
def getline(the_file_path, line_number):
    if line_number < 1:
        return ''
    for cur_line_number, line in enumerate(open(the_file_path, 'rU')):
        if cur_line_number == line_number-1:
            return line
        return ''

data = input("输入要查找的编号: ")
the_line = linecache.getline('pwd.txt', int(data))
print("这一行的密码是：",the_line)