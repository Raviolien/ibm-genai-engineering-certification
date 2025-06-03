# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: list all transactions
@app.route("/")
def get_transactions():
    '''
    Function to get transactions
    '''
    return render_template("transactions.html", transactions=transactions)

# Create operation

@app.route("/add", methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'GET':
        return render_template("form.html")
    
    if request.method == 'POST':
        # Create new transaction
        transaction = {
              'id': len(transactions)+1,
              'date': request.form['date'],
              'amount': float(request.form['amount'])
             }
        
        # Append the new transaction to existing transactions
        transactions.append(transaction)

        # Redirect to read url
        return redirect(url_for("get_transactions"))

# Update operation
@app.route("/edit/<int:transaction_id>", methods = ['GET', 'POST'])
def edit_transaction(transaction_id):
    
    # POST
    if request.method == 'POST':

        # Extract updated values
        date = request.form['date']
        amount = float(request.form['amount'])
        
        # Find the transaction and update values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break # Exit loop when transaction is found
        
        # Redirect to the read url
        return redirect(url_for("get_transactions"))

    # GET
    # Find transaction_id in transactions
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)

    # Transaction not found
    return {"message": "Transaction not found"}, 404

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    
    # Find the transaction and remove it
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break # exit loop if found
    
    # Redirect to read url
    return redirect(url_for("get_transactions"))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)    