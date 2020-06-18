import mysql.connector
#----------------------------
db = mysql.connector.connect(
    host='localhost',
    user='daniel', 
    passwd='daniel',
    database = 'ScoreInfo')

mycursor = db.cursor()
#----------------------------
sc = 0


class Person():
    def __init__(self, name, num):
        self._name = name
        self._won = False
        self._value = num
        return 


def set_score(p, inc):
    p._value = get_score(p)
    p._value += inc 

    sql = """UPDATE discordbotinfo SET Score = %s WHERE Name = %s"""
    param = (p._value,p._name)
    mycursor.execute(sql,param)
    db.commit()

   
    return
def get_score(p):
    global sc
  
    sql = """SELECT Score From discordbotinfo where Name = %s"""
    param = (p._name,)
    
    mycursor.execute(sql,param)
    result = mycursor.fetchall()
    
    
    if result !=[]:
        
        sc = result[0][0]
    elif result == []:
        
        sql = """INSERT INTO discordbotinfo (Score, Name) VALUES (%s,%s)"""
        param = (0, p._name)
        
        mycursor.execute(sql,param)
        db.commit()

        

        get_score(p)


    return sc
