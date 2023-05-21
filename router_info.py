import subprocess

def scan_wifi():
    interface_name = 'wlan0'#change to your wireless network adapter which is internet connected.
    process = subprocess.Popen(['sudo','iwlist', interface_name, 'scan'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    output, _ = process.communicate()
    networks = []
    lines = output.decode('utf-8').split('\n')
    ssid = bssid = signal_strength = frequency= None
    total_routers = 0 
    for line in lines:
        if 'ESSID:' in line:
            ssid = line.split('ESSID:"')[1].split('"')[0]
        elif 'Address:' in line:
            bssid = line.split('Address: ')[1]
        elif 'Frequency:' in line:
            frequency = line.split(':')[1]
        elif 'Quality=' in line:
            signal_strength = line.split('Quality=')[1].split()[0].split('/')[0]

        if ssid and bssid and signal_strength  and frequency:
            total_routers +=1
            networks.append({'SSID': ssid, 'BSSID': bssid, 'Signal Strength': signal_strength,'Frequency':frequency})
            ssid = bssid = signal_strength  =frequency= None

    print("Available Wi-Fi Networks:")
    print("--------------------------------------------------")
    for network in networks:
        print(f"SSID: {network['SSID']}")
        print(f"BSSID: {network['BSSID']}")
        print(f"Signal Strength: {network['Signal Strength']} dBm")
        print(f"Frequency: {network['Frequency']}")
        print("--------------------------------------------------")
    print('Total routers/WAP : ',total_routers)
scan_wifi()
