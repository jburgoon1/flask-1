from flask import Flask, session, request,render_template, url_for, flash, redirect
from convert import converter, CC, CR
app = Flask(__name__)
app.secret_key='sdadasdas'

@app.route('/')
def show_exchanger():
    return render_template('index.html')

@app.route('/convert', methods = ['GET','POST'])
def convert_currency():
    input_code = request.form.get('in')
    output_code = request.form.get('out')
    amount = request.values.get('amount', type = int)
    converted = converter(input_code,output_code,amount)
    symbol = CC.get_symbol(output_code)
    if output_code not in CR.get_rates(input_code):
        flash('no good')
        return redirect(url_for('show_exchanger'))
    flash('Currency Converted')
    return render_template('amount.html', converted = converted, symbol = symbol)