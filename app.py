from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Ambil data dari form
        nama = request.form['nama']
        umur = request.form['umur']
        berat_badan = request.form['berat_badan']
        tinggi_badan = request.form['tinggi_badan']

        # Validasi sederhana
        if nama and umur and berat_badan and tinggi_badan:
            # Hitung BMI
            bmi = float(berat_badan) / ((float(tinggi_badan) / 100) ** 2)
            
            # Kategorikan BMI
            if bmi < 18.5:
                kategori = "Kekurangan Berat Badan"
            elif 18.5 <= bmi < 25:
                kategori = "Berat Badan Normal"
            elif 25 <= bmi < 30:
                kategori = "Kelebihan Berat Badan"
            else:
                kategori = "Obesitas"
            
            result = {
                'nama': nama,
                'umur': umur,
                'berat_badan': berat_badan,
                'tinggi_badan': tinggi_badan,
                'bmi': round(bmi, 2),
                'kategori_bmi': kategori
            }
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)