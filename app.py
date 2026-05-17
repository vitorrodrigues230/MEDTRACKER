from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Lista para armazenar os medicamentos na memória
medicamentos_cadastrados = []

def buscar_cep(cep: str) -> dict:
    """Consome a API pública do ViaCEP"""
    cep_limpo = "".join(filter(str.isdigit, cep))
    if len(cep_limpo) != 8:
        return {"erro": "CEP inválido."}
    
    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep_limpo}/json/", timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" not in dados:
                return {
                    "logradouro": dados.get("logradouro"),
                    "cidade": dados.get("localidade"),
                    "uf": dados.get("uf")
                }
    except requests.RequestException:
        return {"erro": "Erro de conexão."}
    
    return {"erro": "CEP não encontrado."}

@app.route("/", methods=["GET", "POST"])
def index():
    # Se o usuário clicou no botão do formulário (POST)
    if request.method == "POST":
        nome = request.form.get("nome")
        horario = request.form.get("horario")
        cep = request.form.get("cep")
        
        # O Python busca os dados na API externa
        endereco = buscar_cep(cep) if cep else {}
        
        # Salva o cadastro
        medicamentos_cadastrados.append({
            "nome": nome,
            "horario": horario,
            "endereco": endereco
        })
        
    # Envia a tela HTML para o navegador, passando a lista de medicamentos
    return render_template("index.html", medicamentos=medicamentos_cadastrados)

if __name__ == "__main__":
    # Roda o servidor web na sua máquina
    app.run(debug=True)