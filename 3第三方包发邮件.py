#!/usr/bin/env python
# -*- coding:utf-8 -*-
import zmail

# 你的邮件内容
mail_content = {
    'subject': input("请输入邮件的主题:"),  # 随便填写
    'content': input("请输入邮件内容:"),  # 随便填写
    'attachments': input("请输入附件地址(没有则留空):"),
}
# 使用你的邮件账户名和密码登录服务器
server = zmail.server('mayaobo1996@qq.com', 'xjffpnpdksxyfgbj')
# 发送邮件
server.send_mail(input("请输入收件人:"), mail_content)
