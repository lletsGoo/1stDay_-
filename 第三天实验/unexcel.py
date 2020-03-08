import msoffcrypto
from datetime import datetime


def extractFile(file,passwords):
    try:
        file.load_key(password=passwords)
        file.decrypt(open(r'C:\Users\yangyi\Desktop\网络攻防\网络攻防实践.xlsx', 'Wb'))
        print('[+] Found password '+passwords + '\n')
    except:
        pass




def main():
    file = msoffcrypto.OfficeFile(open(r'C:\Users\yangyi\Desktop\网络攻防实践.xlsx', 'rb'))
    passFile=open(r'C:\Users\yangyi\Desktop\网络攻防\password_new_chaifen\new\out_7.txt')
    for line in passFile.readlines():
        password=line.strip('\n')
        passwords=password.split( )
        #print(passwords)
        for i in range(1):	
            extractFile(file,passwords[i])


if __name__ == '__main__':
    print("开始。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    main()
    print("完成。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
