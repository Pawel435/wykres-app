from flask import Flask, request, render_template, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        numbers = [
            float(request.form[f"num{i}"]) 
            for i in range(1, 6)
        ]
        
        # Tworzenie wykresu
        plt.figure()
        plt.plot(numbers, marker='o')
        plt.title("Wykres Twoich liczb")
        plt.xlabel("Kolejne liczby")
        plt.ylabel("Wartości")
        
        # Zapis do bufora w pamięci
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        
        return send_file(buf, mimetype="image/png")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)