# Palo Alto API Assignment

This project allows adding a security rule to the Palo Alto firewall using Flask and API.

## Files
  1. `test_api.py`  
	  • Test script to check connection with the firewall API and retrieve device information.
          • Useful for validating the API connection.



3. `add_rule.py`  
	 •Initial script for adding a security rule via API without a web interface.
	 •Directly sends the API request to add the rule and commit the changes.


4. `app.py`  
         •Final version with a web interface built using Flask.
	 •Accepts a rule name through a form and performs rule addition and commit through API calls.




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


