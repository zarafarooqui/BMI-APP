from flask import Flask , request , jsonify

app=Flask(__name__)
@app.route('/bmi', methods=["POST"])
def calculate_bmi():
    data = request.get_json()

    weight = data['weight']
    height = data["height"]

    bmi = weight*height

    return jsonify({
        "BMI":round(bmi,2)
    })

if __name__ == "__main__":
 app.run(debug=True)