import paramiko

host = "192.168.1.8"
user = "msfadmin"
passwd = "msfadmin"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:
    stdin, stdout, stderr = client.exec_command(input("Comando: "))
    for l in stdout.readlines():
        print(l)
    print(stderr)