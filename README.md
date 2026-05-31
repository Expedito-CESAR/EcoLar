# EcoLar

Sistema acadêmico desenvolvido em Python com foco no monitoramento, análise e conscientização sobre consumo energético residencial.

---

# Equipe 4

* Expedito Ferraz Gominho Paes — Gestão do Projeto, Arquitetura do Sistema, Integração e Documentação

* Lucas Veiga de Aquino Souza Leite — Desenvolvimento de Software e Regras de Negócio

* Mario Sergio Fernandes Mendonça — Apoio Técnico e Pesquisa

* Raquel Moura Lins Acioli — Experiência do Usuário (UX), Interface Textual e Organização Visual

---

# Objetivo do Projeto

O EcoLar tem como objetivo auxiliar usuários no acompanhamento do consumo energético de aparelhos elétricos residenciais, promovendo maior conscientização sobre hábitos de consumo e incentivando práticas mais sustentáveis através de cálculos energéticos, estimativas de custo, relatórios e simulações de economia.

O sistema foi desenvolvido como projeto acadêmico da disciplina de Projeto 1 da CESAR School, utilizando arquitetura modular baseada em camadas para separação de responsabilidades.

---

# Principais Funcionalidades

## Usuários

* Cadastro de usuários
* Login simplificado
* Atualização de dados cadastrais
* Exclusão de conta

## Aparelhos

* Cadastro de aparelhos vinculados ao usuário
* Atualização de tempo de uso
* Remoção de aparelhos
* Organização por categorias

## Consumo Energético

* Cálculo real de consumo energético (kWh)
* Estimativa de custo mensal
* Classificação energética
* Comparação com média de consumo
* Simulação de economia energética

## Relatórios e Recomendações

* Relatórios de consumo por aparelho
* Recomendações de economia
* Simulações de redução de consumo
* Dicas de uso consciente de energia

## Persistência e Robustez

* Persistência em arquivos TXT
* Tratamento de erros e inconsistências
* Validação de entradas do usuário
* Padronização estrutural dos dados

---

# Tecnologias Utilizadas

* Python 3
* Git
* GitHub
* Visual Studio Code
* Arquivos TXT para persistência de dados

---

# Arquitetura do Projeto

O sistema foi desenvolvido utilizando arquitetura modular em camadas:

* **Views** → Interface textual e interação com o usuário
* **Controllers** → Controle do fluxo do sistema
* **Services** → Regras de negócio e cálculos
* **Repositories** → Persistência e manipulação dos arquivos TXT
* **Utils** → Funções auxiliares e validações

Essa organização busca facilitar manutenção, reutilização de código e separação de responsabilidades.

---

# Estrutura do Projeto

```plaintext
EcoLar/
│
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── appliances.txt
│   ├── categories.txt
│   ├── consumption_levels.txt
│   ├── history.txt
│   ├── tips.txt
│   ├── user_appliances.txt
│   ├── users.txt
│
├── repositories/
│   ├── __init__.py
│   ├── user_repository.py
│   ├── appliance_repository.py
│   ├── category_repository.py
│   ├── tip_repository.py
│   ├── history_repository.py
│   ├── consumption_repository.py
│   ├── user_appliance_repository.py
│
├── services/
│   ├── __init__.py
│   ├── user_service.py
│   ├── user_appliance_service.py
│   ├── appliance_service.py
│   ├── consumption_service.py
│   ├── energy_classification_service.py
│   ├── report_service.py
│   ├── simulation_service.py
│
├── controllers/
│   ├── __init__.py
│   ├── user_controller.py
│   ├── appliance_controller.py
│   ├── report_controller.py
│   ├── menu_controller.py
│   ├── energy_controller.py
│
├── utils/
│   ├── __init__.py
│   ├── formatter.py
│   ├── txt_handler.py
│   ├── validators.py
│
├── views/
│   ├── __init__.py
│   ├── appliance_view.py
│   ├── consumption_view.py
│   ├── menu_view.py
│   ├── user_view.py
│
├── docs/
│   ├── guia_consumo_energia.md
│   ├── fluxo_git.md
```

---

# Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/Expedito-CESAR/EcoLar.git
```

---

## 2. Acessar a pasta do projeto

```bash
cd EcoLar
```

---

## 3. Executar o sistema

```bash
python main.py
```

---

# Características Técnicas do Sistema

* Arquitetura modular em camadas
* Separação de responsabilidades
* Reutilização de funções
* Persistência baseada em TXT
* Tratamento de inconsistências estruturais
* Navegação textual interativa
* Validações centralizadas
* Organização para futura expansão

---

# Status do Projeto

Projeto em fase final de estabilização e testes integrados.

---

# Instituição

CESAR School
Graduação em Gestão da Tecnologia da Informação (GTI)
Disciplina: Projeto 1
