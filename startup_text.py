import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import time


phone_number_email = 'number@carrier' 
# Change number in phone_number to your phone number
# Change carier to your carrier's respective address from table below

# AT&T, @mms.att.net
# Sprint, @messaging.sprintpcs.com
# T-Mobile, @tmomail.net
# Verizon, @vtext.com

#i.e '5555555555@mms.att.net

#Change to your own account information
gmail_username = 'test@gmail.com'
gmail_password = 'yourpassword'

s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()
s.ehlo
s.login(gmail_username, gmail_password)
today = datetime.date.today()

#Linux
arg='ip route list'
p = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
my_ip = 'Your ip is %s' % ipaddr
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_username
msg['To'] = phone_number_email
s.sendmail(gmail_username, phone_number_email, msg.as_string())
s.quit()

