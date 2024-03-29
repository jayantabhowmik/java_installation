import platform
import subprocess
import sys

def install_java():
    system = platform.system()
    if system == 'Windows':
        print("Detected Windows OS.")
        install_command = 'choco install adoptopenjdk -y'  
    elif system == 'Linux':
        print("Detected Linux OS.")
        install_command = 'sudo apt-get install default-jdk -y'  
    elif system == 'Darwin':
        print("Detected macOS.")
        install_command = '/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" && brew install adoptopenjdk'
    else:
        print("Unsupported operating system.")
        return

    try:
        subprocess.run(install_command, shell=True, check=True)
        print("Java installation successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing Java: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_java()

