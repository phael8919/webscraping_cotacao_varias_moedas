from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import requests
from bs4 import BeautifulSoup as bs

dict_moedas = {
    'Dólar': 'dolar',
    'Euro': 'euro',
    'Libra Esterlina': 'libra-esterlina',
    'Dólar Australiano': 'dolar-australiano',
    'Dólar Canadense': 'dolar-canadense',
    'Franco Suiço': 'franco-suico',
    'Yene Japonês': 'iene-japones',
    'Peso Argentino': 'peso-argentino',
    'Peso Uruguaio': 'peso-uruguaio',
    'Novo Sol Peruano': 'novo-sol',
    'Boliviano': 'boliviano',
    'Yuan Chinês': 'yuan-chines',
    'Dólar de Singapura': 'dolar-singapura',
    'Lira Turca': 'lira-turca',
    'Dólar de Hong Kong': 'dolar-hong-kong'   
}

tela = Tk()
tela.geometry('750x500')
tela.title('Cotações')

titulo = Label(tela, text='COTAÇÕES DE MOEDAS (COMERCIAL)', font='Arial 20 bold')
titulo.pack(pady=25, padx=50)

def exibe_valor(): 
   try:
       moeda =  dict_moedas[combo.get()]
       url = 'https://www.remessaonline.com.br/cotacao/cotacao-'+moeda
        
       consulta = requests.get(url).text
        
       resultado = bs(consulta)
        
       resultado = resultado.select('.style__Text-sc-1a6mtr6-2')
        
       resultado = resultado[0].text  
    
       moeda_convertida = resultado[0:4]
       moeda_convertida = float(moeda_convertida.replace(',','.')) 
   
       valor = float(entrada1.get())
       valor_final = 'R$ '+str(round(valor * moeda_convertida,2)).replace('.',',')
       
       if len(valor_final) <8:
            resultado = valor_final+'0'
       else:
            resultado = valor_final
        
       mensagem['text'] = resultado
       
   except:
        messagebox.showwarning('Erro', 'Escolha a moeda ou digite o valor a converter')

rotulo1 = Label(tela, text='Escolha a moeda:', font='Arial 20')
rotulo1.pack(pady=1,padx=15)

combo = Combobox(tela, font='Arial 20')
combo['values']= ('Dólar', 'Euro', 'Libra Esterlina','Dólar Australiano','Dólar Canadense',
                  'Franco Suiço','Yene Japonês','Peso Argentino','Peso Uruguaio','Novo Sol Peruano',
                 'Boliviano','Yuan Chinês','Dólar de Singapura','Lira Turca','Dólar de Hong Kong')
combo.current(0)
combo.pack(pady=15,padx=15)

rotulo2 = Label(tela, text='Digite o valor a converter:', font='Arial 20')
rotulo2.pack(pady=1,padx=15)

entrada1 = Entry(tela, font="arial 20", width=21, text='um')
entrada1.pack(pady=15,padx=15)

rotulo3 = Label(tela, text='Valor em Reais:', font='Arial 20')
rotulo3.pack(pady=1,padx=15)

botao = Button(tela, text="Clique Aqui!", width = 26, font='Arial 15 bold',bg='blue', fg='white', command=exibe_valor)
botao.pack(pady=15,padx=15)

mensagem = Label(tela, font="arial 20 bold")
mensagem.pack(pady=15,padx=15)

tela.mainloop()