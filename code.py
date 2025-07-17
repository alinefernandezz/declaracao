import webbrowser
from datetime import datetime
import os

# 💬 Dados personalizados
pessoa = "Bruna"  # Substitua pelo nome real
foto1 = "fotos/foto1.png"
foto2 = "fotos/foto2.png"

# Verifica se os arquivos existem
if not (os.path.exists(foto1) and os.path.exists(foto2)):
    print("❌ Verifique se as fotos estão na pasta 'fotos' com os nomes corretos (foto1.png e foto2.png).")
    exit()

mensagem = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>Para você, {pessoa}</title>
    <style>
        body {{
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        h1 {{
            font-size: 3em;
            margin: 20px 0 10px;
            color: #d6336c;
        }}
        p {{
            font-size: 1.4em;
            max-width: 700px;
            text-align: center;
        }}
        .heart {{
            font-size: 4em;
            margin-bottom: 20px;
            animation: pulse 1.2s infinite alternate;
        }}
        @keyframes pulse {{
            from {{ transform: scale(1); }}
            to {{ transform: scale(1.15); }}
        }}
        .fotos {{
            display: flex;
            gap: 20px;
            margin: 30px 0;
            flex-wrap: wrap;
            justify-content: center;
        }}
        .fotos img {{
            width: 300px;
            height: auto;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }}
        .assinatura {{
            margin-top: 40px;
            font-style: italic;
            font-size: 1.1em;
        }}
    </style>
</head>
<body>
    <div class="heart">💖</div>
    <h1>Oi, {pessoa}!</h1>
    <p>Hoje só queria te lembrar de algo muito simples... mas muito verdadeiro:</p>
    <h1>✨ EU TE AMO MUITO MEU AMOR✨</h1>
    <p>Essas fotos guardam momentos especiais, e ainda vamos criar muitos outros juntas.</p>

    <div class="fotos">
        <img src="{foto1}" alt="Foto nossa 1">
        <img src="{foto2}" alt="Foto nossa 2">
    </div>

    <p class="assinatura">Com carinho,<br>💌 Alguém que te ama muito</p>
</body>
</html>
"""

# 📝 Nome do arquivo HTML gerado
filename = f"para_{pessoa.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

# Salva o arquivo
with open(filename, "w", encoding="utf-8") as f:
    f.write(mensagem)

# Abre no navegador
webbrowser.open(f"file://{os.path.abspath(filename)}")
print(f"✅ Mensagem gerada com sucesso: {filename}")
