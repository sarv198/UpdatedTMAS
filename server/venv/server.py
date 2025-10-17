from flask import Flask, jsonify

# app instance
app = Flask(__name__)
CORS(app)

# /api/home/
@app.route("/api/home", methods=["GET"])
def return_home():
    return jsonify({
        'message': "Subscribe to TMAS!",
        'people': ['Sarvesh', 'Aditya']
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)
