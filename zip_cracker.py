#!/usr/bin/python
#coding: utf-8
#Coded By Callix aka ./W4ST3D

import zipfile,os
from colorama import *
init()
gr = "\033[31m[\033[92m+\033[31m]\033[92m"
rd = "\033[31m[\033[92m-\033[31m]\033[91m"
wh = "\033[0m"
sp = "\n"

os.system('title [+] ZIP File Password Cracker Coded Callix - ./W4ST3D && cls')

print(gr+" ZIP File Password Cracker Coded Callix - ./W4ST3D"+sp)

zfile = raw_input(gr+" Enter Your ZIP File : "+wh)

with open(raw_input(sp+gr+" Enter Password list : "+wh),'r') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile(zfile,'r') as zf:
                zf.extractall(pwd=password)
                data = zf.namelist()[0]
                data_size = zf.getinfo(data).file_size
                print(sp+gr+''' Password found! ~ %s\n ~%s\n ~%s\n''' 
                    % (password.decode('utf8'), data, data_size))
                save=open('cracked.txt','a').write("File : "+zfile+sp+"Password : "+password+sp+sp)
                break
        except:
            print(sp+rd+' Password failed! - %s' % (password.decode('utf8')))
            pass
