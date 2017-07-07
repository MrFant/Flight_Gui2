# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
def Post_Email(content,receive):
	mail_host = 'smtp.qq.com'
	mail_user = '2413633136@qq.com'
	mail_pass = 'vnilclloyvsvecaf'
	sender = '2413633136@qq.com'
	receivers = ['2413633136@qq.com',receive]
	message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = 'Author:Fant'
	message['From'] = '机票监测2.0测试版'
	message['To'] = receivers[1]
	try:
		smtpObj = smtplib.SMTP()
		smtpObj = smtplib.SMTP_SSL(mail_host)
		smtpObj.login(mail_user, mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		#message['To'] = receivers[1]
		#smtpObj.sendmail(sender, receivers, message.as_string())
		smtpObj.quit()
		#print('success')
	except smtplib.SMTPException as e:
		print('error', e)

if __name__=="__main__":
    Post_Email("testing","1911986472@qq.com")


