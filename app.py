from Flask import jsonify

@app.route('/')
@app.route('/API-Kalender-Hari-Besar', method = ['GET', 'POST'])

def fungsikalender():
    if request.method == 'GET':
        return get_kalender()
    elif request.method == 'POST':
        date = request.args.get('date', '')
        hari = request.args.get('hari', '')
        isHaribesar = request.args.get('isHaribesar', '')
        haribesar = request.args.get('haribesar', '')
        
        return newday(date,hari,isHaribesar,haribesar)

@app.route('/API-Kalender-Hari-Besar', method = ['GET'])

def fungsihari(date):
    if request.method == 'GET':
        return get_kalender(date)