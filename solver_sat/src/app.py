from gen import generate_random_SAT, read_cnf
from solver import solve, test
import copy, sys, pycosat
import tkinter as tk

sys.setrecursionlimit(10**4)

def get_values():
    global literais, clausulas, literais_por_clausula
    try:
        literais = int(entry1.get())
        clausulas = int(entry2.get())
        literais_por_clausula = int(entry3.get())

    except ValueError as err:
        l_message.config(text="Insira números inteiros...")

def gerar_sat():
    global formula
    formula = generate_random_SAT(literais, clausulas, literais_por_clausula)

def obter_sample():
    global formula
    formula = read_cnf(entry4.get())

def algoritmo():
    result = []
    result = solve(formula)
    l_message.config(text=f'O resultado é {result}')

if __name__ == '__main__':
    app = tk.Tk()
    app.title("Solucionador SAT Yeshua")

    label1 = tk.Label(app, text="Numero de literais")
    label2 = tk.Label(app, text="Numero de clausulas")
    label3 = tk.Label(app, text="Numero de literais por clausula")
    label4 = tk.Label(app, text="Aqruivo CNF")
    l_message = tk.Label(app)

    entry1 = tk.Entry(app)
    entry2 = tk.Entry(app)
    entry3 = tk.Entry(app)
    entry4 = tk.Entry(app)

    btn1 = tk.Button(app, text="Confirmar valores", command=get_values)
    btn2 = tk.Button(app, text="Gerar SAT", command=gerar_sat)
    btn3 = tk.Button(app, text="Simular Algoritmo", command=algoritmo)
    btn4 = tk.Button(app, text="Ler cnf", command=obter_sample)

    label1.grid(column=0, row=0)
    label2.grid(column=0, row=1)
    label3.grid(column=0, row=2)
    label4.grid(column=0, row=3)
    l_message.grid(column=0, row=4)

    entry1.grid(column=1, row=0)
    entry2.grid(column=1, row=1)
    entry3.grid(column=1, row=2)
    entry4.grid(column=1, row=3)
    
    btn1.grid(column=2, row=0)
    btn2.grid(column=2, row=1)
    btn3.grid(column=2, row=2)
    btn4.grid(column=2, row=3)

    app.mainloop()
