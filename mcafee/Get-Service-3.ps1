#This script is used to post the status of McAfee Firewall service to API

$status=Get-Service | where-object {$_.DisplayName -match 'mcafee firewall'}

$date=Get-Date -Format "MM/dd/yyyy HH:mm:ss"

$json=@{
    Date=$date
    Service_Name=$status.Name
    Display_Name=$status.DisplayName
    Status=$status.Status
}

$final_data="["
$final_data+=$json | ConvertTo-Json
$final_data+="]"

Write-Host "Data Sent : $final_data"

Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/firewall" -Method Post -Body $final_data -ContentType "application/json"