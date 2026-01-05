from flask import Flask , render_template , request , jsonify

app=Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/bmi', methods=["POST"])
def calculate_bmi():
    data = request.get_json()

    weight = data['weight']
    height = data['height']

    bmi = weight/(height**2)

    return jsonify({
        "BMI":round(bmi,2)
    })

if __name__ == "__main__":
 app.run(debug=True)