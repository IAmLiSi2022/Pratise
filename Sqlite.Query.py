import sqlite3;
import os;
os.removedirs
conn=sqlite3.connect("places.sqlite")
cur=conn.cursor()

cur.execute("SELECT * FROM sqlite_master")
list_index=cur.fetchall()
t=0
while t<=13:
  print("TABLE ",t," ",list_index[t][2])
  t=t+1;

cur.execute("SELECT * FROM moz_places")
raw=cur.fetchall()
i=0
while i<=13:
  print("DATA ",i," ",raw[i])
  i=i+1;