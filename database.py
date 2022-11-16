dataset=[{'uid':'1','id':'user1','pw':"1234"},
         {'uid':'2','id':"user2",'pw':"5678"},
         {'uid':'3','id':"admin",'pw':"admin"},
         {'uid':'4','id':"host",'pw':"host"}]


def getKey(key):
    for i in dataset:
        print('i= ',i)
        if key==i['id']:
            return True
    return False

def getValue(value):
    for i in dataset:
        if value==i['pw']:
            return True
    return False

