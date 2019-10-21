from Flask import jsonify

@app.route('/')
@app.route('/API-Kalender-Hari-Besar', method = ['GET', 'POST'])

def fungsikalender():
    if request.method == 'GET':
        return get_kalender()
    elif request.method == 'POST':
        date = request.args.get('date', '')
        hari = request.args.get('hari', '')
        haribesar = request.args.get('haribesar', '')
        
        return newday(date,hari,haribesar)

@app.route('/API-Kalender-Hari-Besar', method = ['GET'])

def fungsihari(date):
    if request.method == 'GET':
        return get_hari(date)
        
        
def get_kalender():
    kalender = session.query(Day).all()
    return jsonify(kalender= [d.serialize for d in kalender])
    
def get_hari(date_dicari):
    hari = session.query(Day).filter_by(date = date_dicari).one()
    return jsonify(hari= hari.serialize)
    
def newday(date,hari,haribesar)
    if haribesar == "":
        isHaribesar = False
    else
        isHaribesar = True
        
    haribaru = Day(date=date, hari=hari, haribesar=haribesar, isHaribesar=isHaribesar)
    session.add(haribaru)
    return jsonify(hari=haribaru.serialize)
