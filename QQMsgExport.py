#!/usr/bin/env python
#coding=utf-8
import sqlite3
import time
import string

def datetime_trans(dt):
        x=time.localtime(dt)
        s = time.strftime('%Y-%m-%d %H:%M:%S',x)
        return s

class Msg:
    def copyData(self) :
        conn = sqlite3.connect('QQ.db')
        cur = conn.execute("SELECT time,flag,content FROM 'tb_c2cMsg_1483712819' ORDER BY 'time' ASC")
        rows = cur.fetchall()
        file = open(u"xxx和xxx的聊天记录.txt","w");
        Baby = u" xxx".encode("utf-8")
        Bro = u" xxx".encode("utf-8")
        for row in rows:
            time = datetime_trans(row[0])
            flag=row[1]
            content = row[2].encode("utf-8")
            if(flag == 1):
                file.write(time)
                file.write(Bro)
                file.write("\n")

            else:
                file.write(time)
                file.write(Baby)
                file.write("\n")
            file.write(content)
            file.write("\n\n")
msg = Msg()
msg.copyData()
