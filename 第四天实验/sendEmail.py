import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import platform

def send():
    if __name__ == '__main__':
        fromaddr = 'zcd1148241614@163.com'
        password = 'zcd158358'
        toaddrs = ['1148241614@qq.com', 'zcd1148241614@163.com']

        result = platform.platform()
        content = result.read()
        textApart = MIMEText(content)
        # print(content)
        zipFile = 'zipnew.zip'
        zipApart = MIMEApplication(open(zipFile, 'rb').read())
        zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

        m = MIMEMultipart()
        m.attach(textApart)
        m.attach(zipApart)
        m['Subject'] = 'title'

        imageFile = '1.png'
        imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
        imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

        try:
            server = smtplib.SMTP('smtp.163.com')
            server.login(fromaddr, password)
            server.sendmail(fromaddr, toaddrs, m.as_string())
            print('success')
            server.quit()
        except smtplib.SMTPException as e:
            print('error:', e)  # 打印错误
