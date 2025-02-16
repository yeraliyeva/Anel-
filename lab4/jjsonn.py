import json 
date = 'sample-data.json'
with open(date,"r") as file:
    data = json.load(file)
out = []
out.append("interface status")
out.append("="* 90)
out.append(f"{'DN:<50'} {'description:<20'} {'speed':<10} {'mtu' :<10}")
out.append("-"*90)
for datas in data["imdata"]:
    m = datas["l1PhysIf"]["attributes"]
    out.append(f"{m['dn']:<50} {m['pathSDescr']:<20} {m['speed']:<10} {m['mtu']:<10}")
for i in out:
    print(i)




