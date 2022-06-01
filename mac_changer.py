# #!/usr/bin/env python3
# 
# import subprocess
# import argparse
# 
# parser = argparse.ArgumentParser()
# 
# parser.add_argument("-n", "--network", dest="network", metavar='', help="Select network device.")
# parser.add_argument("-m", "--mac", dest="new_mac", metavar='', help="Select new MAC address.")
# 
# args = parser.parse_args()
# 
# def change_mac(network, new_mac):
#     print(f"[+] Changing MAC address for {network} to {new_mac}")
# 
#     subprocess.call(["ifconfig", network, "down"])
#     subprocess.call(["ifconfig", network, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", network, "up"])
# 
# 
# change_mac(args.network, args.new_mac)
