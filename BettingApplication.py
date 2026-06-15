import sqlite3
import customtkinter as ctk
ctk.set_appearance_mode("dark")
janela = ctk.CTk()
largura_tela = janela.winfo_screenwidth()
height_tela = janela.winfo_screenheight()
janela.geometry("900x700")
janela.title("Grand Jaguar")

conexao = sqlite3.connect("mkV3060.db")
funcio = conexao.cursor()
funcio.execute("""
    CREATE TABLE IF NOT EXISTS base(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        saldo REAL NOT NULL,
        pp TEXT NOT NULL
)
""")
e = ""
def lobby():
    def accountCreate():
        global warning, e
        try:
            warning.place_forget()
        except:
            pass
        u = username_create.get()
        e = email_create.get()
        p = passwrd_create.get()
        cp = confpasswrd_create.get()
        sd = 0
        profpic = 0
        if not (u and e and p and cp):
            msg = "ALL FIELDS ARE REQUIRED"
        elif not e.endswith(("@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@live.com", "@icloud.com")):
            msg = "INSERT A VALID EMAIL ADDRESS"
        elif len(p) < 6:
            msg = "MINIMUM 6 CHARACTERS"
        elif p != cp:
            msg = "PASSWORDS DO NOT MATCH"
        else:
            funcio.execute(
                "INSERT INTO base(username,email,password, saldo,pp) VALUES(?,?,?,?,?)",
                (u,e,p,sd,profpic)
            )
            conexao.commit()
            game()
            return
        warning = ctk.CTkLabel(frameLogin, text=f"{msg}", text_color="red")
        warning.place(relx = 0.75, rely =0.72, anchor = "center")
    def login():
        global warning, e
        try:
            warning.place_forget()
        except:
            pass
        e = email_login.get()
        p = passwrd_login.get()
        if not (e and p):
            msg = "ALL FIELDS ARE REQUIRED"
        else:
            funcio.execute(
                "SELECT email, password FROM base WHERE email = ? AND password = ?",
                (e,p)
            )
            resultado = funcio.fetchall()
            if resultado:
                game()
                return
            else:
                msg = "INCORRECT PASSWORD OR EMAIL"
        warning = ctk.CTkLabel(frameLogin, text=f"{msg}", text_color="red")
        warning.place(relx = 0.25, rely =0.56, anchor = "center")
    def login_guest():
        global e
        e = "guest@grandjaguar.com"

        funcio.execute("SELECT email FROM base WHERE email = ?", (e,))
        if not funcio.fetchone():
            funcio.execute(
                "INSERT INTO base(username, email, password, saldo, pp) VALUES(?,?,?,?,?)",
                ("Guest_Player", e, "123456", 100.00, "0")
            )
            conexao.commit()

        game()

    janela.configure(fg_color="#121212")
    go_game = ctk.CTkButton(janela, text="Game",corner_radius=75, command=login_guest)
    go_game.place(relx=0.9, rely=0.9,relwidth=0.167,relheight=0.214, anchor="center")

    frameLogin = ctk.CTkFrame(janela, fg_color="#101c30")
    frameLogin.place(relx=0.5,rely=0.5,relwidth=0.8,relheight=0.8,anchor= "center")
    frameVE = ctk.CTkFrame(frameLogin, fg_color="#ffdc82")
    frameVE.place(relx=0.5,rely=0.5,relwidth=0.004,relheight=0.923, anchor = "center")

    ctk.CTkLabel(frameLogin, text="WELCOME BACK", font=("Arial Regular", 28, "bold")).place(relx=0.25,rely=0.1,anchor="center")
    ctk.CTkLabel(frameLogin, text="E-mail", font=("Arial Regular", 16)).place(relx=0.09, rely=0.27,anchor="center")
    ctk.CTkLabel(frameLogin, text="Password", font=("Arial Regular", 16)).place(relx=0.104, rely=0.422, anchor="center")
    email_login = ctk.CTkEntry(frameLogin,placeholder_text="👤 E-mail", font=("Arial Regular",20))
    email_login.place(relx=0.25,rely=0.33,relwidth=0.368,relheight=0.077,anchor="center")
    passwrd_login = ctk.CTkEntry(frameLogin,placeholder_text="🔒 Password", font=("Arial Regular",20))
    passwrd_login.place(relx=0.25,rely=0.48,relwidth=0.368,relheight=0.077,anchor="center")
    send = ctk.CTkButton(frameLogin,text="ENTER", corner_radius=150, font=("Arial Regular",20), command=login)
    send.place(relx=0.25,rely=0.63,relwidth=0.316,relheight=0.077,anchor="center")

    ctk.CTkLabel(frameLogin, text="NEW HERE?", font=("Arial Regular", 28, "bold")).place(relx=0.75,rely=0.1,anchor="center")
    ctk.CTkLabel(frameLogin, text="Username", font=("Arial Regular", 16)).place(relx=0.75, rely=0.27,anchor="center")
    ctk.CTkLabel(frameLogin, text="E-mail", font=("Arial Regular", 16)).place(relx=0.8, rely=0.27,anchor="center")
    ctk.CTkLabel(frameLogin, text="Password", font=("Arial Regular", 16)).place(relx=0.75, rely=0.422, anchor="center")
    ctk.CTkLabel(frameLogin, text="Confirm Password", font=("Arial Regular", 16)).place(relx=0.8, rely=0.422, anchor="center")
    username_create = ctk.CTkEntry(frameLogin,placeholder_text="👤 Username", font=("Arial Regular",20))
    username_create.place(relx=0.75,rely=0.285,relwidth=0.368,relheight=0.077,anchor="center")
    email_create = ctk.CTkEntry(frameLogin, placeholder_text="📩 E-mail",font=("Arial Regular", 20))
    email_create.place(relx=0.75, rely=0.40,relwidth=0.368,relheight=0.077, anchor="center")
    passwrd_create = ctk.CTkEntry(frameLogin,placeholder_text="🔒 Password", font=("Arial Regular",20))
    passwrd_create.place(relx=0.75,rely=0.515,relwidth=0.368,relheight=0.077,anchor="center")
    confpasswrd_create = ctk.CTkEntry(frameLogin,placeholder_text="🔐 Confirm Password", font=("Arial Regular",20))
    confpasswrd_create.place(relx=0.75,rely=0.63,relwidth=0.368,relheight=0.077,anchor="center")
    send = ctk.CTkButton(frameLogin,text="CREATE ACCOUNT", corner_radius=150, font=("Arial Regular",20),command=accountCreate)
    send.place(relx=0.75,rely=0.8,relwidth=0.316,relheight=0.077,anchor="center")
