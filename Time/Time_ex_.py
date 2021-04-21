import time
t=time.time()#return the quantity of seconds from 1970.1.1
time.sleep(1)#stop the program on quantity of sec in function
t_local=time.localtime()#return local time by the host on which installed
t_gmt=time.gmtime()#return local time by the host on which installed in GMT(Grinwich)
t_as_string=time.asctime()#return current and local time as string
t_ctime=time.ctime()#return current and local time as string
print(f"{t}\n{t_local}\n{t_gmt}\n{t_as_string}\n{t_ctime}")
