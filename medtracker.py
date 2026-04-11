class SistemaMedTracker:
    def __init__(self):
        # Lista que armazena os dicionários de medicamentos
        self.medicamentos = []

    def adicionar_medicamento(self, nome, horario):
        # Validação simples para garantir que o nome não esteja vazio
        if not nome:
            return "Erro: O nome do medicamento não pode ser vazio."
        
        novo_med = {"nome": nome, "horario": horario}
        self.medicamentos.append(novo_med)
        return f"Medicamento {nome} adicionado com sucesso às {horario}."

    def listar_medicamentos(self):
        # Retorna uma mensagem amigável caso a lista esteja vazia
        if not self.medicamentos:
            return "Nenhum medicamento cadastrado."
        
        lista = "\n".join([f"- {m['nome']} às {m['horario']}" for m in self.medicamentos])
        return f"Medicamentos agendados:\n{lista}"