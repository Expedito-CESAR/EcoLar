# EcoLar

Sistema acadêmico desenvolvido em Python com foco no monitoramento e conscientização sobre consumo energético residencial.

## Equipe 4

- Expedito Ferraz Gominho Paes - Gestor do Projeto, Pesquisa e Documentação

- Lucas Veiga De Aquino Souza Leite - Desenvolvedor de software

- Mario Sergio Fernandes Mendonça - Analista Técnico

- Raquel Moura Lins Acioli - Designer de Experiência (UX)


## Objetivo do Projeto

O EcoLar tem como objetivo auxiliar usuários no acompanhamento do consumo energético de aparelhos elétricos, promovendo maior conscientização sobre hábitos de consumo e incentivando práticas mais sustentáveis através de cálculos de consumo, estimativas de custo e classificação energética.


## Funcionalidades do Sistema

- Cadastro de usuários
- Cadastro de aparelhos elétricos
- Leitura e manipulação de arquivos TXT
- Atualização de dados
- Remoção de registros
- Cálculo de consumo energético (kWh)
- Estimativa de custo mensal
- Classificação energética (A+ até E)
- Simulação simples de economia
- Tratamento de erros e exceções


## Tecnologias Utilizadas

- Python
- Git
- GitHub
- Visual Studio Code
- Arquivos TXT para persistência de dados


## Estrutura do Projeto

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
│   ├── report_view.py
│
├── docs
|   ├── arquitetura.md
|   ├── guia_consumo_energia.md
|   ├── fluxo_git.md
