#-------------------------------------------------------------------------------
# Name:        Microsoft-.NET-8.0-SDK-Installer-for-Ubuntu 
# Purpose:     Auto-install Microsoft-.NET-8.0-SDK-Installer-for-Ubuntu 
#
# Author:      ReforgedSystems OU
#
# Created:     13/03/2024
# Copyright:   (c) ReforgedSystems OU 2024
# Licence:     MIT licence
#-------------------------------------------------------------------------------
import os
import getpass

def install_dotnet_sdk():
    # Import the Microsoft repository GPG key
    os.system("wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.asc.gpg")
    os.system("sudo mv microsoft.asc.gpg /etc/apt/trusted.gpg.d/")

    # Add the Microsoft package repository
    os.system("sudo sh -c 'echo \"deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-focal-prod focal main\" > /etc/apt/sources.list.d/dotnetdev.list'")
    
    # Update the package cache
    password = getpass.getpass(prompt="Enter your password: ")
    command = f"echo {password} | sudo -S apt-get update"
    os.system(command)
    
    # Install the .NET SDK
    command = f"echo {password} | sudo -S apt-get install -y dotnet-sdk-8.0"
    os.system(command)

if __name__ == "__main__":
    install_dotnet_sdk()
