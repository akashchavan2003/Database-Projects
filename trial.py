import subprocess

def connect_to_wifi(ssid, password):
    command = f'netsh wlan connect name="{ssid}" ssid="{ssid}" keyMaterial="{password}"'
    subprocess.run(command, shell=True)

# Replace 'YourSSID' and 'YourPassword' with the actual SSID and password
connect_to_wifi('Redmi Note 10', '11223344')
