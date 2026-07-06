# PyDeploy CLI v1.0 Python Script
# MIT License: Copyright (c) 2026 Kevin de 3ngineer

import os
import sys
import time
import shutil
import threading
import subprocess
from getpass import getpass, getuser

# Color Palette
g = GREEN = "\033[32m"
b = BLUE = "\033[34m"
y = YELLOW = "\033[33m"
r = RED = "\033[31m"
R = RESET = "\033[0m"

print("\nPyDeploy CLI v1.0 Python Script"), print("MIT License: Copyright (c) 2026 Kevin de 3ngineer\n")
print(f"""{b}██████╗ ██╗   ██╗{y}██████╗ ███████╗██████╗ ██╗      ██████╗ ██╗   ██╗{R}     {g}██████╗██╗     ██╗    ██╗   ██╗ ██╗    ██████╗
{b}██╔══██╗╚██╗ ██╔╝{y}██╔══██╗██╔════╝██╔══██╗██║     ██╔═══██╗╚██╗ ██╔╝{R}    {g}██╔════╝██║     ██║    ██║   ██║███║   ██╔═████╗
{b}██████╔╝ ╚████╔╝ {y}██║  ██║█████╗  ██████╔╝██║     ██║   ██║ ╚████╔╝{R}     {g}██║     ██║     ██║    ██║   ██║╚██║   ██║██╔██║
{b}██╔═══╝   ╚██╔╝  {y}██║  ██║██╔══╝  ██╔═══╝ ██║     ██║   ██║  ╚██╔╝{R}      {g}██║     ██║     ██║    ╚██╗ ██╔╝ ██║   ████╔╝██║
{b}██║        ██║   {y}██████╔╝███████╗██║     ███████╗╚██████╔╝   ██║{R}       {g}╚██████╗███████╗██║     ╚████╔╝  ██║██╗╚██████╔╝
{b}╚═╝        ╚═╝   {y}╚═════╝ ╚══════╝╚═╝     ╚══════╝ ╚═════╝    ╚═╝{R}        {g}╚═════╝╚══════╝╚═╝      ╚═══╝   ╚═╝╚═╝ ╚═════╝{R}
""")

print(f"{g}kevinde3ngineer{R} - Dedicated To Running Python Applications Continuously For Raspberry PI Seamlessly With Systemd!")

