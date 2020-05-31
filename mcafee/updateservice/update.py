import subprocess,sys

def execute_powershell():
    execute=subprocess.Popen(["powershell.exe","D:\\Django_Dev\\api-powershell\\mcafee\\Get-Service.ps1"],stdout=sys.stdout)
    execute.communicate()