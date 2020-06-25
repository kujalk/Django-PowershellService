#This script is used to post the status of McAfee Firewall service to API

try 
{
    $status=Get-Service | where-object {$_.DisplayName -match 'mcafee firewall'}

    $date=Get-Date -Format "MM/dd/yyyy HH:mm:ss"
    
    #Create new object
    $Psobj=New-Object -Type psobject

    $Psobj | Add-Member -MemberType NoteProperty -Name Date -Value $date -Force
    $Psobj | Add-Member -MemberType NoteProperty -Name Service_Name -Value $status.Name -Force
    $Psobj | Add-Member -MemberType NoteProperty -Name Display_Name -Value $status.DisplayName -Force
    $Psobj | Add-Member -MemberType NoteProperty -Name Status -Value $status.Status -Force

    $final_data="["
    $final_data+=$Psobj | ConvertTo-Json
    $final_data+="]"

    Invoke-RestMethod -uri "http://127.0.0.1:8000/api/firewall" -Method Post -Body $final_data -ContentType "application/json"
}

catch 
{
    Write-Host "Error in POSTing data to API endpoint $_" -Type Error
}
