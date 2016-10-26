import sys

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

file = sys.argv[2]
print(file)
with open(file) as f:
    content = f.read().splitlines()
    print(content)

# routes = []
# for ip in content:
#     if ip not in routes:
#         print("Adding routes {}".format(ip))
#         db.add_route(ip, route)
#         ips.append(routes)
#
# ips = db.get_node_ips()
# for ip in ips:
#     print("Found IP: {}".format(ip)
