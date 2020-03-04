# coding: utf-8
from ftplib import FTP

def ftpconnect(host,port,username, password):
    ftp = FTP()
    ftp.connect(host, port)         
    ftp.login(username, password)  
    return ftp


def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR '+ remotepath , fp, bufsize)    #上传文件
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":
    ftp = ftpconnect("192.168.254.129",21, "uftp", "root")

    uploadfile(ftp, "192.168.254.131", "Z:\网络攻防\于晗\password2.txt")
    ftp.quit()
