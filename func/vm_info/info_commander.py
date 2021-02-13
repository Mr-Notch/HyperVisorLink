# -- coding: utf-8 --
import subprocess
import Injector
sys_path=Injector.getSysLocation()
def vm_info_getPowerStatus(vmname):
    output = subprocess.Popen(['powershell.exe', sys_path+"func/vm_info/info_getPowerStatus.ps1" + ' ' + vmname], stdout=subprocess.PIPE)
    dt = output.stdout.read().decode().replace(" ","")

    popen_call = subprocess.call
    if popen_call == 0:
        return False
    else:
        return dt

def vm_info_getAddress(vmname):
    output = subprocess.Popen(['powershell.exe', sys_path+"func/vm_info/info_getAddress.ps1" + ' ' + vmname], stdout=subprocess.PIPE)
    dt = output.stdout.read().decode().replace(" ","")

    popen_call = subprocess.call
    if popen_call == 0:
        return False
    else:
        return dt

<<<<<<< HEAD
def vm_info_getAddressIfVMStarted(vmname):
    output = subprocess.Popen(['powershell.exe', sys_path+"func/vm_info/info_getAddressIfVMStarted.ps1" + ' ' + vmname], stdout=subprocess.PIPE)
    dt = output.stdout.read().decode().replace(" ","")

    popen_call = subprocess.call
    if popen_call == 0:
        return False
    else:
        return dt

=======
>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006
def vm_info_getAllVM():
    output = subprocess.Popen(['powershell.exe', sys_path+"func/vm_info/info_getAllVM.ps1"], stdout=subprocess.PIPE)
    dt = output.stdout.read().decode().replace(" ","")

    popen_call = subprocess.call
    if popen_call == 0:
        return False
    else:
        return dt

def vm_info_getVMID(vmname,vmloc):
    output = subprocess.Popen(['powershell.exe', sys_path+"func/vm_info/info_getVMID.ps1" + ' ' + vmname + ' ' + vmloc], stdout=subprocess.PIPE)
    dt = output.stdout.read().decode().replace(" ","")

    popen_call = subprocess.call
    if popen_call == 0:
        return False
    else:
        return dt