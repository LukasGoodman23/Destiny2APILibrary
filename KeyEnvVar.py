''' 
simple python script to streamline the process of creating a secure windows user
environment variable

this script needs to be run from a admin powershell in order to have permission to 
set the system environment variable
'''
import os

key= input("Paste your Key Here: ")
os.system("SETX {0} {1} /M".format("BungieAPIKey", key))