# Selection
while True:
    print(f"\n{b}Py{y}Depoy{R} CLI v.1.0")

    print(f"{g}Select An Option:{R} "), print("\n[1] Control Panel"), print("[2] Set Up")
    option = input(f"\n{g}-->{R} ").strip().lower()

    # Control Panel Option
    if option in ("controlpanel", "control panel", "1"):
        # Preset
        select_a_control = f"""{g}Select A Control:{R}
        # CONTROL
        [1] --  Enable  -- startup on boot
        [2] --  Start   -- start service
        [3] --  Disable -- disable start on boot
        [4] --  Stop    -- disable service
        [5] --  Restart -- restart service

        # VIEW
        [6] --  Status  -- full report
        [7] --  Logs    -- live output
        
        # QUIT
        [Q] --  Quit    -- exit control panel"""

        # List
        ls = subprocess.run(["ls"], capture_output=True, text=True)
        ls_file = ls.stdout.split()

        # Setup
        while True:
            time.sleep(1), print(), print(ls_file) # time.sleep() is for smoother feel
            service_app = input(f"{g}Your Current Service File Name:{R} ")
            if service_app in ls_file:
                break
            else:
                print(f"\nError: Typo{r}!{R}")

        # Background Status Check (uses threading)
        status = f"{g}Status:{R} Currently Unobtainable"
        def auto_status():
            global status
            
            while True:
                active_status = subprocess.run(["sudo", "systemctl", "status", service_app], capture_output=True, text=True)
                status_text = active_status.stdout.lower()

                status = f"{g}Status:{R} 🟢" if "active (running)" in status_text else f"{g}Status:{R} 🔴"

        threading.Thread(target=auto_status, daemon=True).start()

        # Selections
        while True:
            print(), print(status), print(select_a_control)
            choice = input(f"\n{g}--->{R} ").strip().lower()
            if choice in ("enable", "1"):
                enable_check = subprocess.run(["sudo", "systemctl", "enable", service_app])
                if enable_check.returncode == 0:
                    print(f"\n{g}Successfully Enabled{R}")
                    print("[sudo systemctl enable", service_app + "]")
                else:
                    print(f"\nError: Enable Failed{r}!{R}")
                    print("[sudo systemctl enable", service_app + "]")
                subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)

            elif choice in ("start", "2"):
                start_check = subprocess.run(["sudo", "systemctl", "start", service_app])
                if start_check.returncode == 0:
                    print(f"\n{g}Successfully Started{R}")
                    print("[sudo systemctl start", service_app + "]")
                else:
                    print(f"\nError: Start Failed{r}!{R}")
                    print("[sudo systemctl start", service_app + "]")
                subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)

            elif choice in ("disable", "3"):
                disable_check = subprocess.run(["sudo", "systemctl", "disable", service_app])
                if disable_check.returncode == 0:
                    print(f"\n{g}Successfully Disabled{R}")
                    print("[sudo systemctl disable", service_app + "]")
                else:
                    print(f"\nError: Disable Failed{r}!{R}")
                    print("[sudo systemctl disable", service_app + "]")
                subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)

            elif choice in ("stop", "4"):
                stop_check = subprocess.run(["sudo", "systemctl", "stop", service_app])
                if stop_check.returncode == 0:
                    print(f"\n{g}Successfully Stopped{R}")
                    print("[sudo systemctl stop", service_app, "]")
                else:
                    print(f"\nError: Stop Failed{r}!{R}")
                    print("[sudo systemctl stop", service_app, "]")
                subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)

            elif choice in ("restart", "5"):
                restart_check = subprocess.run(["sudo", "systemctl", "restart", service_app])
                if restart_check.returncode == 0:
                    print(f"\n{g}Successfully Restarted{R}")
                    print("[sudo systemctl restart", service_app, "]")
                else:
                    print(f"\nError: Restart Failed{r}!{R}")
                    print("[sudo systemctl restart", service_app, "]")
                subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)

            elif choice in ("status", "6"):
                print(f"\n{g}Full Status:{R} ")
                subprocess.run(["sudo", "systemctl", "status", service_app])
                print(f"{g}Returning In 5 Seconds...{R}") # 5 is my arbitrary choice (change it if you want)
                time.sleep(5)

            elif choice in ("logs", "7"):
                print(f"\n{g}Logs (Press Enter To Exit):{R} ")
                log_check = subprocess.Popen(["journalctl", "-u", service_app, "-f"])
                input()
                log_check.terminate()

            elif choice in ("quit", "q"):
                print(f"\n{r}Exiting...{R}")
                time.sleep(1)
                break
            else:
                print("\nError: invalid option!")

    # Setup Option
    elif option in ("set up", "setup", "2"):
        # Setup
        apt_updated = False
        token = None
        authenticated_url = None

        # Checks for Git and installs it if it doesn't exist
        print(f"\n{g}Searching for Git...{R}")
        git_path = shutil.which("git")
        if git_path:
            git_result = subprocess.run(["git", "--version"], capture_output=True, text=True)
            print(git_result.stdout.strip()) # ".strip" is used to clean up trailing characters
        else:
            print(f"\n{g}Git Not Found: Installing Git...{R}")
            subprocess.run(["sudo", "apt", "update"], check=True)
            apt_updated = True
            subprocess.run(["sudo", "apt", "install", "-y", "git"], check=True)
            git_result = subprocess.run(["git", "--version"], capture_output=True, text=True)
            print(git_result.stdout.strip())

        # Checks for pip3 and installs it if it doesn't exist
        print(f"\n{g}Searching for Pip3...{R}")
        pip3_path = shutil.which("pip3")
        if pip3_path:
            pip3_result = subprocess.run(["pip3", "--version"], capture_output=True, text=True)
            print(pip3_result.stdout.strip())
        else:
            print(f"\n{g}Pip3 Not Found: Installing Pip3...{R}")
            if not apt_updated:
                subprocess.run(["sudo", "apt", "update"], check=True)
                apt_updated = True
            subprocess.run(["sudo", "apt", "install", "-y", "python3-pip"], check=True)
            pip3_result = subprocess.run(["pip3", "--version"], capture_output=True, text=True)
            print(pip3_result.stdout.strip())

        # Checks for venv and installs it if it doesn't exist (I'm assuming most Pi OS has it but just to make sure)
        print(f"\n{g}Searching for Venv...{R}")
        try:
            subprocess.run(["python3", "-m", "venv", "--help"], check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            venv_result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
            print(venv_result.stdout.strip())
        except subprocess.CalledProcessError: # "subprocess.CalledProcessError" is to prevent you from catching unexpected exceptions.
            print(f"\n{g}Venv Not found: Installing Venv{R}")
            if not apt_updated:
                subprocess.run(["sudo", "apt", "update"], check=True)
                apt_updated = True
            subprocess.run(["sudo", "apt", "install", "-y", "python3-venv"], check=True)
            subprocess.run(["python3", "-m", "venv", "--help"], check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            venv_result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
            print(venv_result.stdout.strip())

        # Enter your GitHub Repository here (checks for valid GitHub HTTPS URL)
        while True:
            github_repo = input(f"\n{g}GitHub Repo (HTTPS):{R} ").strip()

            if not github_repo:
                print(f"\nError: GitHub Repo Cannot Be Empty{r}!{R}")
            elif not github_repo.startswith("https://github.com/"):
                print(f"\nError: Please Enter A Valid GitHub HTTPS URL{r}!{R}")
            else:
                break

        # Verification
        os.environ["GIT_TERMINAL_PROMPT"] = "0"
        result = subprocess.run(["git", "ls-remote", github_repo], stderr=subprocess.PIPE, stdout=subprocess.DEVNULL, text=True)

        if result.returncode == 0:
            print(f"\n{g}Verification Successful{R}\n")
        else:
            error = result.stderr.lower()

            if "could not resolve host" in error:
                print(f"\nError: check your internet connection{r}!{R}")
            elif "repository not found" in error or "could not read username" in error:
                print(f"\nError: Your Repository Might Be private{r}!{R}")
                print(f"Security: Your Token Is Hidden When Typing{r}!{R}")

                while True:
                    token = getpass(f"\n{g}Paste Your Token (or 'q' to quit):{R} ").strip() # getpass is used to hide what the user types

                    if token.lower() == "q":
                        print(f"\n{r}Exiting...{R}")
                        sys.exit()

                    authenticated_url = github_repo.replace("https://", f"https://{token}@") # f strings were used here

                    retry_result = subprocess.run(["git", "ls-remote", authenticated_url], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

                    if retry_result.returncode == 0:
                        print(f"{g}\nVerification Successful{R}\n")
                        break
                    else:
                        print(f"\nError: Token Is Invalid{r}!{R}")
            else:
                print(f"\nError: Git Returned An Unexpected Response{r}!{R}")
                print(f"\n{r}Exiting in 5 seconds...{R}")
                time.sleep(5)
                sys.exit()


        # Clone Repository
        clone_repo = subprocess.run(["git", "clone", github_repo])
        if clone_repo.returncode == 0:
            print(f"\n{g}Repository Successfully Cloned{R}")
        else:
            if authenticated_url is not None:
                retry_clone = subprocess.run(["git", "clone", authenticated_url])
                if retry_clone.returncode == 0:
                    print(f"\n{g}Repository Successfully Cloned{R}")
                else:
                    print(f"\nError: Something Went Wrong On Your End{r}!{R}")
            else:
                print(f"\nError: Clone Failed, But Authentication Wasn't The Issue{r}!{R}")

        # Security: removes further variable references to these
        token = None
        authenticated_url = None

        # Looking For Dependencies In "requirements.txt"
        repo_name = github_repo.rstrip("/").split("/")[-1].replace(".git", "")
        repo_path = os.path.join(os.path.expanduser("~"), repo_name)

        # Creates a virtual environment to prevent crashes - I learned this the hard way while testing
        print(f"\n{g}Creating Virtual Environment (please wait)...{R}")
        subprocess.run(["python3", "-m", "venv", "venv"], cwd=repo_path, check=True)

        # Installs any dependencies from requirements.txt
        requirements = os.path.join(repo_path, "requirements.txt")

        if os.path.exists(requirements):
            print(f"\n{g}Requirements.txt Found: Installing Dependencies{R}")

            venv_python = os.path.join(repo_path, "venv", "bin", "python3")
            subprocess.run([venv_python, "-m", "pip", "install", "-r", "requirements.txt"], cwd=repo_path, check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

            print(f"\n{g}Dependencies Successfully Installed{R}")
        else:
            time.sleep(1)
            print(f"\n{g}No requirements.txt Found; Skipping Dependencies Installation{R}")

        # Looks for python files
        print(f"\n{g}Python File: {R}")
        python_files = []
        found=False

        for root, dirs, files in os.walk(repo_path):
            dirs[:] = [d for d in dirs if d != "venv"] # Don't look inside the venv file
            for file in files:
                if file.endswith(".py"):
                    print(file)
                    python_files.append(file)
                    found=True

        if not found:
            print(f"\nError: No Python Files were found, Please Check Your Repo{r}!{R}")
            print(f"\n{r}Exiting in 5 seconds...{R}")
            time.sleep(5)
            sys.exit()

        # Selecting python file
        while True:
            python_file = input(f"\n{g}Select A Python File (or 'q' to quit):{R} ").strip()

            if python_file.lower() == "q":
                print(f"\n{r}Exiting in 5 seconds...{R}")
                time.sleep(5)
                sys.exit()

            if python_file in python_files:
                break
            else:
                print(f"\nError: Python file Not Found, Check For Any Typos{r}!{R}")

        # Setting up service file
        service_name = input(f"\n{g}Service Name:{R} ")

        # Creating service file
        service = f"""[Unit]
        Description={repo_name} Python Script
        After=multi-user.target

        [Service]
        User={getuser()}
        WorkingDirectory={repo_path}
        ExecStart={repo_path}/venv/bin/python3 {repo_path}/{python_file}
        Restart=always
        RestartSec=5

        [Install]
        WantedBy=multi-user.target
        """
        service_file = service_name + ".service"
        with open(service_file, "w") as file:
            file.write(service)

        print(f"\n{g}{service_file} Created Successfully!{R}")

        # Add service file into systemcd
        subprocess.run(["sudo", "cp", service_file, f"/etc/systemd/system/{service_file}"])

        # Reload service definitions
        print(f"\n{g}Reloading Systemd Service Definitions...{R}")
        subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)

        # Enable the service for startup on boot:
        while True:
            print(f"\n{g}Enable On Boot?:{R} "), print("\n[1] Yes"), print("[2] No")
            enable = input(f"\n{g}--->{R} ").strip().lower()

            if enable in ("yes", "1"):
                print(f"\nEnabling On Boot...")
                subprocess.run(["sudo", "systemctl", "enable", service_file], check=True)
                subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
                break
            elif enable in ("no", "2"):
                break
            else:
                print(f"\nError: Invalid Option{r}!{R}")

        # Start the service
        while True:
            print(f"\n{g}Start Service?:{R}"), print("\n[1] Yes"), print("[2] No")
            enable = input(f"\n{g}--->{R} ").strip().lower()

            if enable in ("yes", "1"):
                print("\nStarting In Background...")
                subprocess.run(["sudo", "systemctl", "start", service_file], check=True)
                subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
                break
            elif enable in ("no", "2"):
                break
            else:
                print(f"\nError: Invalid Option{r}!{R}")
        
        while True:
            print(f"\n{g}Go Back To Main Menu?:{R}"), print("\n[1] Yes"), print("[2] No")
            enable = input(f"\n{g}--->{R} ").strip().lower()

            if enable in ("yes", "1"):
                break
            elif enable in ("no", "2"):
                print(f"\n{r}Exiting in 5 seconds...{R}")
                time.sleep(5)
                sys.exit()
            else:
                print(f"\nError: Invalid Option{r}!{R}")

    # Error Option
    else:
        print(f"\nError: Invalid Option{r}!{R}")