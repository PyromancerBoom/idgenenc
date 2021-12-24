from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (2000, 2000), (27, 27, 27))  # image created
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('verdana.ttf', size=48)

import os
import datetime
import qrcode
import time
import database

nm_date = datetime.datetime.now()
nm_format_date = nm_date.strftime("%d-%m-%Y \t\t\t\t Q-OVID 19 Id \t\t\t\t %I:%M:%S %p")

print('********************************************************************************')
print(" " + nm_format_date)
print('********************************************************************************')

print('\n\n All fields are mandatory')
print('\n\n Avoid spelling mistakes')
print('\n\n Fire at will!')
print('\n\n')

cough = input(" Are you suffering from dry cough or any other form of cough? (y/n) ")
cold = input("\n Are you suffering from cold or running nose? (y/n)")
fever = input("\n Are you suffering from high body temperatures? (y/n) ")
risk_level = ''

if cough == 'y' and cold == 'y' and fever == 'y':
    risk_level = 'Very High risk'
    print('\n Very High risk')
if cough == 'y' and cold == 'n' and fever == 'y':
    risk_level = 'High risk'
    print('\n High risk')
if cough == 'n' and cold == 'y' and fever == 'y':
    risk_level = 'High risk'
    print('\n High risk')
if cough == 'y' and cold == 'y' and fever == 'n':
    risk_level = 'Moderate risk'
    print('\n Moderate risk')
if cough == 'y' and cold == 'n' and fever == 'n':
    risk_level = 'Moderate risk'
    print('\n Moderate risk')
if cough == 'n' and cold == 'y' and fever == 'n':
    risk_level = 'Moderate risk'
    print('\n Moderate risk')
if cough == 'n' and cold == 'n' and fever == 'n':
    risk_level = 'Low risk'
    print('\n low risk')

mask = input("\n\n\n Are you wearing a mask in a public place? (y/n) ")
mask_on = ''
if mask == 'y':
    mask_on = "Mask used"
else:
    mask_on = "Mask not used"

social = input("\n Are you following social distancing in public places? (y/n) ")
social_on = ''
if social == 'y':
    social_on = 'follows social distancing'
else:
    social_on = 'does not follow social distancing'

(x, y) = (550, 50)
mess = 'Q-OVID 19'
color = 'rgb(70,188,222)'
font = ImageFont.truetype('arial.ttf', size=160)
draw.text((x, y), mess, fill=color, font=font)

print("\n\n\n  Please wait...")
time.sleep(3)
os.system('cls')

(x, y) = (50, 450)
mess = input('\n Enter Full Name (Upto 18 characters only): ')
name = mess
color = 'rgb(255,255,255)'
font = ImageFont.truetype('verdana of.ttf', size=110)
draw.text((x, y), mess, fill=color, font=font)

(x, y) = (50, 750)
mess = input('\n Enter Your Gender: ')
gender = mess
color = 'rgb(255,255,255)'
font = ImageFont.truetype('verdana.ttf', size=110)
draw.text((x, y), mess, fill=color, font=font)

(x, y) = (700, 750)
mess = input('\n Enter Your Age: ')
age = mess
color = 'rgb(255,255,255)'
font = ImageFont.truetype('verdana.ttf', size=110)
draw.text((x, y), mess, fill=color, font=font)

(x, y) = (50, 1050)
mess = input('\n Enter Your Date of Birth: ')
dob = mess
color = 'rgb(255,255,255)'
font = ImageFont.truetype('verdana.ttf', size=110)
draw.text((x, y), mess, fill=color, font=font)

(x, y) = (50, 1350)
mess = input('\n Enter Your Blood Group: ')
blood = mess
color = 'rgb(255,255,255)'
font = ImageFont.truetype('verdana.ttf', size=110)
draw.text((x, y), mess, fill=color, font=font)

(x, y) = (50, 1650)
mess = input('\n Enter your Aadhar Number: ')
aadhar = mess
color = 'rgb(241,241,241)'
font = ImageFont.truetype('verdana.ttf', size=110)
draw.text((x, y), mess, fill=color, font=font)

image.save(str(name) + '.png')
img = qrcode.make(str(risk_level) + str('\n') + str(aadhar) + str('\n') + str(social_on) + str('\n') + str(mask_on),
                  box_size=8, border=16, version=12)
img.save(str(aadhar) + '.bmp')

till = Image.open(name + '.png')
naruto = Image.open(str(aadhar) + '.bmp')
till.paste(naruto, (1100, 450))
till.save(name + '.png')

database.AddRecord(name, aadhar, risk_level)

print('\n\n Q-OVID 19 Id Successfully created as ' + name + '.png')

ch = input("\n\n\n  Would you like to encrypt your Q-OVID ID? (y/n)  >>> ")
if (ch == "y"):
    print("\n\n Running Encryption program...")
    time.sleep(3)
    os.system("encryption.py")
else:
    input('\n\n Press any key to close program....')
