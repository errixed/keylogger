import smtplib, ssl

def sendEmail(message):
	smtp_server = "smtp.gmail.com"
	port = 587 
	main_email = "your email address"
	password = "password of main email address"
	secondary_email = "your email address"

	context = ssl.create_default_context()

	try:
		server = smtplib.SMTP(smtp_server,port)
		server.ehlo() 
		server.starttls(context=context) 
		server.ehlo()
		server.login(main_email, password)
		server.sendmail(main_email, secondary_email, message)
		
	except Exception as e:
		print(e)
	finally:
		server.quit()