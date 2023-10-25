from flask import Flask, render_template, request

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@app.route('/', methods=['GET', 'POST'])
def temperature_converter():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            source_unit = request.form['source_unit']
            target_unit = request.form['target_unit']
            
            if source_unit == 'celsius' and target_unit == 'fahrenheit':
                result = celsius_to_fahrenheit(value)
            elif source_unit == 'fahrenheit' and target_unit == 'celsius':
                result = fahrenheit_to_celsius(value)
            else:
                return "Unsupported unit conversion"
        except ValueError:
            return "Invalid input. Please enter a numeric value."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
