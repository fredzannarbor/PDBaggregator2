import sys
import json
import srvdb

db = srvdb.SrvDb("./pdb-aggregator.db")
file = sys.argv[1]
print(file)
with open(file) as f:
    content = f.read().splitlines()
    print(content)

ips = []
for ip in content:
    if ip not in ips:
        print("Adding node {}".format(ip))
        db.add_node(ip, False, 0, "")
        ips.append(ip)
