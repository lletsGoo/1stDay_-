from unrar import rarfile

rarpath='D:\大四\大四下\网络攻防\于晗\第一天-生成字典压缩包爆破\password.rar'
pwdspath='D:\大四\大四下\网络攻防\于晗\第一天-生成字典压缩包爆破\password.txt'

pwds=open(pwdspath,'r')
rf = rarfile.RarFile(rarpath,'r')

print("开始爆破")
while not True:
    for line in pwds.readlines():
        pwd = line.strip('\n')
        try:
            rf.extractall(pwd=pwd)
            print("压缩包的密码是" + pwd)
        except:
            pass

