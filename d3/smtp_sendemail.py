#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
#然后，通过SMTP发出去：
# 输入Email地址和口令:
from_addr = '**********@**.com'
password = '***************'
# 输入收件人地址:
to_addr = 'yangpuqing2@outlook.com'
# 输入SMTP服务器地址:
smtp_server='smtp.qq.com'
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 587) # SMTP协议默认端口是25
#server = smtplib.SMTP_SSL('smtp.qq.com',465) #设置了SMTP服务器为stmp.qq.com 其端口号为465
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr,[to_addr], msg.as_string())
server.quit()
