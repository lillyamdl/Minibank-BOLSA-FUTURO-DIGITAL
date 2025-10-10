import tkinter as tk
from mini_bank.src.models.Cliente import Cliente
from mini_bank.src.models.Conta import Conta
from mini_bank.src.models.Saque import Saque
from mini_bank.src.models.Deposito import Deposito

# Criação de cliente e conta (exemplo simples)
cliente = Cliente("Rua Exemplo, 123")
conta = Conta.nova_conta(cliente, "12345")
cliente.adicionar_conta(conta)

def depositar():
    valor = float(entry_valor.get())
    deposito = Deposito(valor)
    cliente.realizar_transacao(conta, deposito)
    label_resultado.config(text=f"Depósito de R${valor:.2f} realizado!")

def sacar():
    valor = float(entry_valor.get())
    saque = Saque(valor)
    cliente.realizar_transacao(conta, saque)
    label_resultado.config(text=f"Saque de R${valor:.2f} realizado!")

# Interface Tkinter
root = tk.Tk()
root.title("MiniBank")

label_valor = tk.Label(root, text="Valor:")
label_valor.pack()

entry_valor = tk.Entry(root)
entry_valor.pack()

btn_depositar = tk.Button(root, text="Depositar", command=depositar)
btn_depositar.pack()

btn_sacar = tk.Button(root, text="Sacar", command=sacar)
btn_sacar.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack()

root.mainloop()