import getpass
import subprocess
import os
from colorama import Fore, Style

def change_password():
    print(Fore.BLUE + Style.BRIGHT + f"[[[KALI STARTUP_LOGIN_SCREEN_PASSWORD CHANGING SCRIPT MADE BY CRITICAL]]]\n" + Style.RESET_ALL)
    username = input("Enter the username: ")
    new_password = getpass.getpass(prompt="Enter the new password: ")

    try:
        uid = os.getuid()
        if uid == 0:
            p = subprocess.Popen(['su', '-', '-c', f'passwd {username}'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            print(Fore.RED + Style.BRIGHT + "Error: Run the script as root user (e.g., using 'sudo').\n" + Style.RESET_ALL)
            return

        p.communicate(input=f'{new_password}\n{new_password}\n'.encode())
        
        if p.returncode == 0:
            print("Password changed successfully!")
        else:
            if uid == 0:
                print(f"Error: Password change failed for user '{username}' when running as root.")
            else:
                print("Error: Password change failed.")
    except subprocess.CalledProcessError:
        print("Error: Password change failed.")

if __name__ == '__main__':
    change_password()
