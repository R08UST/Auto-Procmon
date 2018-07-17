Requirement:
主机端：无额外安装项
虚拟机端：psutil

使用：
1 为虚拟机添加用户 账号 root 密码 123456 
2 在虚拟机中安装Python3(推荐位置 C盘根目录)
3 在C盘根目录下创建file文件夹，将procmon.exe,pac.py,pacv.py放入
4 在PATH中添加vmrun.exe的目录如（D:/Program Files/VMware/vmrun.exe）
5 Python host.py -m 模式 （normal/virus ）（normal 模式 数据集放在虚拟机C:file/file/  下）-c 类别（virus模式下的参数）-t 运行时间
6 病毒数据 放置于ftp下的VIRUS目录下，每一类病毒置于一个文件夹下