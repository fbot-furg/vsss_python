import redis

def ball():
    r = redis.Redis(host='localhost', port=6379, db=0)
    x = r.get("BALL_X")
    y = r.get("BALL_y")
    return ([float(x),float(y)])

def yellow_car(id):
    r = redis.Redis(host='localhost', port=6379, db=0)
    if id == 0:
        x = float(r.get("yellow_0_x"))
        y = float(r.get("yellow_0_y"))
        o = float(r.get("yellow_0_y"))
        return ([float(x),float(y),float(o)])

    if id == 1:
        x = r.get("yellow_1_x")
        y = r.get("yellow_1_y")
        o = r.get("yellow_1_y")
        return ([x,y,o])

    if id == 2:
        x = r.get("yellow_2_x")
        y = r.get("yellow_2_y")
        o = r.get("yellow_2_y")
        return ([x,y,o])

def blue_car(id):
    r = redis.Redis(host='localhost', port=6379, db=0)
    if id == 1:
        x = r.get("bleu_0_x")
        y = r.get("blue_0_y")
        o = r.get("blue_0_y")
        return ([x,y,o])

    if id == 1:
        x = r.get("blue_1_x")
        y = r.get("blue_1_y")
        o = r.get("blue_1_y")
        return ([x,y,o])

    if id == 2:
        x = r.get("blue_2_x")
        y = r.get("blue_2_y")
        o = r.get("blue_2_y")
        return ([x,y,o])
