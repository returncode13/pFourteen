import re
import subprocess

TARGET_FILE = "linux-2.6.0.tar.xz"
TARGET_LINK = "http://www.kernel.org/pub/linux/kernel/v2.6/%s" % TARGET_FILE

wgetExecutable = '/usr/bin/wget'
wgetParameters = ['--progress=dot', TARGET_LINK]

wgetPopen = subprocess.Popen([wgetExecutable] + wgetParameters,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

for line in iter(wgetPopen.stdout.readline, b''):
    match = re.search(r'\d+%', line)
    if match:
        print('\b\b\b\b' + match.group(0))

wgetPopen.stdout.close()
wgetPopen.wait()