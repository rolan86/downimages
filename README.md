# downimages
Download images and serve via a webserver

1. Download this git repository to your local system which contains python, pip
2. Create a virtualenv by any name you like and activate it
3. Once the virtualenv has been activated, run the following commands:
    a. cd downloadimages
    b. pip install -r initial_reqs.txt
4. In the hosts file under [remote] add the any server ip you would like to run the script on.
5. Run the following commands:
    a. ansible -i ./hosts --ask-pass --ssh-extra-args='-o "PubkeyAuthentication=no"' remote -m ping
    b. ansible-playbook -i ./hosts install.yml
    The command a. will ask for the server password, please enter that so as to authenticate the servers
    The command b. will install all the requirements, copy the files necessary, and start up the webserver.
6. The webserver will start up through cron and the download and scraping will happen through cron as well.

Note.: Currently the python downloader.py script has been fed with urls.txt file in the ansible install.yml playbook.
If you need to change the file name, change at the appropriate places in the install.yml playbook.

This install.yml file is currently being worked upon to include dynamic update of the url files.

The images will be served at <server_ip>:5000
