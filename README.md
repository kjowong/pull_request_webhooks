# Trigger a webhook for pull requests

This repo's purpose is to trigger a webhook on a server upon opened or closed ​Pull Requests​ where information about the pull request is then saved onto a file. This code was done as a challenge for a Junior SRE position with a 2 hour timelimit. 

## How to use

### Installation Requirements

 ``` sudo apt-get update
     sudo apt-get unzip
     sudo apt-get install unzip
     wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
     unzip ngrok-stable-linux-amd64.zip
     sudo apt-get install python3
     sudo apt-get install python3-pip
     pip3 install Flask  
```

#### Run Ngrok to connect to Github Webhooks
`  ./ngrok http 80`

#### Start Python Flask App
` python3 webhooks.py`
 
#### File Expected Output

- State of PR (“open” or “closed”)
- Time and date in epoch time
- Number of the pull request (GitHub will assign a sequential number to pull requests)
- Username of user who submitted the pull request  
- Name of the head branch of the pull request

#### To do:
- [ ] Handle errors
- [ ] Survive reboot with systemd
- [ ] Update variable names
- [ ] Create script to install requirements
- [ ] Format text output
#### Notes:
- Webhook app does not handle errors
- Service does not surive reboot
- Does not include application tests
