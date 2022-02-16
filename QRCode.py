#!C:\Users\ACER\anaconda3\python.exe
#!/usr/local/bin/python

import cgi, os
import pyqrcode
import png
import cgitb
cgitb.enable()

print('Content-Type: text/html\r\n\r\n')
form = cgi.FieldStorage()
link = str(form.getvalue('link'))
# link = "https://web.facebook.com/muhammad.khairie.733"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)


print('<html>')
print('<body>') 
print('<fieldset><legend><h1>Your QR Code</h1></legend>')
print('<center><img src="instagram.png" width="30%" height="30%"> </center></fieldset>')
print('</body>')
print('</html>')