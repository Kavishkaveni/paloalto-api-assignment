from flask import Flask, request
import requests

app = Flask(__name__)

FIREWALL_IP = "https://paloalto.qcetl.com:9443"
API_KEY = "LUFRPT1taGNOc0xxbkZZN2ZLWnBaaHJIM1pGVVdHMU09Vkc0c3NYSlEyeEpnTUx3dFloQkd6OUxHSWp4NXhDT214R3NYeHVWSmR2d3dwTDlJZ2s3ZEdUQTF0WmpZaVFFMQ=="

def add_security_rule(rule_name):
    xpath = "/config/devices/entry/vsys/entry/rulebase/security/rules"
    element = f"""
    <entry name='{rule_name}'>
        <from><member>any</member></from>
        <to><member>any</member></to>
        <source><member>192.168.1.0/24</member></source>
        <destination><member>8.8.8.8</member></destination>
        <service><member>service-http</member><member>service-https</member></service>
        <action>allow</action>
    </entry>
    """
    params = {
        "type": "config",
        "action": "set",
        "xpath": xpath,
        "element": element,
        "key": API_KEY,
        "position": "1"
    }
    response = requests.get(FIREWALL_IP + "/api/", params=params, verify=False)
    return response.text

def commit_changes():
    commit_url = f"{FIREWALL_IP}/api/?type=commit&cmd=<commit></commit>&key={API_KEY}"
    response = requests.get(commit_url, verify=False)
    return response.text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rulename = request.form['rulename']
        add_response = add_security_rule(rulename)
        commit_response = commit_changes()
        return f"Rule added! API response:<br><pre>{add_response}</pre><br>Commit response:<br><pre>{commit_response}</pre>"
    return '''
        <h1>Welcome to the Palo Alto Rule Manager</h1>
        <h2>Add New Rule</h2>
        <form method="POST">
            Rule Name: <input type="text" name="rulename"><br><br>
            <input type="submit" value="Add Rule">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)