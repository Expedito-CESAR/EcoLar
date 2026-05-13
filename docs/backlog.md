# Backlog do Projeto EcoLar

## Visão Geral

O backlog do projeto EcoLar reúne todas as funcionalidades, melhorias, correções e entregas necessárias para o desenvolvimento completo do sistema.

As atividades foram organizadas considerando:
- requisitos funcionais;
- requisitos não funcionais;
- critérios de avaliação;
- arquitetura modular do projeto;
- cronograma oficial da disciplina.

O objetivo do backlog é:
- organizar o desenvolvimento;
- acompanhar evolução do sistema;
- facilitar divisão da equipe;
- evitar retrabalho;
- garantir rastreabilidade das funcionalidades.

---

# Status Utilizados

| Status | Descrição |
|---|---|
| Não iniciado | A atividade ainda não começou |
| Em andamento | A atividade está sendo desenvolvida |
| Concluído | A atividade foi finalizada |
| Bloqueado | A atividade depende de outra tarefa |

---

# Prioridades

| Prioridade | Significado |
|---|---|
| Alta | Essencial para funcionamento do sistema |
| Média | Importante para estabilidade e organização |
| Baixa | Melhoria complementar |

---

# BACKLOG GERAL

---

# 1. Arquitetura e Estruturação

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-001 | Definir arquitetura modular do sistema | Expedito | Alta | Concluído |
| BL-002 | Organizar estrutura de pastas | Expedito / Raquel | Alta | Concluído |
| BL-003 | Definir separação em camadas | Expedito | Alta | Concluído |
| BL-004 | Criar arquitetura repositories/services/controllers/views | Expedito | Alta | Concluído |
| BL-005 | Estruturar fluxo Git e branches | Expedito | Alta | Concluído |
| BL-006 | Configurar padrão de nomenclatura | Expedito | Média | Em andamento |

---

# 2. Persistência de Dados TXT

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-007 | Criar base de aparelhos TXT | Raquel | Alta | Concluído |
| BL-008 | Criar categorias TXT | Raquel | Alta | Concluído |
| BL-009 | Criar níveis de consumo TXT | Raquel | Alta | Concluído |
| BL-010 | Criar base de dicas TXT | Raquel | Média | Concluído |
| BL-011 | Implementar leitura genérica TXT | Expedito | Alta | Concluído |
| BL-012 | Implementar escrita TXT | Mario | Alta | Em andamento |
| BL-013 | Revisar encoding UTF-8 | Mario | Média | Não iniciado |
| BL-014 | Validar consistência de delimitadores | Mario | Média | Não iniciado |
| BL-015 | Revisar persistência geral | Mario | Alta | Não iniciado |

---

# 3. Repositories

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-016 | Implementar user_repository.py | Mario | Alta | Não iniciado |
| BL-017 | Implementar appliance_repository.py | Mario | Alta | Não iniciado |
| BL-018 | Implementar user_appliance_repository.py | Mario | Alta | Não iniciado |
| BL-019 | Implementar category_repository.py | Mario | Média | Não iniciado |
| BL-020 | Implementar history_repository.py | Mario | Média | Não iniciado |
| BL-021 | Revisar persistência dos repositories | Mario | Alta | Não iniciado |

---

# 4. Services e Regras de Negócio

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-022 | Finalizar user_service.py | Lucas | Alta | Não iniciado |
| BL-023 | Implementar cálculo de consumo kWh | Lucas | Alta | Não iniciado |
| BL-024 | Implementar cálculo mensal | Lucas | Alta | Não iniciado |
| BL-025 | Implementar classificação energética | Lucas | Alta | Não iniciado |
| BL-026 | Implementar simulação de economia | Lucas | Média | Não iniciado |
| BL-027 | Implementar recommendation_service.py | Lucas | Média | Não iniciado |
| BL-028 | Revisar regras de negócio | Lucas | Alta | Não iniciado |

---

# 5. Controllers e Fluxo do Sistema

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-029 | Finalizar user_controller.py | Expedito | Alta | Em andamento |
| BL-030 | Criar menu_controller.py | Expedito | Alta | Não iniciado |
| BL-031 | Integrar controllers com services | Expedito | Alta | Não iniciado |
| BL-032 | Integrar controllers com repositories | Expedito | Alta | Não iniciado |
| BL-033 | Revisar fluxo principal do sistema | Expedito | Alta | Não iniciado |

