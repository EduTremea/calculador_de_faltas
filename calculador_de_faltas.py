import tkinter as tk
from PIL import Image, ImageTk

def calcular_faltas():
    try:
        total_dias = int(entry_total_dias.get())
        faltas_atual = int(entry_faltas.get())
        
        limite_faltas = int(total_dias * 0.25)

        faltas_restantes = limite_faltas - faltas_atual

        print(f"Total de dias: {total_dias}, Faltas atuais: {faltas_atual}, Limite de faltas: {limite_faltas}, Faltas restantes: {faltas_restantes}")

        if faltas_restantes > 1:
            msg = f"Você ainda pode faltar {faltas_restantes} dias."
            exibir_imagem("pode_faltar.jpg")  
        elif faltas_restantes == 1:
            msg = "Você ainda pode faltar 1 dia."
            exibir_imagem("pode_faltar.jpg")  
        elif faltas_restantes == 0:
            msg = "Você não pode mais faltar. Cuidado!!"
            exibir_imagem("nao_pode_faltar.jpg")  
        else:
            msg = "Você excedeu o limite de faltas! Parabéns, reprovou ^^"
            exibir_imagem("reprovo.jpg")  

        # Atualiza o rótulo com a mensagem
        lbl_mensagem.config(text=msg)

    except ValueError:
        lbl_mensagem.config(text="Erro: Por favor, insira números válidos.")
        print("Erro: entradas inválidas.")

def exibir_imagem(nome_imagem):
    try:
        img = Image.open(nome_imagem)
        img = img.resize((200, 200), Image.LANCZOS)  
        img_tk = ImageTk.PhotoImage(img)
        lbl_imagem.configure(image=img_tk)
        lbl_imagem.image = img_tk
        print(f"Imagem {nome_imagem} carregada com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Controle de Faltas")
root.geometry("350x550")  

tk.Label(root, text="Total de dias no semestre:").pack(pady=10)
entry_total_dias = tk.Entry(root)
entry_total_dias.pack()

tk.Label(root, text="Quantidade de faltas atuais:").pack(pady=10)
entry_faltas = tk.Entry(root)
entry_faltas.pack()

btn_calcular = tk.Button(root, text="Calcular Faltas", command=calcular_faltas)
btn_calcular.pack(pady=20)

lbl_imagem = tk.Label(root)
lbl_imagem.pack()

lbl_mensagem = tk.Label(root, text="", font=("Arial", 12), wraplength=300)
lbl_mensagem.pack(pady=10)

root.mainloop()
