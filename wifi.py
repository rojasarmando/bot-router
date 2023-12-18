import os

def disable_wifi():
    os.system("ip link set dev wlan0 down")

def enable_wifi():
    os.system("ip link set dev wlan0 up")