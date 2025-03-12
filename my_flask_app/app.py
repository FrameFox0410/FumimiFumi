from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    rabbit_info = {
        "name": "ฟูมิมิฟู",
        "species": "Holland Lop",
        "age": 5,
        "color": "ขาว-น้ำตาล",
        "weight": " กิโลกรัม",
        "description": "กระต่ายพันธุ์ Holland Lop ที่น่ารักและขี้เล่น(กัดทีเลือดอาบ)ชอบกินแครอทและอาหารเม็ดสีชมพู"
    }
    return render_template('index.html', rabbit=rabbit_info)

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)