import os
os.system('docker cp find3_find3_1:/data/data/xUq8pGzb.sqlite3.db /home/pte2/sqlite3/oil230-data.sqlite3.db')
os.system('sqlite3mysql -f /home/pte2/sqlite3/oil230-data.sqlite3.db -d "find3" -u "find3" -p "Lekkerhoor12@" -h "10.10.1.12"')