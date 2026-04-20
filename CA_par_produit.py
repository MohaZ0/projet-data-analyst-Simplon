import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

données['CA'] = données['prix'] * données['qte']

figure = px.pie(données, values='CA', names='produit', title='CA par produit')

figure.write_html('CA-par-produit.html')

print('CA-par-produit.html généré avec succès !')