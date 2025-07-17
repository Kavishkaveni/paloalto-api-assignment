# Palo Alto API Assignment

This project allows adding a security rule to the Palo Alto firewall using Flask and API.

## Files
  1. `test_api.py`  
	  • This is your basic test script to check if you can connect to the firewall API and get a response (like device info).  
	  • It’s useful to prove you tested the API connection works.

2. `add_rule.py`  
	 • This script was your first version to add the security rule via API (without web UI).  
	 • It directly sends the API request to add the rule and commit.  
	 • You can include it to show you tried a standalone script approach.

3. `app.py`  
	 • This is the final version with web UI you built for the assignment.  
	 • It lets user input the rule name on a webpage and adds + commits the rule using API calls.


## How to Run

1. Install dependencies:
   ```bash
   pip install flask requests
   
2. Run the Flask app:
   ```bash
   python app.py

3. Open in browser:
   ```text
   http://127.0.0.1:5000
   
5. Enter rule name and submit.
   API response and commit message will be displayed.


