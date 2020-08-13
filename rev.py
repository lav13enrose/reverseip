from urllib3.util.retry import Retry
import requests
from requests.adapters import HTTPAdapter
import sys
import random
import requests, threading, os
import queue as Queue
from datetime import date
import os.path
import threading
today = date.today()
os.system('cls' if os.name == 'nt' else 'clear')
print("""
    ██╗███████╗░█████╗░███╗░░██╗███████╗██╗░░██╗██████╗░██╗░░░░░░█████╗░██╗████████╗
    ██║╚════██║██╔══██╗████╗░██║██╔════╝╚██╗██╔╝██╔══██╗██║░░░░░██╔══██╗██║╚══██╔══╝
    ██║░░███╔═╝██║░░██║██╔██╗██║█████╗░░░╚███╔╝░██████╔╝██║░░░░░██║░░██║██║░░░██║░░░
    ██║██╔══╝░░██║░░██║██║╚████║██╔══╝░░░██╔██╗░██╔═══╝░██║░░░░░██║░░██║██║░░░██║░░░
    ██║███████╗╚█████╔╝██║░╚███║███████╗██╔╝╚██╗██║░░░░░███████╗╚█████╔╝██║░░░██║░░░
    ╚═╝╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░░╚═╝░░░

    [ HackerTarget IPs Reverse ] - facebook.com/lav13enrose 

""")
proxyny = input("[ ? ] Proxy List : ")
def proxy():
    lines = open(proxyny).read().splitlines()
    mylines =random.choice(lines)
    return mylines
webny = input("[ ? ] Web File : ")
check_file = os.path.isfile(today.strftime("%b-%d-%Y")+"_success.txt")
if check_file == 1:
    nanya1 = input("[ ! ] File Result Exist , Delete? : ")
    if ('y') in nanya1 or ('Y') in nanya1:
        os.remove(today.strftime("%b-%d-%Y")+"_success.txt")
    elif ('n') in nanya1 or ('N') in nanya1:
        pass
if check_file == 0:
    pass
