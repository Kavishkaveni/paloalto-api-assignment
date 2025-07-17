import requests

firewall_ip = "paloalto.qcetl.com"

api_key = "LUFRPT1taGNOc0xxbkZZN2ZLWnBaaHJIM1pGVVdHMU09Vkc0c3NYSlEyeEpnTUx3dFloQkd6OUxHSWp4NXhDT214R3NYeHVWSmR2d3dwTDlJZ2s3ZEdUQTF0WmpZaVFFMQ=="

rule_name = "Kavishka"
source_ip = "192.168.1.0/24"
dest_ip = "8.8.8.8/32"


base_url = f"https://{firewall_ip}:9443/api/"


requests.packages.urllib3.disable_warnings()


xpath = "/config/devices/entry/vsys/entry/rulebase/security/rules"


rule_xml = f"""
<entry name="{rule_name}">
  <from><member>any</member></from>
  <to><member>any</member></to>
  <source><member>{source_ip}</member></source>
  <destination><member>{dest_ip}</member></destination>
  <service>
    <member>service-http</member>
    <member>service-https</member>
  </service>
  <action>allow</action>
</entry>
"""

def add_rule():
    params = {
        "type": "config",
        "action": "set",
        "key": api_key,
        "xpath": xpath,
        "element": rule_xml,
        "position": "1"  
    }
    response = requests.post(base_url, params=params, verify=False)
    if response.status_code == 200 and "success" in response.text:
        print("Rule added successfully.")
        return True
    else:
        print("Failed to add rule.")
        print(response.text)
        return False

def commit_config():
    params = {
        "type": "commit",
        "key": api_key,
        "cmd":"<commit></commit>"
    }
    response = requests.post(base_url, params=params, verify=False)
    if response.status_code == 200 and "success" in response.text:
        print("Commit started successfully.")
        return True
    else:
        print("Commit failed.")
        print(response.text)
        return False

if  __name__ == "__main__":
    if add_rule():
        commit_config()