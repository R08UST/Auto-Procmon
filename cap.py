
import sys,os,signal
import subprocess 
import time
import codecs
import csv
import psutil
import argparse
from ftplib import FTP
ftp=FTP()
ftp.connect("144.202.7.166",21)
ftp.login("app","741236985")
ftp.cwd("~/data/")
def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--path', '-p',
                        default='C:/file/file/',
                        dest='path',
                        help='Path to training data file (one password per line) (default: data/train.txt)')

    parser.add_argument('--log', '-l',
                        default='C:/file/log/',
                        dest='log',
                        help='Output directory. If directory doesn\'t exist it will be created.')

    parser.add_argument('--dir', '-d',
                        default='D:\Program Files\VMware\ISO\Windows XP Professional\Windows XP Professional.vmx',
                        dest='dir',
                        help='Output directory. If directory doesn\'t exist it will be created.')

    parser.add_argument('--time', '-t',
                        default='10',
                        dest='time',
                        help='Output directory. If directory doesn\'t exist it will be created.')

    return parser.parse_args()
def is_pe(file):
	if not os.path.isfile(file): 
		print(file + ' is not file.')
		return False
	with open(file, 'rb') as fp:
		flag1 = fp.read(2) 
		fp.seek(0x3c)
		offset = ord(fp.read(1))
		fp.seek(offset)
		flag2 = fp.read(4) 
	if flag1==b'MZ' and flag2==b'PE\x00\x00': 
		return True
	else:
		return False
args=parse_args()
'''path="C:/file/file/"
log="C:/file/log/"
files= os.listdir(path)
tim=sys.argv[1]'''
path=args.path
log=args.log
dir=args.dir
files= os.listdir(path)
tim=args.time
for file in files:
	if not is_pe(path+file):
		print(file)
		continue
	procmon=subprocess.Popen(["C:/file/Procmon.exe", "/AcceptEula","/quiet","/backingfile","C:/file/back.pml"],close_fds=True)
	time.sleep(10)
	proc=subprocess.Popen (path+file,close_fds=True)
	time.sleep(int(tim))
	proc.kill()
	for pid in psutil.pids():
		if not psutil.pid_exists(pid):
			break
		p = psutil.Process(pid)
		if p.name()=="Procmon64.exe":
			print(p.name())
			subprocess.call("taskkill /PID %i"%pid, close_fds=True)
			time.sleep(20)
			break
		elif p.name()=="Procmon.exe":
			print(p.name())
			subprocess.call("taskkill /PID %i"%pid, close_fds=True)
			time.sleep(20)
			break
	procmon=subprocess.call(["C:/file/Procmon.exe", "/AcceptEula","/quiet","/openlog","C:/file/back.pml","/saveas","C:/file/logs.csv"],close_fds=True)
	_in=codecs.open("C:/file/logs.csv","r+","utf-8")
	out=open(log+file+".csv","w+")
	source=csv.reader(_in)
	writer=csv.writer(out)
	for line in source:
		if(line[1]==file):
			print(line)
			writer.writerow(line)
	_in.close()
	out.close()
	out=open(log+file+".csv","rb")
	ftp.storbinary('STOR %s ' % file+".csv",out)
	out.close()
	os.remove("C:/file/back.pml")
	os.remove("C:/file/logs.csv")
exit(8848)

	
	
