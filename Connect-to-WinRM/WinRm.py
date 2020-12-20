#!/bin/python
# Author: Habib Guliyev 12.17.2020
import winrm
# Global Variables:
WinMachine = 'ad1.graypit.local'
WinDomainName = 'graypit.local'
WinRmUsername = 'winrmuser' # Must be Administrator
WinRmPassword = 'strongpass'
# Try/Initiate connection to Windows
session = winrm.Session(WinMachine, auth=('{}@{}'.format(WinRmUsername,WinDomainName), WinRmPassword), transport='ntlm')
# Run command in PowerShell:
result = session.run_ps("hostname")
#result = session.run_ps('Get-Acl')
print(result.std_out)
# Run commain in Windows Command Prompt:
#result = session.run_cmd('ipconfig', ['/all'])
#print(result.std_out)