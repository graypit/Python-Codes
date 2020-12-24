# DNS Manager via Python and PowerShell
## Python and PowerShell Together :sunglasses:
<img src="https://image.flaticon.com/icons/png/512/1183/1183595.png" width="100">
<img src="https://cdn.educba.com/academy/wp-content/uploads/2018/12/PowerShell-Vs-Python.jpg" width="300">

In this article I'll show you how to `Create`/`Remove`/`Update` and `Get` DNS A Record in Windows Server (AD/DNS)

After researching for a while, I found that we needed a cross platform solution.

## What should I Do before executing?
### Configure your WinRM Service into Windows Server
### Install Python Libraries:
For Python 2.7 :
```bash
$ pip install --user pywinrm jinja2
```
For Python3 or high :
```bash
$ pip3 install --user pywinrm jinja2
```
### Set your Windows Server Credentials in `.credentials` file
### Check your Connection to Windows Server:
```bash
$ ./DNS-Manager.py check
# You'll get Windows Server hostname and ifconfig commands output
```
## How to Install ?
Just clone the repo and execute the `DNS-Manager.py` script

For extra information just execute the following command:
```bash
$ ./DNS-Manager.py --help
```

## Some Examples:
### Create New A Record `testapp` into zone `graypit.local`  with `192.168.5.44` IP Address:
```bash
$ ./DNS-Manager.py create --name testapp --zone graypit.local --ip 192.168.5.44
```
### Update `testapp` A Record's IP Address to `192.168.5.88`:
```bash
$ ./DNS-Manager.py update --name testapp --zone graypit.local --ip 192.168.5.88
```
### Delete `testapp` A record into zone `graypit.local`:
```bash
$ ./DNS-Manager.py remove --name testapp --zone graypit.local
```
### Get All records in zone `test.local`:
```bash
$ ./DNS-Manager.py get --zone test.local
```
### Get `test-devops-awesome` record into zone `graypit.local`
```bash
$ ./DNS-Manager.py get --name test-devops-awesome --zone graypit.local
```
### Get all logs:
```bash
$ ./DNS-Manager.py logs
# This parameter read file dns-results.log that will created after first action
```
### Requirement: Python2.7 or higher

Useful Documentations:

https://github.com/diyan/pywinrm

https://adamtheautomator.com/powershell-dns/

https://adamtheautomator.com/python-winrm/