---

# 6. Views e Navegação Terminal

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-034 | Criar menu textual principal | Raquel | Alta | Não iniciado |
| BL-035 | Organizar exibição textual | Raquel | Média | Não iniciado |
| BL-036 | Padronizar mensagens do sistema | Raquel | Média | Não iniciado |
| BL-037 | Melhorar navegação terminal | Raquel | Média | Não iniciado |
| BL-038 | Revisar experiência textual do usuário | Raquel | Média | Não iniciado |

---

# 7. Validações e Tratamento de Erros

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-039 | Centralizar validações em validators.py | Expedito | Alta | Não iniciado |
| BL-040 | Validar entradas vazias | Expedito | Alta | Não iniciado |
| BL-041 | Validar e-mails | Expedito | Média | Não iniciado |
| BL-042 | Validar tipos numéricos | Expedito | Média | Não iniciado |
| BL-043 | Tratar arquivos inexistentes | Mario | Média | Não iniciado |
| BL-044 | Tratar inconsistências TXT | Mario | Média | Não iniciado |
| BL-045 | Revisar mensagens de erro | Raquel | Média | Não iniciado |

---

# 8. Integração e Estabilização

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-046 | Integrar repositories e services | Expedito | Alta | Não iniciado |
| BL-047 | Integrar controllers e views | Expedito | Alta | Não iniciado |
| BL-048 | Validar fluxo completo | Expedito | Alta | Não iniciado |
| BL-049 | Revisar integração geral | Todos | Alta | Não iniciado |
| BL-050 | Executar testes ponta a ponta | Todos | Alta | Não iniciado |
| BL-051 | Corrigir erros críticos finais | Todos | Alta | Não iniciado |
| BL-052 | Criar backup e congelar versão final | Expedito | Alta | Não iniciado |

---

# 9. Testes

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-053 | Criar test_users.py | Lucas | Média | Não iniciado |
| BL-054 | Criar test_consumption.py | Lucas | Média | Não iniciado |
| BL-055 | Criar test_reports.py | Lucas | Média | Não iniciado |
| BL-056 | Revisar estabilidade do sistema | Todos | Alta | Não iniciado |

---

# 10. Documentação Técnica

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-057 | Criar arquitetura.md | Expedito | Alta | Em andamento |
| BL-058 | Criar fluxo_git.md | Expedito | Alta | Em andamento |
| BL-059 | Criar backlog.md | Expedito | Alta | Em andamento |
| BL-060 | Criar regras_negocio.md | Expedito | Média | Não iniciado |
| BL-061 | Atualizar README.md | Expedito | Alta | Não iniciado |

---

# 11. GitHub e Organização da Equipe

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-062 | Criar branch DEV | Expedito | Alta | Concluído |
| BL-063 | Criar branches individuais | Expedito | Alta | Concluído |
| BL-064 | Organizar fluxo de merge | Expedito | Alta | Em andamento |
| BL-065 | Padronizar commits da equipe | Expedito | Média | Não iniciado |
| BL-066 | Revisar integração GitHub | Todos | Alta | Não iniciado |

---

# 12. Entrega e Apresentação

| ID | Atividade | Responsável | Prioridade | Status |
|---|---|---|---|---|
| BL-067 | Atualizar GitHub final | Expedito | Alta | Não iniciado |
| BL-068 | Preparar site da equipe | Raquel | Média | Não iniciado |
| BL-069 | Criar slides da apresentação | Todos | Alta | Não iniciado |
| BL-070 | Ensaiar apresentação final | Todos | Alta | Não iniciado |
| BL-071 | Revisar versão final para apresentação | Todos | Alta | Não iniciado |

---

# Objetivo Final do Backlog

O backlog do EcoLar busca garantir:
- organização do desenvolvimento;
- clareza das responsabilidades;
- rastreabilidade das funcionalidades;
- estabilidade da execução;
- alinhamento com os requisitos da disciplina;
- melhor controle das entregas;
- redução de conflitos entre membros da equipe;
- preparação adequada para apresentação final do projeto.