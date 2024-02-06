
import math
mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
   'cucuPhone': 2010,
     'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
     'cucuPhone': 2010,
}
home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}


def is_english(word):
    return all(ord(char) < 128 for char in word)

for device in home_devices:
    if is_english(device):
        print(f"{device} - на английском языке")
    else:
        print(f"{device} - не на английском языке")
