from flask import Flask, request, redirect

app = Flask(__name__)

expenses = []

CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Health", "Entertainment", "Education", "Other"]

@app.route('/')
def home():
    total = sum([e['amount'] for e in expenses])

    if not expenses:
        expense_list = "<tr><td colspan='5'>No expenses added yet</td></tr>"
    else:
        expense_list = ""
        for i, e in enumerate(expenses):
            expense_list += f"""
            <tr>
                <td>{e['name']}</td>
                <td>₹{e['amount']}</td>
                <td><span class="tag">{e['category']}</span></td>
                <td>{e['date']}</td>
                <td>
                    <a href="/delete/{i}" class="delete-btn"
                    onclick="return confirm('Delete this expense?')">Delete</a>
                </td>
            </tr>
            """

    category_options = "".join([f"<option>{c}</option>" for c in CATEGORIES])

    return f"""
    <html>
    <head>
        <title>Expense Tracker</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f4f6f8;
                margin: 0;
                padding: 0;
            }}
            .container {{
                width: 60%;
                margin: auto;
                margin-top: 30px;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                text-align: center;
                color: #333;
            }}
            .subtitle {{
                text-align: center;
                color: gray;
                margin-bottom: 20px;
            }}
            form {{
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                justify-content: center;
                margin-bottom: 20px;
            }}
            input, select {{
                padding: 8px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }}
            button {{
                background-color: #28a745;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 5px;
                cursor: pointer;
            }}
            button:hover {{
                background-color: #218838;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                padding: 10px;
                border-bottom: 1px solid #ddd;
                text-align: center;
            }}
            th {{
                background-color: #007bff;
                color: white;
            }}
            .delete-btn {{
                color: white;
                background-color: red;
                padding: 5px 10px;
                border-radius: 5px;
                text-decoration: none;
            }}
            .delete-btn:hover {{
                background-color: darkred;
            }}
            .tag {{
                padding: 5px 10px;
                border-radius: 10px;
                background-color: #17a2b8;
                color: white;
            }}
            .total-card {{
                margin-top: 15px;
                padding: 10px;
                background-color: #ffc107;
                text-align: center;
                font-weight: bold;
                border-radius: 5px;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Expense Tracker</h1>
            <p class="subtitle">Track and manage your daily expenses efficiently</p>

            <form method="POST" action="/add">
                <input name="name" placeholder="Expense Name" required>
                <input name="amount" type="number" placeholder="Amount" required>
                <select name="category">
                    {category_options}
                </select>
                <input name="date" type="date" required>
                <button type="submit">Add Expense</button>
            </form>

            <table>
                <tr>
                    <th>Name</th>
                    <th>Amount</th>
                    <th>Category</th>
                    <th>Date</th>
                    <th>Action</th>
                </tr>
                {expense_list}
            </table>

            <div class="total-card">Total Expense: ₹{total}</div>
        </div>
    </body>
    </html>
    """

@app.route('/add', methods=['POST'])
def add():
    expense = {
        'name': request.form['name'],
        'amount': int(request.form['amount']),
        'category': request.form['category'],
        'date': request.form['date']
    }

    expenses.insert(0, expense)

    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)