def userInfo():
    for elemento in janela.winfo_children():
        elemento.destroy()
    overlay_aberto = False
    frame_overlay = None
    funcio.execute("SELECT saldo FROM base WHERE email = ?",(e,))
    result = funcio.fetchone()
    saldonow = result[0]
    def depositod():
        nonlocal saldonow
        textvalor = deposito.get().strip()
        if not textvalor:
            return
        valor = float(textvalor)
        saldonow += valor
        funcio.execute(
            "UPDATE base SET saldo = ? WHERE email = ?",
            (saldonow,e)
        )
        conexao.commit()
        saldo.configure(text=f"R${saldonow:.2f}")
        deposito.delete(0, "end")
    color_emoji = "#533566"
    def alternar_overlay():
        nonlocal overlay_aberto, frame_overlay
        if not overlay_aberto:
            frame_overlay = ctk.CTkFrame(janela, fg_color="gray20", corner_radius=10)
            frame_overlay.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
            texto = ctk.CTkLabel(frame_overlay, text="Change Profile Photo", font=("Arial Regular", 24,"bold"))
            texto.place(relx=0.1,rely=0.05,anchor="center")
            def emojiChangeA():
                funcio.execute("UPDATE base SET pp = ? WHERE email = ?",(0, e))
                conexao.commit()
                alternar_overlay()
                color_emoji = "#533566"
                userInfo()
            def emojiChangeB():
                funcio.execute("UPDATE base SET pp = ? WHERE email = ?",(1, e))
                conexao.commit()
                alternar_overlay()
                color_emoji = "#ff8257"
                userInfo()
            def emojiChangeC():
                funcio.execute("UPDATE base SET pp = ? WHERE email = ?",(2, e))
                conexao.commit()
                alternar_overlay()
                color_emoji = "#00d26a"
                userInfo()
            def emojiChangeD():
                funcio.execute("UPDATE base SET pp = ? WHERE email = ?",(3, e))
                conexao.commit()
                alternar_overlay()
                color_emoji = "#179354"
                userInfo()
            def emojiChangeE():
                funcio.execute("UPDATE base SET pp = ? WHERE email = ?",(4, e))
                conexao.commit()
                alternar_overlay()
                color_emoji = "#ffb235"
                userInfo()
            def emojiChangeF():
                funcio.execute("UPDATE base SET pp = ? WHERE email = ?",(5, e))
                conexao.commit()
                alternar_overlay()
                color_emoji = "#b05d46"
                userInfo()
            def emojiChangeG():
                funcio.execute("UPDATE base SET pp = ? WHERE email = ?",(6, e))
                conexao.commit()
                alternar_overlay()
                color_emoji = "#86d72f"
                userInfo()
            def emojiChangeH():
                funcio.execute("UPDATE base SET pp = ? WHERE email = ?",(7, e))
                conexao.commit()
                alternar_overlay()
                color_emoji = "#ff8687"
                userInfo()
            def emojiChangeI():
                funcio.execute("UPDATE base SET pp = ? WHERE email = ?",(8, e))
                conexao.commit()
                alternar_overlay()
                color_emoji = "#fea931"
                userInfo()
            def emojiChangeJ():
                funcio.execute("UPDATE base SET pp = ? WHERE email = ?",(9, e))
                conexao.commit()
                alternar_overlay()
                color_emoji = "#00a6ed"
                userInfo()
            def emojiChangeK():
                funcio.execute("UPDATE base SET pp = ? WHERE email = ?",(11, e))
                conexao.commit()
                alternar_overlay()
                color_emoji = "#f5d455"
                userInfo()
            button_emojiA = ctk.CTkButton(frame_overlay,text="👤", text_color="#533566", font=("Arial", 42), fg_color="#293142",border_color="#1a1a1a",border_width=3,command=emojiChangeA)
            button_emojiA.place(relx=0.1,rely=0.2,relwidth=0.105,relheight=0.154,anchor="center")
            button_emojiB = ctk.CTkButton(frame_overlay,text="🐙", text_color="#ff8257", font=("Arial", 42), fg_color="#293142",border_color="#1a1a1a",border_width=3,command=emojiChangeB)
            button_emojiB.place(relx=0.2,rely=0.2,relwidth=0.105,relheight=0.154,anchor="center")
            button_emojiC = ctk.CTkButton(frame_overlay,text="🐉", text_color="#00d26a", font=("Arial", 42), fg_color="#293142",border_color="#1a1a1a",border_width=3,command=emojiChangeC)
            button_emojiC.place(relx=0.3,rely=0.2,relwidth=0.105,relheight=0.154,anchor="center")
            button_emojiD = ctk.CTkButton(frame_overlay,text="🤑", text_color="#179354", font=("Arial", 42), fg_color="#293142",border_color="#1a1a1a",border_width=3,command=emojiChangeD)
            button_emojiD.place(relx=0.4,rely=0.2,relwidth=0.105,relheight=0.154,anchor="center")
            button_emojiE = ctk.CTkButton(frame_overlay,text="🤠", text_color="#ffb235", font=("Arial", 42), fg_color="#293142",border_color="#1a1a1a",border_width=3,command=emojiChangeE)
            button_emojiE.place(relx=0.5,rely=0.2,relwidth=0.105,relheight=0.154,anchor="center")
            button_emojiF = ctk.CTkButton(frame_overlay,text="💩", text_color="#b05d46", font=("Arial", 42), fg_color="#293142",border_color="#1a1a1a",border_width=3,command=emojiChangeF)
            button_emojiF.place(relx=0.6,rely=0.2,relwidth=0.105,relheight=0.154,anchor="center")
            button_emojiG = ctk.CTkButton(frame_overlay,text="👽", text_color="#86d72f", font=("Arial", 42), fg_color="#293142",border_color="#1a1a1a",border_width=3,command=emojiChangeG)
            button_emojiG.place(relx=0.7,rely=0.2,relwidth=0.105,relheight=0.154,anchor="center")
            button_emojiH = ctk.CTkButton(frame_overlay,text="🐷", text_color="#ff8687", font=("Arial", 42), fg_color="#293142",border_color="#1a1a1a",border_width=3,command=emojiChangeH)
            button_emojiH.place(relx=0.8,rely=0.2,relwidth=0.105,relheight=0.154,anchor="center")
            button_emojiI = ctk.CTkButton(frame_overlay,text="😼", text_color="#fea931", font=("Arial", 42), fg_color="#293142",border_color="#1a1a1a",border_width=3,command=emojiChangeI)
            button_emojiI.place(relx=0.9,rely=0.2,relwidth=0.105,relheight=0.154,anchor="center")
            button_emojiJ = ctk.CTkButton(frame_overlay,text="🐳", text_color="#00a6ed", font=("Arial", 42), fg_color="#293142",border_color="#1a1a1a",border_width=3,command=emojiChangeJ)
            button_emojiJ.place(relx=0.1,rely=0.4,relwidth=0.105,relheight=0.154,anchor="center")
            button_emojiK = ctk.CTkButton(frame_overlay,text="🐣", text_color="#f5d455", font=("Arial", 42), fg_color="#293142",border_color="#1a1a1a",border_width=3,command=emojiChangeK)
            button_emojiK.place(relx=0.2,rely=0.4,relwidth=0.105,relheight=0.154,anchor="center")
            botao_fechar = ctk.CTkButton(frame_overlay, text="Close", command=alternar_overlay)
            botao_fechar.place(relx=0.95,rely=0.97,relwidth=0.147,relheight=0.077,anchor="center")
            overlay_aberto = True
        else:
            if frame_overlay:
                frame_overlay.place_forget()
                frame_overlay.destroy()
            overlay_aberto = False

    janela.configure(fg_color="#121212")
    funcio.execute(
        "SELECT username, saldo, pp FROM base WHERE email = ?",
        (e,)
    )
    data = funcio.fetchone()
    pictures = ["👤", "🐙", "🐉", "🤑", "🤠", "💩", "👽", "🐷", "😼", "🐳", "🐯", "🐣"]
    ind = int(data[2])
    profile_picture = pictures[ind]
    canvas = ctk.CTkCanvas(janela, bg="#121212", highlightthickness=0)
    canvas.place(relx=0.33, rely=0.59,relwidth=0.526,relheight=0.769, anchor="center")
    canvas.create_oval(10, 10, 300, 300, fill="#2d3030", outline="orange")
    frameLobbys = ctk.CTkFrame(janela, fg_color="black", corner_radius=0)
    frameLobbys.place(relx=0.0, rely=0.0, relwidth=1.0,relheight=0.115, anchor="nw")
    botao3traco = ctk.CTkButton(frameLobbys,fg_color="black", text="≡", font=("Agency FB", 73, "bold"), hover_color="black")
    botao3traco.place(relx=0.03,rely=0.40,anchor="center")
    ctk.CTkLabel(frameLobbys, text="Grand\n       Jaguar",fg_color="black", font=("Agency FB", 35, "bold")).place(relx=0.12,rely=0.45,anchor="center")
    ctk.CTkButton(frameLobbys, text="🐯", text_color="Orange", fg_color="black",command= game, hover_color="black", font=("Agency FB", 43, "bold")).place(relx=0.08, rely=0.45,relwidth=0.042, anchor="center")
    ctk.CTkLabel(janela, text=profile_picture,fg_color="#2d3030",text_color= color_emoji, font=("Arial Regular", 120, "bold")).place(relx=0.15,rely=0.35,anchor = "center")
    ctk.CTkLabel(janela, text=data[0], font=("Arial Regular", 24, "bold")).place(relx=0.15, rely=0.57, anchor="center")
    ctk.CTkFrame(janela,fg_color="#121212", border_color="#d9c25b",border_width=3).place(relx=0.15,rely=0.75,relwidth=0.28,relheight=0.208,anchor="center")
    ctk.CTkLabel(janela, text="Saldo: ", font=("Microsoft Sans Serif", 24), text_color="white").place(relx=0.15, rely=0.68,anchor="center")
    saldo = ctk.CTkLabel(janela,text=f"R${data[1]:.2f}",text_color="#d9c25b", font=("Microsoft Sans Serif", 38))
    saldo.place(relx=0.15, rely=0.765, anchor="center")
    ctk.CTkFrame(janela,fg_color="#1a1a1a", corner_radius=0, border_color="#7ad470",border_width=3).place(relx=0.6,rely=0.6,relwidth=0.256,relheight=0.7,anchor="center")
    ctk.CTkLabel(janela, text="Deposit",fg_color="#1a1a1a",text_color="white", font=("Arial Rounded MT Bold", 28)).place(relx=0.51, rely=0.4, anchor="center")
    ctk.CTkLabel(janela, text="Add cash💸", fg_color="#1a1a1a", text_color="green",font=("Arial Regular", 32)).place(relx=0.6, rely=0.3, anchor="center")
    def validar(texto):
        if texto in ("", "🪙Ex: 34.50"): return True
        if not texto.replace(".", "", 1).isdigit(): return False
        return "." not in texto or len(texto.split(".")[-1]) <= 2
    vcmd = (janela.register(validar), "%P")
    deposito = ctk.CTkEntry(janela, placeholder_text="🪙Ex: 34.50", font=("Arial Regular", 28), validate ="key", validatecommand=vcmd)
    deposito.place(relx =0.6, rely=0.48,relwidth=0.240,relheight=0.105, anchor = "center")
    sendDeposit = ctk.CTkButton(janela,text="DEPOSIT", text_color="#1a1a1a", fg_color="#2fc91e",bg_color="#121212", corner_radius=50, hover_color="#0dd62b", command=depositod)
    sendDeposit.place(relx=0.6,rely=0.7,relwidth=0.216,relheight=0.08,anchor="center")
    botao_abrir = ctk.CTkButton( janela,text="🖌",corner_radius=15,font=("Arial", 24),text_color="white",hover_color="#555555",fg_color="#2d3030", bg_color="transparent",command=alternar_overlay)
    botao_abrir.place(relx=0.22, rely=0.46,relwidth=0.042,relheight=0.062, anchor="center")

