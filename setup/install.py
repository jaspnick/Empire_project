import os
file_name = 'ez_setup.py'
from urllib import urlopen
data = urlopen('http://peak.telecommunity.com/dist/ez_setup.py')
with open(file_name, 'wb') as f:
    f.write(data.read())
os.system('python %s' % (os.path.join(os.getcwd(),file_name)))

os.system('eaay_install pip')


data = urlopen('https://github.com/saltstack/salt-windows-install/blob/master/deps/win-amd64-py2.7/M2Crypto-0.21.1.win-amd64-py2.7.exe?raw=true')
with open(file_name, 'wb') as f:
    f.write(data.read())
os.system( os.path.join(os.getcwd(),file_name) )

os.system('pip install pyreadline')