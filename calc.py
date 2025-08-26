from flask import Flask, render_template, request

app = Flask(__name__)

# Home route to display the calculator form
@app.route('/')
def home():
    return render_template('calculator.html')

# Route to handle the calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get input values from the form
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        # Perform the selected operation
        if operation == 'add':
            result = num1 + num2
            operation_name = "Addition"
        elif operation == 'subtract':
            result = num1 - num2
            operation_name = "Subtraction"
        elif operation == 'multiply':
            result = num1 * num2
            operation_name = "Multiplication"
        elif operation == 'divide':
            if num2 == 0:
                return render_template('calculator.html', error="Division by zero is not allowed.")
            result = num1 / num2
            operation_name = "Division"
        else:
            return render_template('calculator.html', error="Invalid operation selected.")

        # Render the result, also pass back the original numbers and operation
        # so the user can see what they entered
        return render_template('calculator.html', result=result, operation=operation_name, num1=num1, num2=num2)

    except ValueError:
        return render_template('calculator.html', error="Invalid input. Please enter numeric values.")
    except KeyError:
        return render_template('calculator.html', error="Missing form data. Please fill out all fields.")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)