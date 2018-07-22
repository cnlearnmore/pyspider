import MySQLdb
import random

if __name__ == '__main__':
    db = MySQLdb.connect('localhost','root','root','wenda',charset='utf8')
    try:
        cursor = db.cursor()
        sql = 'insert into question(title, content, user_id, created_date, comment_count) values("%s","%s","%d","%s","%d")' % ('title', 'content',random.randint(1, 10),'now()', 0);
        cursor.execute(sql)
        qid = cursor.lastrowid
        db.commit()
        print qid
    except Exception, e:
        print e
        db.rollback()
    db.close()
