# Author: Habib Guliyev 12.24.2020
# Global Variables:
$RecordName = '{{ recordname }}'
$ZoneName = '{{ zonename }}'
$IpAddress = '{{ ipaddress }}'
# Global Functions:
function Preparation() {
        write-host 'Successfully Connected to Windows Server'
        {{ WhatToDo }}
}
function CheckConnection() {
        hostname
        ipconfig 
}
function AddRecord() {
        Add-DnsServerResourceRecordA -Name "$RecordName" -ZoneName "$ZoneName" -AllowUpdateAny -IPv4Address "$IpAddress" -TimeToLive "00:00:10"
        write-host "Success! Record was added: $recordname.$zonename redirected to $ipaddress"
}
function RemoveRecord() {
        Remove-DnsServerResourceRecord -ZoneName "$ZoneName" -Name "$RecordName" -RRType A -Force
        write-host "Success! Record was removed: $recordname.$zonename"
}
function UpdateRecord(){
	$oldobj = get-dnsserverresourcerecord -name $RecordName -zonename $ZoneName -RRType A
	$newobj = get-dnsserverresourcerecord -name $RecordName -zonename $ZoneName -RRType A
	$newobj.recorddata.ipv4address=[System.Net.IPAddress]::parse($IpAddress)
	Set-dnsserverresourcerecord -newinputobject $newobj -oldinputobject $oldobj -zonename $ZoneName -passthru
    	write-host "Success! Record was updated: $recordname.$zonename redirected to $ipaddress"
}
Preparation
