import subprocess

def check_output(command, text):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        return text in output
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


command = "ls"
text = "nginx.list"
res = check_output(command, text)
print(res)