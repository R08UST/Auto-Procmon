import subprocess
import sys
import time
from ftplib import FTP
import argparse
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', '-m',
						default='normal',
                        dest='mode',
                        help='Output directory. If directory doesn\'t exist it will be created.')
    parser.add_argument('--class', '-c',
						default='',
                        dest='clas',
                        help='Output directory. If directory doesn\'t exist it will be created.')
    parser.add_argument('--user', '-u',
                        default='root',
                        dest='usr',
                        help='Path to training data file (one password per line) (default: data/train.txt)')

    parser.add_argument('--pass', '-o',
                        default='123456',
                        dest='pas',
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
'''if len(sys.argv)!=1:
	usr=sys.argv[1]
	pas=sys.argv[2]
	dir=sys.argv[3]
	tim=sys.argv[4]
	tims=sys.argv[5]
usr='root'
pas='123456'
dir="D:\Program Files\VMware\ISO\Windows XP Professional\Windows XP Professional.vmx"
tim='10' '''
args=parse_args()
usr=args.usr
pas=args.pas
dir=args.dir
tim=args.time
def normal():
	back=subprocess.Popen(["vmrun",'listSnapshots',dir],stdout=subprocess.PIPE)
	if chr(back.stdout.read()[17])=='0':
			print("create snap shot")
			vm=subprocess.Popen(["vmrun","snapshot",dir,'sp'],stdout=subprocess.PIPE)
			print(vm.stdout.read())
	vm=subprocess.Popen(["vmrun","list"],stdout=subprocess.PIPE)
	if chr(vm.stdout.read()[19])=='0':
		print("open the vm")
		vm=subprocess.Popen(["vmrun","-T",'ws','start',dir],stdout=subprocess.PIPE)
		print(vm.stdout.read())
		time.sleep(20)
	pg=subprocess.Popen(["vmrun","-T",'ws',"-gu",usr,"-gp",pas,"runProgramInGuest",dir,'C:\Python\python.exe','C:/file/cap.py','-t',tim],stdout=subprocess.PIPE)
	print(pg.stdout.read())
	back=subprocess.Popen(["vmrun","-T",'ws',"revertToSnapshot",dir,'sp'],stdout=subprocess.PIPE)
	print(back.stdout.read())
	print('OK!')
def virus():
	ftp=FTP()
	ftp.connect("144.202.7.166",21)
	ftp.login("app","741236985")
	ftp.cwd("~/VIRUS/"+args.clas)
	for virus in ftp.nlst():
		vm=subprocess.Popen(["vmrun","list"],stdout=subprocess.PIPE)
		if chr(vm.stdout.read()[19])=='0':
			back=subprocess.Popen(["vmrun",'listSnapshots',dir],stdout=subprocess.PIPE)
			if chr(back.stdout.read()[17])=='0':
				print("create snap shot")
				vm=subprocess.Popen(["vmrun","snapshot",dir,'sp'],stdout=subprocess.PIPE)
				print(vm.stdout.read())
			print("open the vm")
			vm=subprocess.Popen(["vmrun","-T",'ws','start',dir],stdout=subprocess.PIPE)
			#print(vm.stdout.read())
			time.sleep(60)

		print(virus)
		pg=subprocess.Popen(["vmrun","-T",'ws',"-gu",usr,"-gp",pas,"runProgramInGuest",dir,'C:\Python\python.exe','C:/file/capV.py','-t',tim,'-d',args.clas,'-f',virus],stdout=subprocess.PIPE)
		print(pg.stdout.read())
		back=subprocess.Popen(["vmrun","revertToSnapshot",dir,'sp'],stdout=subprocess.PIPE)
		print(back.stdout.read())
		print('OK!')
		time.sleep(20)
if args.mode=="normal":
	normal()
elif args.mode=="virus":
	virus()
