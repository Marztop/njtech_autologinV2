import paramiko   
# 实例化SSHClient  
ssh_client = paramiko.SSHClient()   
# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接 ，此方法必须放在connect方法的前面
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
# 连接SSH服务端，以用户名和密码进行认证 ，调用connect方法连接服务器
ssh_client.connect(hostname='192.168.1.1', port=22, username='root', password='admin')   
# 打开一个Channel并执行命令  结果放到stdout中，如果有错误将放到stderr中
#stdin, stdout, stderr = ssh_client.exec_command('df -hT ')
# stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
'''while True:
    command=input()
    if command=='quit paramiko':
        break
    else:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))'''
stdin, stdout, stderr = ssh_client.exec_command('cd /sbin/;./ifup wan')
'''
if stdout.read():
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))
'''
# 打印执行结果  print(stdout.read().decode('utf-8'))
# 关闭SSHClient连接 
ssh_client.close()