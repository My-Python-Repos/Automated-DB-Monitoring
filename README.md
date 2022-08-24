### What is this?
We can use this script to retrieve data from database, and set conditions to appropriately give alerts instead of manually checking database

Installation:
Run Following:
``
		python3 -m pip install mysql-connector-python
		python3 -m pip install pyyaml
``

## To run cron job on Mac:

	1. Give Cron Job to run automatically on Mac:
	Follow the steps here to update System Preferences > Security & Privacy > Privacy > Full Disk Access > Add Cron Path (/usr/sbin/cron)
	https://blog.bejarano.io/fixing-cron-jobs-in-mojave/
	
	2. Run Following:
	crontab -e
	The above will open up cron scheduler, We can edit by clicking "i"

	Based on the frequency We want to run the script (take any command):
Replace the PythonPath with where Wer python3 packages are installed, this is needed because in order for python3 to know Wer modules it needs to know the site-package path
	
	Run Every Minute:
	* * * * * PYTHONPATH=/usr/local/lib/python3.9/site-packages python3 /Users/praveen1664/Documents/DataCore/Code/Support/DatabaseCheck.py
	
	Exit and save the file - Click Esc - ":wq"
	
	3. If We run into errors, We can check cron job logs by going to following:
	/private/var/mail/
	
