# MEDTRACKER 💊

O **MedTracker** é um sistema desenvolvido para auxiliar idosos e cuidadores no controle e agendamento de medicamentos. Este projeto foi construído com foco em boas práticas de Engenharia de Software, utilizando testes automatizados e workflows de Integração Contínua (CI).

## 🚀 Funcionalidades

* **Cadastro de Medicamentos:** Adição de remédios com validação de nome e horário.
* **Listagem Inteligente:** Visualização de todos os medicamentos agendados para o dia.
* **Validação de Dados:** O sistema impede o cadastro de itens sem nome, garantindo a integridade dos dados.

## 🛠️ Tecnologias Utilizadas

Para garantir a qualidade e a padronização do código, o projeto utiliza:

* **Linguagem:** Python 3.10+.
* **Testes Unitários:** [Pytest](https://pytest.org/) para validar a lógica de negócio.
* **Análise Estática (Linting):** [Ruff](https://beta.ruff.rs/docs/) para garantir que o código siga os padrões PEP8.
* **CI/CD:** [GitHub Actions](https://github.com/features/actions) configurado para automação.

## 🏗️ Estrutura do Repositório

* `medtracker.py`: Contém a classe principal `SistemaMedTracker` e a lógica do sistema.
* `tests/`: Pasta com os scripts de testes automatizados.
* `.github/workflows/ci.yml`: Arquivo de configuração da automação do GitHub.
* `requirements.txt`: Lista de dependências necessárias.
* `VERSION`: Arquivo de controle de versão (1.0.0).


## ⚙️ Como Executar o Projeto

### 1. Instalação
Clone o repositório e instale as dependências:
```bash
git clone [https://github.com/vitorrodrigues230/MEDTRACKER.git](https://github.com/vitorrodrigues230/MEDTRACKER.git)
cd MEDTRACKER
pip install -r requirements.txt

## ⚙️ 2. Executando Testes

Para garantir que a lógica do sistema permaneça íntegra após qualquer modificação, utilizamos o **Pytest**. Siga os passos abaixo para rodar a bateria de testes localmente:

1. **Certifique-se de estar com o ambiente virtual ativo.**
2. **Execute o comando abaixo no terminal da raiz do projeto:**

```bash
python -m pytest

## 👨‍💻 Autor

**Vitor Rodrigues Ferreira**
* Estudante de Engenharia de Software no UniCEUB.


