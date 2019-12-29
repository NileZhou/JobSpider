from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.image import MIMEImage
from os import sep


def send_simple_mail(txt, receiver):
    host_server = 'smtp.qq.com'
    sender_qq = '修改成您自己的'
    pwd = "修改成您自己的"
    sender = '修改成您自己的qq邮箱'
    mail_title = '网站存活检测报告'

    # 邮件正文内容
    msg = MIMEMultipart('related')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender
    msg["To"] = Header("您有一封网站存活检测报告", 'utf-8')  # 接收者的别名

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    # 邮件正文内容
    mail_body = "<p>您需要的网站存活检测报告到啦</p>"
    for line in txt.split('\n'):
        mail_body = mail_body+"<br>"+line

    msgText = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msgText)

    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def send_mail(key, receiver):
    # 设置登录及服务器信息
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # 发件人qq
    sender_qq = '1033161554'
    # 发件人qq邮箱授权码
    pwd = "frxgpxefroelbdfh"
    # 发件人邮箱
    sender = '1033161554@qq.com'

    data_dir = "data"+sep

    # 邮件标题
    mail_title = key+'职位分析报告'

    # 邮件正文内容
    msg = MIMEMultipart('related')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender
    msg["To"] = Header("亲", 'utf-8')  # 接收者的别名

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    # 邮件正文内容
    mail_body = """
     <p>您需要的职位技能分析结果到啦</p>
     <p>附件是分析结果, 数字越大的词语重要性越高</p>
     <p>职位技能关键词词云：</p>
     <center><img src="cid:cloud" width="70%", height="70%"></center>
    """

    msgText = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msgText)

    # 指定图片为当前目录
    fp = open(data_dir+key+'_cloud.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', 'cloud')
    msg.attach(msgImage)

    # 构造附件1
    att1 = MIMEText(open(data_dir+key+'_key_skills.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="attach.txt"'
    msg.attach(att1)

    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


