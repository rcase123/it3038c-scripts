
#You must first use (pip install pypng)  and   (pip install pyqrcode)  for this to work

#importing plug ins
import pyqrcode
import png
from pyqrcode import QRCode 

#Text explaining program and what to do
print(" ")
print("With this program you can enter information and convert it to a QR Code")
print(" ")
print("I suggest using your email or a link to video you want to share")
print(" ")
text_entered = input ("Enter the information you want to be converted: ")

# Captured text from the input 
s = text_entered
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png in the same location as the script files location. 
# It will be name YourNewQRCode.png
 
url.png('YourNewQRCode.png', scale = 6) 

#explaining where the qr code is
print(" ")
print("Your QR Code picture has been saved to the same location as this program")
print(" ")
print("Have a nice day!")