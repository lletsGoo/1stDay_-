from socket import *
import struct
import json

host = ''
port = 11444

s = socket(AF_INET, SOCK_STREAM)
#s.setsockopt(SOL_SOCKET, SO_REUSERADDR, 1)
s.bind((host, port))
s.listen(10)
buffer = 1024  # 缓冲区大小，这里好像因为windows的系统的原因，这个接收的缓冲区不能太大

conn, addr = s.accept()
# 先接收报头的长度
head_len = conn.recv(4)
head_len = struct.unpack('i', head_len)[0]  # 将报头长度解包出来
# 再接收报头
json_head = conn.recv(head_len).decode('utf-8')  # 拿到的是bytes类型的数据，要进行转码
head = json.loads(json_head)  # 拿到原本的报头
file_size = head['filesize']
with open(head['filename'], 'ab') as f:
    print(file_size)
    while file_size:
        if file_size >= buffer:  # 判断剩余文件的大小是否超过buffer
            content = conn.recv(buffer)
            f.write(content)
            file_size -= buffer
        else:
            content = conn.recv(file_size)
            f.write(content)
            file_size = 0
            break

print('Connected by ', addr)
data = conn.recv(1024)

while 1:
    command = input("Enter shell command or quit: ")
    conn.send(command.encode())
    if command == "quit": break
    data = conn.recv(1024)
    data = data.decode('gbk')
    print(data)
conn.close()