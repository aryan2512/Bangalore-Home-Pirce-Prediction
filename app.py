from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)
util.load_saved_artifacts()

@app.route('/', methods=['GET', 'POST'])
def predict_home_price():
    locations = util.get_location_names()
    param = {
        'total_sqft': 1000,
        'location': 'Choose location',
        'bhk': 2,
        'bath': 2,
        'price': ''
    }
    if request.method=='POST':
        total_sqft = float(request.form['Squareft'])
        location = request.form['uiLocations']
        bhk = int(request.form['uiBHK'])
        bath = int(request.form['uiBathrooms'])
        if location== 'Choose location':
            price= 'select location'
        else:
            price= util.get_estimated_price(location,total_sqft,bhk,bath)
            price= str(price)+ '  lakh'
        param= {
            'total_sqft' : total_sqft,
            'location' : location,
            'bhk' : bhk,
            'bath' : bath,
            'price' : price

        }
        return render_template('app.html',locations=locations,param=param)
    return render_template('app.html',locations=locations,param=param)

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(host='192.168.0.101' ,debug=True)
