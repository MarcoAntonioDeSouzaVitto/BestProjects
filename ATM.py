####################--ATM WITH CUSTOMTKINTER USING JSON--####################
import json
import os
from datetime import datetime
import customtkinter as ctk

root = ctk.CTk()
ctk.set_appearance_mode("dark")
root.geometry("1200x950")
root.resizable(False,False)
statement = []
wallet = 0
caixa = [100, 50, 20, 10, 5, 1]
retiradas = []
if os.path.exists("In3vcrTcnk16bUWT0g46WA.json"):
    with open("In3vcrTcnk16bUWT0g46WA.json", "r", encoding="utf-8") as efi:
        try:
            data = json.load(efi)
            wallet = data["wallet"]
            statement = data["history"]
        except (json.JSONDecodeError,KeyError):
            statement = []
            wallet = 0
data_base = {
    "wallet": wallet,
    "history": statement
}

print("Hello Word")



def panel():
    frame_overlay = None
    root.configure(fg_color="#edfaff")
    frame_prin = ctk.CTkFrame(root, fg_color="#222324")
    frame_prin.place(
        relx=0.5,rely=0.25,relwidth=0.75,relheight=0.35,anchor="center"
    )
    tela = ctk.CTkFrame(root, fg_color="#c0cca5")
    tela.place(
        relx=0.5,rely=0.25,relwidth=0.4,relheight=0.25,anchor="center"
    )
    ctk.CTkLabel(root, text="AA", fg_color="#c0cca5", text_color="black",font=("Arial", 32)).place(
        relx=0.5, rely=0.25, anchor="center"
    )
    ######################################################################
    def shw():
        msg = []
        nonlocal frame_overlay
        if frame_overlay is not None:
            frame_overlay.destroy()
            frame_overlay = None
            return
        frame_overlay = ctk.CTkFrame(root, fg_color="#c0cca5")
        frame_overlay.place(
        relx=0.5,rely=0.25,relwidth=0.4,relheight=0.25,anchor="center"
    )
        def visualizar():
            if os.path.exists("In3vcrTcnk16bUWT0g46WA.json"):
                with open("In3vcrTcnk16bUWT0g46WA.json", "r", encoding="utf-8") as efi:
                    dataw = json.load(efi)
                for i in dataw["history"]:
                    msg.append(i)
            else:
                msg.append("ERROR")
        visualizar()
        texto_exibicao = f"Saldo Atual: R$ {wallet}\n\n" + "\n".join(msg)
        mensagem = ctk.CTkLabel(frame_overlay,text=texto_exibicao,text_color="White", font=("arial",20))
        mensagem.place(
            relx=0.5, rely=0.25, anchor="center"
        )

    ######################################################################
    def dep():
        global wallet
        nonlocal frame_overlay
        if frame_overlay is not None:
            frame_overlay.destroy()
            frame_overlay = None
            return
        frame_overlay = ctk.CTkFrame(root, fg_color="#c0cca5")
        frame_overlay.place(
        relx=0.5,rely=0.25,relwidth=0.4,relheight=0.25,anchor="center"
    )
        mensagem = ctk.CTkLabel(frame_overlay, text="", text_color="White", font=("arial", 20))
        mensagem.place(relx=0.5, rely=0.15, anchor="center")
        value_entry = ctk.CTkEntry(frame_overlay, placeholder_text="Ex: 81.54", font=("Arial", 24))
        value_entry.place(relx=0.5, rely=0.45, relwidth=0.5, relheight=0.2, anchor="center")
        def depositar():
            global wallet
            msg = []
            try:
                getanswer = float(value_entry.get().replace(",", "."))
            except ValueError:
                mensagem.configure(text="!INSIRA UM NÚMERO VÁLIDO!")
                return
            if getanswer >= 1:
                blank = getanswer
                hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                statement.append(f"{hora_atual} | +R${getanswer}")
                for nota in caixa:
                    while getanswer >= nota:
                        retiradas.append(nota)
                        getanswer -= nota
                wallet += blank
                data_base["wallet"] = wallet
                data_base["history"] = statement
                with open("In3vcrTcnk16bUWT0g46WA.json", "w", encoding="utf-8") as f:
                    json.dump(data_base, f, indent=4, ensure_ascii=False)
                mensagem.configure(text=f"→ Depósito de R${blank:.2f} efetuado.")
                value_entry.delete(0, 'end')
            else:
                mensagem.configure(text="!VALOR MÍNIMO É R$ 1.00!")
        send = ctk.CTkButton(frame_overlay, text="Enviar", command=depositar)
        send.place(relx=0.5, rely=0.8, relwidth=0.3, relheight=0.15, anchor="center")

    ######################################################################

    def wtw():
        global wallet
        nonlocal frame_overlay
        if frame_overlay is not None:
            frame_overlay.destroy()
            frame_overlay = None
            return
        frame_overlay = ctk.CTkFrame(root, fg_color="#c0cca5")
        frame_overlay.place(
        relx=0.5,rely=0.25,relwidth=0.4,relheight=0.25,anchor="center"
    )
        mensagem = ctk.CTkLabel(frame_overlay, text="", text_color="White", font=("arial", 20))
        mensagem.place(relx=0.5, rely=0.15, anchor="center")
        value_entry = ctk.CTkEntry(frame_overlay, placeholder_text="Ex: 81.54", font=("Arial", 24))
        value_entry.place(relx=0.5, rely=0.45, relwidth=0.5, relheight=0.2, anchor="center")
        def sacar():
            global wallet
            msg = []
            try:
                getanswer = float(value_entry.get().replace(",", "."))
            except ValueError:
                mensagem.configure(text="!INSIRA UM NÚMERO VÁLIDO!")
                return
            if 1 <= getanswer <= wallet:
                blank = getanswer
                hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                statement.append(f"{hora_atual} | -R${getanswer}")
                for nota in caixa:
                    while getanswer >= nota:
                        retiradas.append(nota)
                        getanswer -= nota
                wallet -= blank
                data_base["wallet"] = wallet
                data_base["history"] = statement
                with open("In3vcrTcnk16bUWT0g46WA.json", "w", encoding="utf-8") as f:
                    json.dump(data_base, f, indent=4, ensure_ascii=False)
                mensagem.configure(text=f"→ Saque de R${blank:.2f} efetuado.\n")
                value_entry.delete(0, 'end')
            else:
                mensagem.configure(text= "!VALOR MAIOR QUE SALDO ATUAL!")
        send = ctk.CTkButton(frame_overlay, text="Enviar", command=sacar)
        send.place(relx=0.5, rely=0.8, relwidth=0.3, relheight=0.15, anchor="center")

    ######################################################################
    sbs = ctk.CTkButton(frame_prin, text="Show balance and statement",command=shw)
    de = ctk.CTkButton(frame_prin, text="Deposite",command=dep)
    ww = ctk.CTkButton(frame_prin, text="Withdraw",command=wtw)
    blankre = ctk.CTkButton(frame_prin, text="BLANK")
    sbs.place(
        relx=0.12, rely=0.3, relwidth=0.2, relheight=0.28, anchor="center"
    )
    de.place(
        relx=0.12, rely=0.7, relwidth=0.2, relheight=0.28, anchor="center"
    )
    ww.place(
        relx=0.88, rely=0.3, relwidth=0.2, relheight=0.28, anchor="center"
    )
    blankre.place(
        relx=0.88, rely=0.7, relwidth=0.2, relheight=0.28, anchor="center"
    )
    ######################################################################

panel()
root.mainloop()