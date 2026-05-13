# Arquitetura do Sistema EcoLar

## Visão Geral

O EcoLar é um sistema acadêmico desenvolvido em Python com foco no monitoramento e conscientização sobre consumo energético residencial.

O sistema foi estruturado utilizando arquitetura modular em camadas, permitindo:
- organização do código;
- separação de responsabilidades;
- facilidade de manutenção;
- reutilização de funções;
- desenvolvimento paralelo da equipe;
- redução de conflitos no GitHub;
- maior estabilidade durante integração.

O projeto utiliza:
- Python;
- Git/GitHub;
- Visual Studio Code;
- Arquivos TXT como persistência de dados.

---

# Objetivo da Arquitetura

A arquitetura adotada busca garantir:
- desacoplamento entre módulos;
- separação clara das responsabilidades;
- facilidade de integração;
- manutenção simplificada;
- redução de retrabalho;
- organização estrutural;
- melhor colaboração entre os membros da equipe.

---

# Estrutura Geral do Projeto

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
├── models/
│   ├── __init__.py
│   ├── appliance.py
│   ├── user.py
│   ├── category.py
│   ├── tip.py
│   ├── consumption_level.py
│   ├── history.py
│   ├── user_appliance.py
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
│   ├── appliance_service.py
│   ├── consumption_service.py
│   ├── report_service.py
│   ├── recommendation_service.py
│   ├── history_service.py
│   ├── user_appliance_service.py
│
├── controllers/
│   ├── __init__.py
│   ├── user_controller.py
│   ├── appliance_controller.py
│   ├── report_controller.py
│   ├── menu_controller.py
│
├── utils/
│   ├── __init__.py
│   ├── constants.py
│   ├── formatter.py
│   ├── helpers.py
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
├── tests/
│   ├── test_users.py
│   ├── test_consumption.py
│   ├── test_reports.py
│
├── docs/
│   ├── arquitetura.md
│   ├── backlog.md
│   ├── fluxo_git.md
│   ├── regras_negocio.md

---

# Estrutura em Camadas

O sistema foi organizado utilizando separação em camadas.

Cada camada possui responsabilidades específicas.

---

# Fluxo da Arquitetura

Repositories
↓
Services
↓
Controllers
↓
Views

---

# Repositories

Responsáveis pela persistência e manipulação de dados.

Funções principais:

* leitura de arquivos TXT;
* escrita em arquivos TXT;
* atualização de dados;
* remoção de registros;
* persistência do sistema.

A camada repository não deve conter:

* lógica de negócio;
* regras do sistema;
* validações complexas.

---

## Arquivos

repositories/

---

## Exemplos

user_repository.py
appliance_repository.py
history_repository.py

---

# Services

Responsáveis pelas regras de negócio do sistema.

Funções principais:

* cálculos;
* processamento de dados;
* lógica energética;
* classificação de consumo;
* simulações;
* regras do sistema.

A camada service funciona como intermediária entre:

* repositories;
* controllers.

---

## Arquivos

services/

---

## Exemplos

consumption_service.py
report_service.py
user_service.py

---

# Controllers

Responsáveis pelo controle do fluxo do sistema.

Funções principais:

* receber entradas do usuário;
* controlar menus;
* chamar services;
* validar fluxo;
* integrar módulos.

A camada controller atua como ponte entre:

* views;
* services.

---

## Arquivos

controllers/

---

## Exemplos

user_controller.py
menu_controller.py

---

# Views

Responsáveis pela exibição textual do sistema.

Funções principais:

* organização visual do terminal;
* menus;
* exibição de dados;
* mensagens do sistema;
* relatórios textuais.

O sistema não utiliza interface gráfica.

Toda interação ocorre via terminal.

---

## Arquivos

views/

---

## Exemplos

menu_view.py
report_view.py

---

# Utils

Responsáveis por funções auxiliares reutilizáveis.

Funções principais:

* validações;
* manipulação TXT;
* formatação;
* helpers;
* constantes globais.

---

## Arquivos

utils/

---

## Exemplos

validators.py
formatter.py
txt_handler.py

---

# Models

Responsáveis pela representação estrutural dos dados.

Funções principais:

* organização lógica das entidades;
* padronização dos dados;
* estruturação dos objetos do sistema.

---

## Arquivos

models/

---

## Exemplos

user.py
appliance.py
history.py

---

# Data

Responsável pelo armazenamento persistente do sistema.

A persistência é realizada utilizando arquivos TXT.

---

## Arquivos

data/

---

## Exemplos

users.txt
appliances.txt
history.txt

---

# Tests

Responsáveis pela validação e testes do sistema.

Funções principais:

* testar funcionalidades;
* validar regras;
* verificar estabilidade;
* reduzir erros.

---

## Arquivos

tests/

---

# Docs

Responsáveis pela documentação técnica do projeto.

Funções principais:

* documentar arquitetura;
* registrar backlog;
* documentar fluxo Git;
* registrar regras de negócio.

---

## Arquivos

docs/

---

# Fluxo de Funcionamento do Sistema

O funcionamento geral do EcoLar segue o seguinte fluxo:

Usuário
↓
Views
↓
Controllers
↓
Services
↓
Repositories
↓
Arquivos TXT

---

# Fluxo de Desenvolvimento

O desenvolvimento da equipe foi organizado por responsabilidades arquiteturais.

Cada integrante atua prioritariamente em uma camada específica do sistema.

O objetivo é:

