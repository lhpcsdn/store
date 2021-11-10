def send_mail(project_name, version, filename, revicers):
    import zmail

    # 邮件内容
    email_content = {
        'subject': '{}项目{}版本自动化测试报告'.format(project_name, version),
        'content_text': '{}项目{}版本自动化测试完毕，具体测试报告请查看附件详情'.format(project_name, version),
        'attachments': filename
    }

    # 收件人
    # revicer = ['2167365108@qq.com']
    revicer = revicers

    # 发件人
    sender = {'username': '1539533097@qq.com', 'pwd': 'ernxaotdssgdfjjg'}

    # 发送邮件
    server = zmail.server(sender['username'], sender['pwd'])
    # 把邮件发送给收件人
    server.send_mail(revicer, email_content)


# send_mail('论坛', 'V03', r'E:\python\python1\day13【单元测试】\计算器.html', '2167365108@qq.com')
