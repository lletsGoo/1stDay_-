import PyPDF4
import sys

pdfReader = PyPDF4.PdfFileReader(open('D:\大四\大四下\网络攻防\于晗\第三天\文档2.pdf','rb'))
if pdfReader.isEncrypted:
    #开始破解密码
    print('尝试破解密码...')
    #获取密码字典
    File = open('D:\大四\大四下\网络攻防\于晗\pwd.txt')
    sfile = File.read()
    dic = sfile.split('\n')
    num = len(dic)
    for i in range(num):
        print('第 '+str(i) +' 次尝试...     ' + dic[i],end=' ')
        if pdfReader.decrypt(dic[i]):
            print('破解成功，密码是 ' + dic[i] + '...')
            #进入PDF
            print('PDF有 '+ str(pdfReader.numPages) + '页')
            print('内容摘要')
            pageObj = pdfReader.getPage(0)
            print(pageObj.extractText())
            break
        temp = dic[i].lower()
        if pdfReader.decrypt(temp):
            print('破解成功，密码是 ' + temp + '...')
            #进入PDF
            print('PDF有 '+ str(pdfReader.numPages) + '...')
            print('内容摘要')
            pageObj = pdfReader.getPage(0)
            print(pageObj.extractText())
            break
        print('失败')
    print('程序关闭...')
    sys.exit()