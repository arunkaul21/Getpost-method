import requests

data ={"email": "anand@tache.in", "password": "tachee"}
resp = requests.post("http://13.233.186.205/rest-auth/login/", data)

print(resp.text)
print(resp.status_code)
if resp.status_code != 200:
    print("Bad Status")
elif resp.status_code !=400:
    print("OK Status") 
#a= r.json()
#print(a.text)
headers = {
 'Authorization':'Token df60cad8f46658cdc1a03938aafdacebbef44f9c', 
 'Content-Type':'application/json'
}
a = requests.get("http://13.233.186.205/links/missions/", headers=headers)
b = a.json()
print(b['results'])
for r in b['results']:
  print(r['survey'])