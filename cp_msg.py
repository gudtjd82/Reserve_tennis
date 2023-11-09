import sqlite3
import os
import re
import subprocess

def cp_msg():
    # 인증번호 복사
    conn = sqlite3.connect(os.environ['HOME'] + '/Library/Messages/chat.db')
    cur = conn.cursor()

    latest_rowid = None

    while True:
        cur.execute("select rowid, text from message order by date desc limit 1")

        rowid, text = cur.fetchone()

        if latest_rowid is None:
            latest_rowid = rowid
        
        if latest_rowid != rowid:
            latest_rowid = rowid
            numbers = re.findall(r'\d{4,6}', text)
            if len(numbers) == 1:
                number = numbers[0]
                process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
                process.communicate(number.encode('utf-8'))
                break