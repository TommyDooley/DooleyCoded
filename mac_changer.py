#!/usr/bin/env python3

#import subprocess
#import optparse

#def change_mac(network, new_mac):
    #print(f"[+] Changing MAC address for {network} to {new_mac}")
#
    #subprocess.call(["ifconfig", network, "down"])
    #subprocess.call(["ifconfig", network, "hw", "ether", new_mac])
    #subprocess.call(["ifconfig", network, "up"])

#parser = optparse.OptionParser()

#parser.add_option("-n", "--network", dest="network", help="Interface to change MAC address.")
#parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address.")

#(options, args) = parser.parse_args()

#change_mac(options.network, options.new_mac)