# -*- coding: utf-8 -*-
#
# Time: 2024-01-14
# File: send_email.py
# URL: https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第29课：用Python发送邮件和短信.md
#      https://www.freecodecamp.org/chinese/news/send-emails-using-code/
#      https://www.runoob.com/python/python-email.html
# Description: python 批量发送邮件，邮件内容有模板但不完全相同
#              如不同的人邮件中写对方的名字等，但模板格式相同
#              执行有错误，发送邮件失败 smtplib.SMTPDataError: (550, b'2f2f65a4e314d53-56da9 Mail rejected')

import ssl
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

EMAIL_USER = 'email.com'
EMAIL_AUTH = 'authorization password' # 授权码
#
EMAIL_HOST = 'smtp.163.com' # smtp 邮件服务器地址
EMAIL_PORT = 465

CONTACT_FILE = "./email_contacts/contacts.txt"
TEMPLATE_FILE = "./email_contacts/message.txt"


# 从文件中获取联系人，姓名，email
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as f:
        for contact in f:
            names.append(contact.split(',')[0])
            emails.append(contact.split(',')[1])
        return names, emails


# 邮件正文模板 模板不要过大
def read_template(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        content = f.read()
    return Template(content)


def main():
    names, emails = get_contacts(CONTACT_FILE)
    print(names, emails)
    message_template = read_template(TEMPLATE_FILE)
    print(message_template)

    # 不添加下面的代码则提示 ssl 握手失败，ssl 协议冲突，可能是版本问题
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.set_ciphers('AES256-SHA256')

    s = smtplib.SMTP_SSL(host=EMAIL_HOST, port=EMAIL_PORT, context=context)
    s.login(EMAIL_USER, EMAIL_AUTH)

    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        content = message_template.substitute(NAME=name.strip().title(), EMAIL=email.strip())

        print(name, email)
        print(content)

        msg['From'] = EMAIL_USER
        msg['To'] = email
        msg['Subject'] = 'test email 1'

        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        # print(type(msg), msg)

        # error：smtplib.SMTPDataError: (550, b'2f2f65a4e314d53-56da9 Mail rejected')
        # s.sendmail(EMAIL_USER, email, msg.as_string())
        # s.send_message(msg, EMAIL_USER, email)
        s.send_message(msg)
        del msg

    s.quit()


if __name__ == '__main__':
    main()