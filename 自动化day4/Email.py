def send_mail(project_name, version, filename, revicers):
    import zmail

    # 邮件内容
    email_content = {
        'subject': '{}项目{}版本自动化测试报告'.format(project_name, version),
        'content_text': '{}项目{}版本自动化测试完毕，具体测试报告请查看附件详情'.format(project_name, version),
        'attachments': filename
    }

    # 收件人
    # addressee = ['2167365108@qq.com']
    addressee = revicers

    # 发件人
    sender = {'username': '1539533097@qq.com', 'password': 'ernxaotdssgdfjjg'}

    try:
        # 发送邮件
        server = zmail.server(sender['username'], sender['password'])
        # 把邮件发送给收件人
        server.send_mail(addressee, email_content)
        print("邮件发送成功")
    except Exception as cause:
        print("无法发送邮件", cause)


# send_mail('hkr登录测试报告', 'V01', r'HKR.xlsx', '2167365108@qq.com')  # 老贾:'2431320433@qq.com'
