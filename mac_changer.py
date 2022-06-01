#!/usr/bin/env python3

# import subprocess
# import argparse

# def change_mac(network, new_mac):
#     print(f"[+] Changing MAC address for {network} to {new_mac}")

#     subprocess.call(["ifconfig", network, "down"])
#     subprocess.call(["ifconfig", network, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", network, "up"])

# parser = argparse.ArgumentParser()

# parser.add_argument("-n", "--network", dest="network", help="Interface to change MAC address.")
# parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address.")

# args = parser.parse_args()

# change_mac(args.network, args.new_mac)
