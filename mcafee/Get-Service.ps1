#This script is used to post the status of McAfee Firewall service to API

$status=Get-Service | where-object {$_.DisplayName -match 'mcafee firewall'}

$date=Get-Date -Format "MM/dd/yyyy HH:mm:ss"
Write-Host "Ans: $($status.DisplayName)"
$json=@"
[{
    "Date":"$date",
    "Service_Name":"$($status.Name)",
    "Display_Name":"$($status.DisplayName)",
    "Status":"$($status.Status)"
}]
"@

Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/firewall" -Method Post -Body $json -ContentType "application/json"