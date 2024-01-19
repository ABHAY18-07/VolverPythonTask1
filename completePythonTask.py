import wmi

import pyautogui
import requests
import uuid
connection = wmi.WMI()
for os in connection.Win32_OperatingSystem():
	print("OS Name:",os.Name)
	print("\nOS Articture:", os.OsArchitecture)
	print("\nRAM Size:", os.TotalVisibleMemorySize) 
     

software = connection.Win32_Product()

print("List of Installed Software")
for product in software:
    print(f"Software: {product.Name}")
    

print("Screen Size")
print(pyautogui.size())

def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text
print("Public IP Address:")
print(get_public_ip())
cpu = connection.Win32_Processor()[0]
print(f"CPU Name: {cpu.Name}")
print(f"CPU Number of Cores: {cpu.NumberOfCores}")
print(f"CPU Max Clock Speed: {cpu.MaxClockSpeed} MHz")

controllers = wmi.WMI().Win32_VideoController()

gpu_data = list()

for controller in controllers:
   controller_info = {
        'Name': controller.wmi_property('Name').value,
        'HRes': controller.wmi_property('CurrentHorizontalResolution').value,
        'VRes': controller.wmi_property('CurrentVerticalResolution').value,
    }
   gpu_data.append(controller_info)
print(gpu_data)
print("mac address: ")

print (hex(uuid.getnode()))