* reduzir conflitos;
* evitar retrabalho;
* permitir desenvolvimento paralelo;
* facilitar integração.

---

# Estrutura de Branches

O projeto utiliza a seguinte estrutura de branches:


main
↓
DEV
↓
branch-expedito
branch-lucas
branch-mario
branch-raquel


---

## main

Branch principal do projeto.

Responsável pela versão estável e final do sistema.

---

## DEV

Branch principal de desenvolvimento.

Responsável pela integração geral das funcionalidades desenvolvidas pela equipe.

---

## Branches Individuais

Cada integrante possui uma branch própria vinculada à branch `DEV`.

O objetivo é:

* evitar conflitos;
* reduzir sobrescrita de código;
* organizar responsabilidades;
* permitir integração controlada.

---

# Divisão da Equipe e Responsabilidades Técnicas

A equipe do projeto EcoLar foi organizada de forma modular, seguindo a arquitetura em camadas do sistema.

A divisão foi baseada em:

* arquitetura do sistema;
* separação de responsabilidades;
* fluxo Git da equipe;
* organização por camadas;
* estabilidade da integração.

---

# Expedito Ferraz Gominho Paes

## Função Geral no Projeto

* Gestor do Projeto;
* Arquiteto de Software;
* Responsável pela integração do sistema;
* Responsável pela documentação técnica.

---

## Função na Fase de Execução

* Desenvolver controllers;
* Centralizar validações;
* Integrar camadas do sistema;
* Revisar arquitetura;
* Gerenciar fluxo Git;
* Validar integração entre módulos;
* Coordenar estabilização do sistema;
* Supervisionar merges na branch `DEV`.

---

## Branch

branch-expedito


---

## Pastas de Responsabilidade

controllers/
docs/

---

## Arquivos Principais

controllers/user_controller.py
controllers/menu_controller.py

utils/validators.py

docs/arquitetura.md
docs/fluxo_git.md
docs/regras_negocio.md
docs/backlog.md

README.md
main.py

---

# Lucas Veiga De Aquino Souza Leite

## Função Geral no Projeto

* Desenvolvedor de Lógica de Negócio;
* Responsável pelas regras do sistema;
* Responsável pelos cálculos do EcoLar.

---

## Função na Fase de Execução

* Desenvolver services;
* Implementar cálculos de consumo;
* Implementar regras de negócio;
* Desenvolver lógica energética;
* Implementar simulações e classificações.

---

## Branch

branch-lucas

---

## Pastas de Responsabilidade

services/

---

## Arquivos Principais

services/user_service.py
services/appliance_service.py
services/consumption_service.py
services/report_service.py
services/recommendation_service.py
services/history_service.py
services/user_appliance_service.py

---

# Mario Sergio Fernandes Mendonça

## Função Geral no Projeto

* Analista Técnico;
* Responsável pela persistência;
* Responsável pela estrutura de dados.

---

## Função na Fase de Execução

* Desenvolver repositories;
* Implementar leitura e escrita TXT;
* Organizar persistência de dados;
* Revisar models;
* Garantir estabilidade da manipulação de arquivos.

---

## Branch

branch-mario

---

## Pastas de Responsabilidade

repositories/
models/
data/

---

## Arquivos Principais

repositories/user_repository.py
repositories/appliance_repository.py
repositories/category_repository.py
repositories/tip_repository.py
repositories/history_repository.py
repositories/consumption_repository.py
repositories/user_appliance_repository.py

models/user.py
models/appliance.py
models/category.py
models/tip.py
models/history.py
models/consumption_level.py
models/user_appliance.py

data/*.txt

---

# Raquel Moura Lins Acioli

## Função Geral no Projeto

* Organização de Experiência do Usuário em Terminal;
* Estruturação textual do sistema;
* Apoio em modelagem e organização dos dados.

---

## Função na Fase de Execução

* Desenvolver views do terminal;
* Organizar menus;
* Padronizar mensagens do sistema;
* Melhorar fluxo textual;
* Estruturar navegação do usuário;
* Auxiliar testes ponta a ponta.

---

## Branch

branch-raquel

---

## Pastas de Responsabilidade

views/

---

## Arquivos Principais

views/menu_view.py
views/user_view.py
views/report_view.py
views/appliance_view.py
views/consumption_view.py

utils/formatter.py

---

# Objetivos da Divisão Técnica

A estrutura adotada possui os seguintes objetivos:

* reduzir conflitos no GitHub;
* evitar retrabalho;
* permitir desenvolvimento paralelo;
* separar responsabilidades;
* facilitar integração;
* melhorar manutenção do sistema;
* estabilizar o fluxo de desenvolvimento;
* garantir organização até a entrega final.

---

# Fluxo de Desenvolvimento

Cada integrante:

* trabalha prioritariamente em suas próprias pastas;
* realiza commits em sua branch pessoal;
* envia alterações para integração na branch `DEV`.

O fluxo principal utilizado é:

branch pessoal
↓
DEV
↓
main

---

# Integração do Sistema

A integração geral do sistema é centralizada na branch `DEV`.

Após validação:

* o sistema é estabilizado;
* testes finais são executados;
* a versão final é integrada na branch `main`.

---

# Objetivo Final da Arquitetura

A arquitetura modular adotada no EcoLar busca garantir:

* organização estrutural;
* separação clara de responsabilidades;
* facilidade de manutenção;
* escalabilidade acadêmica;
* melhor colaboração entre os membros da equipe;
* maior estabilidade durante o desenvolvimento e apresentação final do projeto.
