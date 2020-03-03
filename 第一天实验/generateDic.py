import itertools as its
words="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"#如需要，可加入大写字母及其他符号
dic=open('pwd.txt','w')
for num in range(1,5):#度为8~10位数# # #
    keys=its.product(words,repeat=num)
    for key in keys:
        dic.write("".join(key) + "\n")

dic.close()
