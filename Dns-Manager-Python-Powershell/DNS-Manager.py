#!/usr/bin/env python
#===============================================================================
#
#          FILE:  DNS-Manager.py
#
#         USAGE:  DNS-Manager.py --help
#
#   DESCRIPTION:  Python script to manage DNS Server via PowerShell
#
#       OPTIONS:  ---
#  REQUIREMENTS:  Clear Mind :)
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Habib Guliyev (), graypit@gmail.com
#       VERSION:  4.0
#       CREATED:  12/24/2020 14:17:44 PM +04
#      REVISION:  ---
#===============================================================================
import os
import imp
import winrm
import logging
import argparse
from jinja2 import Template
# Global Variable:
PowerShellScriptPath = 'Templates/DnsFunctions.ps1'
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', filename='dns-results.log', level=logging.INFO)
# Get Param List
ParseFromArgs = argparse.ArgumentParser()
ParseFromArgs.add_argument('mode', help="Script WorkMode", action="store")
ParseFromArgs.add_argument("-n", "--name", help="Set DNS Record Name", action="store", dest="RecordName")
ParseFromArgs.add_argument("-z", "--zone", help="Set DNS Zone Name", action="store", dest="RecordZone")
ParseFromArgs.add_argument("-ip", "--ip-address", help="Set Record IP Address", action="store", dest="RecordIp")
# Read arguments from the command line
args = ParseFromArgs.parse_args()
def MainSelector():
    if args.mode == 'check':
        logging.info('WinRM service availability check')
        RenderTemplates('CheckConnection')
    elif args.mode == 'create':
        logging.info('Created A record ' + args.RecordName + ' into zone: ' + args.RecordZone + ' with ' + args.RecordIp + ' DNS: ' + args.RecordName + '.' + args.RecordZone )
        RenderTemplates('AddRecord')
    elif args.mode == 'remove':
        logging.info('Removed A record ' + args.RecordName + ' into zone: ' + args.RecordZone + ' with ' + args.RecordIp + ' DNS: ' + args.RecordName + '.' + args.RecordZone )
        RenderTemplates('RemoveRecord')
    elif args.mode == 'update':
        logging.info('Updated A record ' + args.RecordName + ' into zone: ' + args.RecordZone + ' with ' + args.RecordIp + ' DNS: ' + args.RecordName + '.' + args.RecordZone )
        RenderTemplates('UpdateRecord')
    elif args.mode == 'logs':
        with open("dns-results.log","r") as logfile: print logfile.read()  
    else:
        ConnectToWinRM(args.mode)
def GetCredetials(filename):
    f = open(filename)
    global config
    config = imp.load_source('data', '', f)
    f.close()
def RenderTemplates(JobMode):
    with open(PowerShellScriptPath) as file_:
        template = Template(file_.read())
    PowerShellScript = template.render(WhatToDo=JobMode,recordname=args.RecordName,zonename=args.RecordZone,ipaddress=args.RecordIp)
    ConnectToWinRM(PowerShellScript)
def ConnectToWinRM(PS_Script):
    # Path to Credentials file:
    GetCredetials('.credentials')
    # Try/Initiate connection to Windows
    Session = winrm.Session(config.WinMachine, auth=('{}@{}'.format(config.WinRmUsername,config.WinDomainName), config.WinRmPassword), transport='ntlm')
    # Run PowerShell:
    if PS_Script == 'get':
        if args.RecordName:
            logging.info('Get info about record: ' + args.RecordName + ' into zone: ' + args.RecordZone )
            print('DNS Name: ' + args.RecordName + '.' + args.RecordZone )
            ExecutePowerShell = Session.run_ps("Get-DnsServerResourceRecord -ZoneName " + args.RecordZone + " -Name " + args.RecordName )
        else:
            logging.info('Get info about all records into zone: ' + args.RecordZone )
            ExecutePowerShell = Session.run_ps("Get-DnsServerResourceRecord -ZoneName " + args.RecordZone)
    else:
        ExecutePowerShell = Session.run_ps(PS_Script)
    print(ExecutePowerShell.std_out)
    if os.path.isfile('c'):
        os.unlink('c')
MainSelector()
