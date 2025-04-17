from Flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>สายพันธุ์แมว</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f8ff;
        }

        header {
            background-color: #ffb6c1;
            padding: 20px;
            text-align: center;
        }

        header h1 {
            color: #4b0082;
        }

        nav ul {
            list-style-type: none;
            padding: 0;
        }

        nav ul li {
            display: inline;
            margin: 10px;
        }

        nav ul li a {
            text-decoration: none;
            color: #4b0082;
            font-weight: bold;
        }

        section {
            padding: 20px;
            margin: 20px;
            background-color: white;
            border-radius: 8px;
        }

        section h2 {
            color: #ff6347;
        }

        section p {
            color: #555;
        }

        footer {
            background-color: #4b0082;
            color: white;
            text-align: center;
            padding: 10px;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>ยินดีต้อนรับสู่เว็บไซต์สายพันธุ์แมว</h1>
        <nav>
            <ul>
                <li><a href="#siamese">แมวพันธุ์สยาม</a></li>
                <li><a href="#persian">แมวพันธุ์เปอร์เซีย</a></li>
                <li><a href="#mainecoon">แมวพันธุ์เมนคูน</a></li>
            </ul>
        </nav>
    </header>
    
    <section id="siamese">
        <h2>แมวพันธุ์สยาม</h2>
        <p>แมวพันธุ์สยามเป็นแมวที่มีลักษณะเฉพาะตัว...</p>
        <img src="siamese.jpg" alt="แมวพันธุ์สยาม">
    </section>
    
    <section id="persian">
        <h2>แมวพันธุ์เปอร์เซีย</h2>
        <p>แมวพันธุ์เปอร์เซียเป็นหนึ่งในสายพันธุ์ที่มีขนยาว...</p>
        <img src="persian.jpg" alt="แมวพันธุ์เปอร์เซีย">
    </section>
    
    <section id="mainecoon">
        <h2>แมวพันธุ์เมนคูน</h2>
        <p>แมวพันธุ์เมนคูนเป็นแมวที่มีขนาดใหญ่และขนยาว...</p>
        <img src="mainecoon.jpg" alt="แมวพันธุ์เมนคูน">
    </section>

    <footer>
        <p>© 2025 เว็บไซต์สายพันธุ์แมว</p>
    </footer>
</body>
</html>
"""

# กำหนด route ของเว็บไซต์
@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
