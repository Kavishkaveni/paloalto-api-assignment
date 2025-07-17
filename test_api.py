import requests

firewall_ip = "paloalto.qcetl.com"
api_key = "LUFRPT1taGNOc0xxbkZZN2ZLWnBaaHJIM1pGVVdHMU09Vkc0c3NYSlEyeEpnTUx3dFloQkd6OUxHSWp4NXhDT214R3NYeHVWSmR2d3dwTDlJZ2s3ZEdUQTF0WmpZaVFFMQ=="


url = f"https://{firewall_ip}:9443/api/?type=op&cmd=<show><system><info></info></system></show>&key={api_key}"


requests.packages.urllib3.disable_warnings()


response = requests.get(url, verify=False)


print(response.text)