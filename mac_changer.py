# #!/usr/bin/env python3
# 
# import subprocess
# import argparse
# 
# def get_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-n", "--network", dest="network", metavar='', required=True, help="Select network device.")
#     parser.add_argument("-m", "--mac", dest="new_mac", metavar='', required=True, help="Select new MAC address.")
#     return parser.parse_args()
# 
# def spoof_mac(network, new_mac):
#     subprocess.call(["ifconfig", network, "down"])
#     subprocess.call(["ifconfig", network, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", network, "up"])
#     print(f"[+] Changing MAC address for {network} to {new_mac}")
# 
# args = get_args()
# spoof_mac(args.network, args.new_mac)