def game():
    for elemento in janela.winfo_children():
        elemento.destroy()
    dados = funcio.execute(
        "SELECT username, pp FROM base WHERE email = ? ",
        (e,)
    )
    data = funcio.fetchone()
    janela.configure(fg_color="#141c24")
    frameLobby = ctk.CTkFrame(janela, fg_color="#141c24", corner_radius=0)
    frameLobby.place(relx=0.0, rely=0.0, relwidth=1.0,relheight=0.15, anchor="nw")

    bordaframeHO = ctk.CTkFrame(janela, fg_color="white", corner_radius=0)
    bordaframeHO.place(relx=0.0, rely=0.11, relwidth=1.0,relheight=0.003, anchor="nw")
    bordaframeVE = ctk.CTkFrame(janela, fg_color="white", corner_radius=0)
    bordaframeVE.place(relx=0.1, rely=0.11, relwidth=0.002, relheight=0.9, anchor="nw")


    botao3traco = ctk.CTkButton(frameLobby,fg_color="#141c24", text="≡", font=("Agency FB", 73, "bold"), hover_color="#141c24")
    botao3traco.place(relx=0.03,rely=0.305,anchor="center")
    ctk.CTkLabel(frameLobby, text="Grand\n       Jaguar",fg_color="#141c24", font=("Agency FB", 35, "bold")).place(relx=0.12,rely=0.345,anchor="center")
    ctk.CTkLabel(frameLobby, text="🐯", text_color="Orange", fg_color="#141c24", font=("Agency FB", 43, "bold")).place(relx=0.08, rely=0.345, anchor="center")

    botao_casino = ctk.CTkButton(frameLobby, text="♠cassino",font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9", fg_color="#141c24",hover_color="#d60222")
    botao_casino.place(relx=0.3,rely=0.5,anchor="center")
    botao_esporte = ctk.CTkButton(frameLobby, text="🏀esportes",font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9", fg_color="#141c24",hover_color="#d60222")
    botao_esporte.place(relx=0.38,rely=0.5,anchor="center")

    profilepicture = ctk.CTkButton(frameLobby,text=f"{data[1]}",font=("Arial Regular",50, "bold"), fg_color="#141c24",hover_color="#141c24",command=userInfo)
    profile = ctk.CTkButton(frameLobby, text=f"Welcome, {data[0]}!",font=("Arial Regular",20), fg_color="#141c24",hover_color="#141c24",command=userInfo)
    profilepicture.place(relx=0.83,rely=0.5,anchor = "center")
    profile.place(relx=0.9,rely=0.5,anchor = "center")

    frameAdd = ctk.CTkFrame(janela, fg_color="orange", corner_radius=10)
    frameAdd.place(relx=0.55, rely=0.3, relwidth=0.8, relheight=0.3, anchor="center")
    frameAdd = ctk.CTkFrame(janela, fg_color="orange", corner_radius=10)
    frameAdd.place(relx=0.55, rely=0.3, relwidth=0.8, relheight=0.3, anchor="center")
    ctk.CTkLabel(frameAdd, text="Primeiro cassino\n honesto\n do Brasil!", font=("Arial Black", 38)).place(relx=0.15,rely=0.5,anchor="center")
    ctk.CTkLabel(janela, text="Populares", font=("Century Gothic", 28, "bold")).place(relx=0.15, rely=0.54,anchor="center")
    caca = ctk.CTkButton(janela, text=f"{"\n" * 8}Caça-Níquel", command=niquel, font=("Lucida Sans", 32, "bold"),fg_color="#d4374f", hover_color="#d4374f")
    caca.place(relx=0.225, rely=0.78, relwidth=0.176, relheight=0.415, anchor="center")
    caca._canvas.configure(highlightthickness=0)
    icone_niquel = ctk.CTkButton(janela, text="🎰", font=("Century Gothic", 60, "bold"), fg_color="#d4374f",text_color="white", hover_color="#d4374f", command=niquel, corner_radius=0,border_width=0, border_spacing=0)
    icone_niquel.place(relx=0.225, rely=0.73, relwidth=0.138, relheight=0.104, anchor="center")
    icone_niquel._canvas.configure(highlightthickness=0)
    cavalinhos = ctk.CTkButton(janela, text=f"{"\n" * 8}Cavalinhos", font=("Lucida Sans", 32, "bold"),fg_color="#37d444", hover_color="#37d444", command=cavalo)
    cavalinhos.place(relx=0.42, rely=0.78, relwidth=0.176, relheight=0.415, anchor="center")
    cavalinhos._canvas.configure(highlightthickness=0)
    icone_cavalo = ctk.CTkButton(janela, text="🎠", font=("Century Gothic", 60), fg_color="#37d444",text_color="#61360e", hover_color="#37d444", command=cavalo, corner_radius=0,border_width=0, border_spacing=0)
    icone_cavalo.place(relx=0.42, rely=0.73, relwidth=0.138, relheight=0.104, anchor="center")
    icone_cavalo._canvas.configure(highlightthickness=0)


def niquel():
    for elemento in janela.winfo_children():
        elemento.destroy()
    janela.configure(fg_color="#141c24")
    frameLobby = ctk.CTkFrame(janela, fg_color="#141c24", corner_radius=0)
    frameLobby.place(relx=0.0, rely=0.0, relwidth=1.0,relheight=0.15, anchor="nw")

    bordaframeHO = ctk.CTkFrame(janela, fg_color="white", corner_radius=0)
    bordaframeHO.place(relx=0.0, rely=0.11, relwidth=1.0,relheight=0.003, anchor="nw")

    botao3traco = ctk.CTkButton(frameLobby, fg_color="#141c24", text="≡", font=("Agency FB", 73, "bold"),hover_color="#141c24")
    botao3traco.place(relx=0.03, rely=0.305, anchor="center")
    ctk.CTkLabel(frameLobby, text="Grand\n       Jaguar", fg_color="#141c24", font=("Agency FB", 35, "bold")).place(relx=0.12, rely=0.345, anchor="center")
    ctk.CTkButton(frameLobby, text="🐯", text_color="Orange", fg_color="#141c24",command= game, hover_color="#141c24", font=("Agency FB", 43, "bold")).place(relx=0.08, rely=0.345,relwidth=0.042, anchor="center")

    botao_casino = ctk.CTkButton(frameLobby, text="♠cassino", font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9",fg_color="#141c24", hover_color="#d60222")
    botao_casino.place(relx=0.3, rely=0.50, anchor="center")
    botao_esporte = ctk.CTkButton(frameLobby, text="🏀esportes", font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9",fg_color="#141c24", hover_color="#d60222")
    botao_esporte.place(relx=0.38, rely=0.50, anchor="center")

    principal = ctk.CTkFrame(janela, fg_color="#910109", corner_radius=0)
    principal.place(relx=0.5, rely=0.574,relwidth=0.35,relheight=0.9,anchor = "center")
    wpp = ctk.CTkFrame(principal,fg_color="#c21502")
    wpp.place(relx=0.5,rely=0.425,relwidth=1.0,relheight=0.762,anchor="center")
    slots = ctk.CTkFrame(janela, fg_color="#d4bfa3",corner_radius=0)
    slots.place(relx=0.5,rely=0.5,relwidth=0.3,relheight=0.6,anchor="center")
    barra1 = ctk.CTkFrame(slots,fg_color="#ffd900", border_color="#ff9500", border_width=3, corner_radius=0)
    barra1.place(relx=0.333,rely=0.5,relwidth=0.016,relheight=1.0,anchor="center")
    barra2 = ctk.CTkFrame(slots,fg_color="#ffd900", border_color="#ff9500", border_width=3, corner_radius=0)
    barra2.place(relx=0.6659,rely=0.5,relwidth=0.016,relheight=1.0,anchor="center")

    play = ctk.CTkButton(principal,text="↺",fg_color="#4da616", corner_radius=40, font=("Times New Roman", 70), text_color="#ffc800",hover_color="#66c928")
    play.place(relx=0.5,rely=0.85,relwidth=0.145,relheight=0.085,anchor="center")
def cavalo():
    for elemento in janela.winfo_children():
        elemento.destroy()
    janela.configure(fg_color="#141c24")
    frameLobby = ctk.CTkFrame(janela, fg_color="#141c24", corner_radius=0)
    frameLobby.place(relx=0.0, rely=0.0, relwidth=1.0,relheight=0.15, anchor="nw")

    bordaframeHO = ctk.CTkFrame(janela, fg_color="white", corner_radius=0)
    bordaframeHO.place(relx=0.0, rely=0.11, relwidth=1.0,relheight=0.003, anchor="nw")

    botao3traco = ctk.CTkButton(frameLobby, fg_color="#141c24", text="≡", font=("Agency FB", 73, "bold"),hover_color="#141c24")
    botao3traco.place(relx=0.03, rely=0.305, anchor="center")
    ctk.CTkLabel(frameLobby, text="Grand\n       Jaguar", fg_color="#141c24", font=("Agency FB", 35, "bold")).place(relx=0.12, rely=0.345, anchor="center")
    ctk.CTkButton(frameLobby, text="🐯", text_color="Orange", fg_color="#141c24",command= game, hover_color="#141c24", font=("Agency FB", 43, "bold")).place(relx=0.08, rely=0.345,relwidth=0.042, anchor="center")

    botao_casino = ctk.CTkButton(frameLobby, text="♠cassino", font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9",fg_color="#141c24", hover_color="#d60222")
    botao_casino.place(relx=0.3, rely=0.50, anchor="center")
    botao_esporte = ctk.CTkButton(frameLobby, text="🏀esportes", font=("Lucida Sans", 21, "bold"), text_color="#c9c9c9",fg_color="#141c24", hover_color="#d60222")
    botao_esporte.place(relx=0.38, rely=0.50, anchor="center")

    principal = ctk.CTkFrame(janela, fg_color="#24282b")
    principal.place(relx=0.5, rely=0.5,relwidth=0.547,relheight=0.6, anchor="center")
    apostaframe = ctk.CTkFrame(janela,fg_color="#24282b")
    apostaframe.place(relx=0.5,rely=0.5,relwidth=0.647,relheight=0.5,anchor="center")

    corredor_escolhido = ctk.StringVar(value="- - -")

    lbl_escolha = ctk.CTkLabel(
        apostaframe,
        text="Escolha o Cavalinho:",
        font=("Arial", 12, "bold"),
        corner_radius=0
    )
    lbl_escolha.place(relx=0.25, rely=0.05, anchor="w")

    menu_corredores = ctk.CTkOptionMenu(
        apostaframe,
        corner_radius=0,
        button_hover_color="#24282b",
        variable=corredor_escolhido,
        values=["Gordiço ", "Felipe", "Omni-man","Putrefação das trevas","Bob"]
    )
    menu_corredores.place(relx=0.4, rely=0.05, anchor="w")

    pista = ctk.CTkFrame(janela, fg_color="#1a1a1a")
    pista.place(relx=0.5, rely=0.5, relwidth=0.425,relheight=0.538, anchor="center")
    pista.pack_propagate(False)

    c1 = ctk.CTkButton(pista, text="🐴", fg_color="red", corner_radius=20, font=("Arial", 24, "bold"))
    c1._canvas.config(width=40, height=40)
    c1.place(relx=0.022, rely=0.057, relwidth=0.1, relheight=0.114)

    c2 = ctk.CTkButton(pista, text="🐴", fg_color="blue", corner_radius=20, font=("Arial", 24, "bold"))
    c2._canvas.config(width=40, height=40)
    c2.place(relx=0.022, rely=0.228, relwidth=0.1, relheight=0.114)

    c3 = ctk.CTkButton(pista, text="🐴", fg_color="darkred", corner_radius=20, font=("Arial", 24, "bold"))
    c3._canvas.config(width=40, height=40)
    c3.place(relx=0.022, rely=0.400, relwidth=0.1, relheight=0.114)

    c4 = ctk.CTkButton(pista, text="🐴", fg_color="green", corner_radius=20, font=("Arial", 24, "bold"))
    c4._canvas.config(width=40, height=40)
    c4.place(relx=0.022, rely=0.571, relwidth=0.1, relheight=0.114)

    c5 = ctk.CTkButton(pista, text="🐴", fg_color="brown", corner_radius=20, font=("Arial", 24, "bold"))
    c5._canvas.config(width=40, height=40)
    c5.place(relx=0.022, rely=0.743, relwidth=0.1, relheight=0.114)

    btn_iniciar = ctk.CTkButton(janela, text="CORRER! 🏁", font=("Arial", 16, "bold"), fg_color="#4da616", hover_color="#3d8512")
    btn_iniciar.place(relx=0.5, rely=0.8, relwidth=0.15, relheight=0.06, anchor="center")

lobby()
janela.after(0, lambda: janela.state("zoomed"))
janela.mainloop()
