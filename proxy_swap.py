# proxy_swap.py
# when current use of proxies hit 5, we swap and resume.

import os
import random

proxy_list = "proxies.txt"
combo_list = "combo.txt"
proxies = []
data = []
currentproxy = ""
emails = []
passwords = []
parsed_passwords = []


def split():
    for x in data:
        y = x.split(":")
        passwords.append(y[1:4])
        emails.append(y[0])


def combine():
    for passes in passwords:  # iterates through each tuple
        for item in passes:  # iterates through each tuple items
            parsed_passwords.append(item)

def start_proxy_swap():
	currentproxy = ""
	for d, e in zip(emails, parsed_passwords):
		currproxy = switch_proxy(currentproxy)
		print d + ":" + e + " is using proxy: " + currproxy
	else:
		print 'error'
def switch_proxy(currentproxy):
	currentproxy = proxies[random.randint(0, len(proxies)-1)]
	return currentproxy
	
if os.path.exists(combo_list):
	combo_reader = open(combo_list, 'r')
	for combo in combo_reader.readlines():
		if combo != "":
			data.append(combo.strip())
		combo_reader.close()
else:
	print '[-][-] Combo list not found... quitting.'
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
start_proxy_swap()
