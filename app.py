from flask import Flask, render_template

app = Flask(__name__)

# Example tattoo data (image files should be in static/images/)
tattoos = [
    {"name": "Dragon Tattoo", "image": "image1.png", "price": 150},
    {"name": "Rose Tattoo", "image": "image2.png", "price": 80},
    {"name": "Skull Tattoo", "image": "image3.png", "price": 120},
]

@app.route("/")
def index():
    return render_template("index.html", tattoos=tattoos)

if __name__ == "__main__":
    app.run(debug=True)