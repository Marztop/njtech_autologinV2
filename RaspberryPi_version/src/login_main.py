debug_mode = False


import paramiko
import autologin
import time


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.1.1', port=22, username='root', password='admin')

def send_command(command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    if debug_mode == True:
        try:
            if stdout.read():
                print(stdout.read().decode('utf-8'))
            else:
                print(stderr.read().decode('utf-8'))
        except Exception:
            print(Exception)
    time.sleep(1)

#send_command('cd /sbin/;./ifup wan')

if __name__ == '__main__':
    send_command('cd /sbin/;./ifup wan')
    send_command('cd /sbin/;./ifdown wan2')
    send_command('cd /sbin/;./ifdown wan3')
    autologin.main()

    send_command('cd /sbin/;./ifdown wan')
    send_command('cd /sbin/;./ifup wan2')
    autologin.main()

    send_command('cd /sbin/;./ifdown wan2')
    send_command('cd /sbin/;./ifup wan3')
    autologin.main()

    send_command('cd /sbin/;./ifup wan')
    send_command('cd /sbin/;./ifup wan2')
    send_command('cd /usr/sbin;./mwan3 stop')
    send_command('cd /usr/sbin;./mwan3 start')
    send_command('cd /usr/sbin;./mwan3 restart')

ssh_client.close()