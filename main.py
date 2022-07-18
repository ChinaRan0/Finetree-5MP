import requests
header={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

def WeakPassword():
    f = open("taeget.txt","r")
    ff = f.read().splitlines()
    f.close()
    print(f"检测{len(ff)}个目标的弱口令漏洞:")
    post={
        "user": "admin",
        "pwd": "admin",
        "method": "login"
    }
    for it in ff:
        try:
            res1 = requests.post(url=f"http://{it}/",data={"user":"admin","pwd":"admin","method":"login"},headers=header,timeout=10)

            if len(res1.text) <= 2000 :
                print(f"{it}不存在弱口令漏洞")
                with open("NoAdmin.txt","a") as NoAdmin:
                    NoAdmin.write(f"{it}\n")
            else:
                with open("overAdmin.txt","a") as AdminPassword:
                    AdminPassword.write(f"{it}\n")
        except:
            pass
def Unauthorized():
    pass
if __name__ == '__main__':
    WeakPassword()
    Unauthorized()