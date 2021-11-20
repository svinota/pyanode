import sys
import logging
import base64
import inspect
import subprocess


def stream():
    while True:
        data = sys.stdin.readline()
        if not data:
            break
        exec(data)


def main(target, python):
    code = inspect.getsource(stream)
    b64c = base64.b64encode(code.encode())
    cmd = ['ssh',
           target,
           '''
           %s -c "import os,sys,base64; exec(base64.b64decode(%s).decode()); stream()"
           ''' % (python, b64c)]
    ssh = subprocess.Popen(cmd,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)
    ssh.stdin.write(b'print(os.uname())\nsys.stdout.flush()\n')
    ssh.stdin.flush()
    print(ssh.stdout.readline().decode())


main('localhost', 'python')
