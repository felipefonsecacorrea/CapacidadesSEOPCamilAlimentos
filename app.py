from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        industry = request.form['industry']
        segment = request.form['segment']
        productType = request.form['productType']
        quantity = request.form['quantity']
        productionDays = request.form['productionDays']

        data = {
            'Industry': [industry],
            'Segment': [segment],
            'Product Type': [productType],
            'Quantity': [quantity],
            'Production Days': [productionDays]
        }

        df = pd.DataFrame(data)
        file_path = 'data.xlsx'

        # Check if the file exists
        if not os.path.isfile(file_path):
            # If it does not exist, create it with the DataFrame
            df.to_excel(file_path, index=False)
        else:
            # If it exists, append the data to the file without overwriting it
            existing_df = pd.read_excel(file_path)
            new_df = pd.concat([existing_df, df], ignore_index=True)
            new_df.to_excel(file_path, index=False)

        return f"""
        <h1>Dados Recebidos</h1>
        <p>Indústria: {industry}</p>
        <p>Segmento: {segment}</p>
        <p>Tipo de Produto: {productType}</p>
        <p>Quantidade: {quantity}</p>
        <p>Dias de Produção: {productionDays}</p>
        <p><a href='/'>Voltar</a></p>
        """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)