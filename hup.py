import requests, time, json, urllib.parse, random, threading, os, sys
from pystyle import Colorate, Colors, Write, Add, Center
os.system("cls" if os.name == "nt" else "clear")
def banner():
 banner = f"""
 \033[1;93m

__      ___                 _______ _ _ _______    _                     _ 
\ \    / (_)               |__   __(_) |__   __|  | |        /\         (_)
 \ \  / / _  _____      __    | |   _| | _| | ___ | | __    /  \   _ __  _ 
  \ \/ / | |/ _ \ \ /\ / /    | |  | | |/ / |/ _ \| |/ /   / /\ \ | '_ \| |
   \  /  | |  __/\ V  V /     | |  | |   <| | (_) |   <   / ____ \| |_) | |
    \/   |_|\___| \_/\_/      |_|  |_|_|\_\_|\___/|_|\_\ /_/    \_\ .__/|_|
                                                                  | |      
                                                                  |_|      
\033[1;37m===========================================================================
\033[1;34mBản Quyền: \033[1;33mLê Quang Minh (Mun)
\033[1;37m===========================================================================
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush()
banner()
VIDEO = input("\033[1;34mNhập Id Video TikTok : \033[1;33m")
IID = "7136182505984493314", #"7138317669417174786"
DID = "7099666381000918530"

from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
import ssl
import queue
class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r                                 = requests.Session()
countQueue                        = queue.Queue()
sentRequests                      = 0
completed                         = False

r.cookies.set_policy(BlockCookies())
import requests, time, json, urllib.parse, random, threading

def view(video):
   # try:
        
        ve= random.choice(
            [247, 312, 322, 357, 358, 415, 422, 444, 466]
        )
    
        device = random.choice(
            ["SM-G9900", "sm-g950f", "SM-A136U1", "SM-M225FV", "SM-E426B", "SM-M526BR", "SM-M326B", "SM-A528B", "SM-F711B", "SM-F926B", "SM-A037G", "SM-A225F", "SM-M325FV", "SM-A226B", "SM-M426B", "SM-A525F"]
        )
       
        host = random.choice(
            ["api16.tiktokv.com", "api.tiktokv.com", "api19.tiktokv.com", "api21.tiktokv.com","api-t2.tiktokv.com"]
        )
       # ve=random.randint(100,2600)
        params = urllib.parse.urlencode(
            {
                "app_language": "fr",
                "iid": IID,
                "device_id": DID,
                "channel": "googleplay",
                "device_type": device,
                "ac": "wifi",
                "os_version": random.randint(5, 11),
                "version_code": ve,
                "app_name": "trill",
                "device_brand": "samsung",
                "ssmix": "a",
                "device_platform": "android",
                "aid": 1180,
                "as": "a1iosdfgh",  
                "cp": "androide1",
            }
        )

        response = r.post(
            url = (
                "https://"
                    + host
                    + "/aweme/v1/aweme/stats?"
                    + params
            ),
            
            data = (
                f'&manifest_version_code={ve}'
                    + f'&update_version_code={ve}0'
                    + '&play_delta=1'
                    + f'&item_id={video}'
                    + f'&version_code={ve}'
                    + '&aweme_type=0'
            ), 
            headers = {
                "host": host,
                "connection": "keep-alive",
                "accept-encoding": "gzip",
                "x-ss-req-ticket": str(int(time.time())),
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "user-agent": f"com.ss.android.ugc.trill/{ve} (Linux; U; Android 11; fr_FR; {device}; Build/RP1A.200720.012; Cronet/58.0.2991.0)"
                
            },
            
        )
        try:
         print(response.json())
        except:
         pass

while True:
   for x in range(10000082910000):
    if threading.active_count() < 10:
        threading.Thread(target = view, args = [VIDEO] ).start()
    
