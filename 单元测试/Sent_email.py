import zmail

# 邮件内容
msg_content = {
    'subject': '计算器的测试报告',
    'content_text': '计算器测试报告',
    'attachments': ['计算器.html']
}

# 收件人
reviceser = [ '863091485@qq.com']

# 发件人
sender = {'username': '1539533097@qq.com', 'pwd': 'ernxaotdssgdfjjg'}

# 发送邮件
server = zmail.server(sender['username'], sender['pwd'])
# 把邮件发送给收件人
server.send_mail(reviceser, msg_content)
