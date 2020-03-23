import subprocess

a = open('a/as1.bat').read()
print(a)
subprocess.run(a, check=True, shell=True, cwd='a')