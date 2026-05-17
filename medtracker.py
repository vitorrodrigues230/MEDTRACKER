import requests
class SistemaMedTracker:
    def __init__(self):
        
        self.medicamentos = []

    def adicionar_medicamento(self, nome, horario):
        
        if not nome:
            return "Erro: O nome do medicamento não pode ser vazio."
        
        novo_med = {"nome": nome, "horario": horario}
        self.medicamentos.append(novo_med)
        return f"Medicamento {nome} adicionado com sucesso às {horario}."

    def listar_medicamentos(self):
        
        if not self.medicamentos:
            return "Nenhum medicamento cadastrado."
        
        lista = "\n".join([f"- {m['nome']} às {m['horario']}" for m in self.medicamentos])
        return f"Medicamentos agendados:\n{lista}"
def buscar_endereco_por_cep(self, cep: str) -> dict:
        
        cep_limpo = "".join(filter(str.isdigit, cep))

        if len(cep_limpo) != 8:
            return {"erro": "CEP inválido. Deve conter 8 dígitos."}

        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        try:
            resposta = requests.get(url, timeout=5)
            if resposta.status_code == 200:
                dados = resposta.json()
                if "erro" in dados:
                    return {"erro": "CEP não encontrado."}
                return {
                    "logradouro": dados.get("logradouro"),
                    "bairro": dados.get("bairro"),
                    "cidade": dados.get("localidade"),
                    "estado": dados.get("uf")
                }
            return {"erro": "Não foi possível conectar ao serviço de CEP."}
        except requests.RequestException:
            return {"erro": "Erro de conexão com a internet."}