def do_print():
    with open(webny,'r') as ips:
        count = len(open(webny).readlines())
        countproxy = len(open(proxyny).readlines())
        print("===============================")
        print("[ ! ] Total IPs : "+str(count))
        print("[ ! ] Total Proxy : "+str(countproxy))
        print("===============================")
        linez = ips.read().splitlines() 
        proxies = { 
            "http"  : "http://"+proxy(), 
        }
        for line in linez:
            try:
                count -= 1
                print("[ + ] IP Sisa : "+str(count)+" -  Checking "+line+" with "+proxy())
                ayam = requests.get(
                    "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                    ).text
                if ("No DNS A records found") in ayam:
                    print("Error : No DNS A Records")
                elif ("Many Requests") in ayam:
                    print("Error : Many Requests")
                elif ("error check your search parameter") in ayam:
                    print("Website Error")
                    cuakz = open("error_log.txt", "+a")
                    cuakz.write(ayam)
                    cuakz.close()
                elif ("API count exceeded") in ayam:
                    print("[ ! ] Rechecking "+line+" with "+proxy())
                    ayam = requests.get(
                    "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                    ).text
                    if ("No DNS A records found") in ayam:
                        print("Error : No DNS A Records")
                    elif ("Many Requests") in ayam:
                        print("Error : Many Requests")
                    elif ("error check your search parameter") in ayam:
                        print("Website Error")
                        cuakz = open("error_log.txt", "+a")
                        cuakz.write(ayam)
                        cuakz.close()
                    elif ("API count exceeded") in ayam:
                        print("[ ! ] Rechecking "+line+" with "+proxy())
                        ayam = requests.get(
                        "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                        ).text
                        if ("No DNS A records found") in ayam:
                            print("Error : No DNS A Records")
                        elif ("Many Requests") in ayam:
                            print("Error : Many Requests")
                        elif ("error check your search parameter") in ayam:
                            print("Website Error")
                            cuakz = open("error_log.txt", "+a")
                            cuakz.write(ayam)
                            cuakz.close()
                        elif ("API count exceeded") in ayam:
                            print("[ ! ] Rechecking "+line+" with "+proxy())
                            ayam = requests.get(
                            "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                            ).text
                        else:
                            a = open("temp_resulz.txt","+a")
                            a.write(ayam)
                            a.close()
                            countz = len(open("temp_resulz.txt").readlines())
                            print("[ SUCCESS ] Reversed - "+line+" [ Got "+str(countz)+" Website ]")
                            cuak = open(today.strftime("%b-%d-%Y")+"_success.txt", "+a")
                            cuak.write(ayam)
                            cuak.close()
                            os.remove("temp_resulz.txt")
                    elif ("API count exceeded") in ayam:
                        print("[ ! ] Rechecking "+line+" with "+proxy())
                        ayam = requests.get(
                        "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                        ).text
                else:
                    a = open("temp_resulz.txt","+a")
                    a.write(ayam)
                    a.close()
                    countz = len(open("temp_resulz.txt").readlines())
                    print("[ SUCCESS ] Reversed - "+line+" [ Got "+str(countz)+" Website ]")
                    cuak = open(today.strftime("%b-%d-%Y")+"_success.txt", "+a")
                    cuak.write(ayam)
                    cuak.close()
                    os.remove("temp_resulz.txt")
            except:
                try:
                    print("[ ! ] Rechecking "+line+" with "+proxy())
                    ayam = requests.get(
                    "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                    ).text
                    if ("No DNS A records found") in ayam:
                        print("Error : No DNS A Records")
                    elif ("Many Requests") in ayam:
                        print("Error : Many Requests")
                    elif ("error check your search parameter") in ayam:
                        print("Website Error")
                        cuakz = open("error_log.txt", "+a")
                        cuakz.write(ayam)
                        cuakz.close()
                    elif ("API count exceeded") in ayam:
                        print("[ ! ] Rechecking "+line+" with "+proxy())
                        ayam = requests.get(
                        "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                        ).text
                    else:
                        a = open("temp_resulz.txt","+a")
                        a.write(ayam)
                        a.close()
                        countz = len(open("temp_resulz.txt").readlines())
                        print("[ SUCCESS ] Reversed - "+line+" [ Got "+str(countz)+" Website ]")
                        cuak = open(today.strftime("%b-%d-%Y")+"_success.txt", "+a")
                        cuak.write(ayam)
                        cuak.close()
                        os.remove("temp_resulz.txt")
                except:
                    print("[ ! ] Rechecking "+line+" with "+proxy())
                    ayam = requests.get(
                    "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                    ).text
                    if ("No DNS A records found") in ayam:
                        print("Error : No DNS A Records")
                    elif ("Many Requests") in ayam:
                        print("Error : Many Requests")
                    elif ("error check your search parameter") in ayam:
                        print("Website Error")
                        cuakz = open("error_log.txt", "+a")
                        cuakz.write(ayam)
                        cuakz.close()
                    elif ("API count exceeded") in ayam:
                        print("[ ! ] Rechecking "+line+" with "+proxy())
                        ayam = requests.get(
                        "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                        ).text
                    else:
                        a = open("temp_resulz.txt","+a")
                        a.write(ayam)
                        a.close()
                        countz = len(open("temp_resulz.txt").readlines())
                        print("[ SUCCESS ] Reversed - "+line+" [ Got "+str(countz)+" Website ]")
                        cuak = open(today.strftime("%b-%d-%Y")+"_success.txt", "+a")
                        cuak.write(ayam)
                        cuak.close()
                        os.remove("temp_resulz.txt")
                    try:
                        print("[ ! ] Rechecking "+line+" with "+proxy())
                        ayam = requests.get(
                        "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                        ).text
                        if ("No DNS A records found") in ayam:
                            print("Error : No DNS A Records")
                        elif ("Many Requests") in ayam:
                            print("Error : Many Requests")
                        elif ("error check your search parameter") in ayam:
                            print("Website Error")
                            cuakz = open("error_log.txt", "+a")
                            cuakz.write(ayam)
                            cuakz.close()
                        elif ("API count exceeded") in ayam:
                            print("[ ! ] Rechecking "+line+" with "+proxy())
                            ayam = requests.get(
                            "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                            ).text
                        else:
                            a = open("temp_resulz.txt","+a")
                            a.write(ayam)
                            a.close()
                            countz = len(open("temp_resulz.txt").readlines())
                            print("[ SUCCESS ] Reversed - "+line+" [ Got "+str(countz)+" Website ]")
                            cuak = open(today.strftime("%b-%d-%Y")+"_success.txt", "+a")
                            cuak.write(ayam)
                            cuak.close()
                            os.remove("temp_resulz.txt")
                    except:
                        print("[ ! ] Rechecking "+line+" with "+proxy())
                        ayam = requests.get(
                        "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                        ).text
                        if ("No DNS A records found") in ayam:
                            print("Error : No DNS A Records")
                        elif ("Many Requests") in ayam:
                            print("Error : Many Requests")
                        elif ("error check your search parameter") in ayam:
                            print("Website Error")
                            cuakz = open("error_log.txt", "+a")
                            cuakz.write(ayam)
                            cuakz.close()
                        elif ("API count exceeded") in ayam:
                            print("[ ! ] Rechecking "+line+" with "+proxy())
                            ayam = requests.get(
                            "http://api.hackertarget.com/reverseiplookup/?q="+line,timeout=5,proxies=proxies
                            ).text
                        else:
                            a = open("temp_resulz.txt","+a")
                            a.write(ayam)
                            a.close()
                            countz = len(open("temp_resulz.txt").readlines())
                            print("[ SUCCESS ] Reversed - "+line+" [ Got "+str(countz)+" Website ]")
                            cuak = open(today.strftime("%b-%d-%Y")+"_success.txt", "+a")
                            cuak.write(ayam)
                            cuak.close()
                            os.remove("temp_resulz.txt")
threading.Thread(target=do_print).start()
print("===============================")
count_result = len(open(today.strftime("%b-%d-%Y")+"_success.txt").readlines())
print("[ + ] Total Result : "+str(count_result))
                
