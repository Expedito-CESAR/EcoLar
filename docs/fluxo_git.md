# Fluxo Git — Projeto EcoLar

O projeto EcoLar utiliza Git e GitHub para controle de versão, organização do desenvolvimento e colaboração entre os integrantes da equipe.

---

# Objetivos do Fluxo Git

O fluxo adotado possui os seguintes objetivos:

* organizar o desenvolvimento da equipe;
* reduzir conflitos entre alterações;
* manter estabilidade do projeto;
* facilitar integração das funcionalidades;
* permitir desenvolvimento simultâneo.

---

# Estrutura de Branches

O projeto utiliza uma estrutura simples baseada em três níveis de branches:

```plaintext
main
DEV
branch-pessoal
```

---

# 1. Branch Main

## Objetivo

A branch `main` representa a versão estável e final do sistema.

Ela deve conter apenas:

* funcionalidades concluídas;
* código testado;
* versões prontas para entrega.

## Regras da Main

* nunca desenvolver diretamente na `main`;
* nunca enviar funcionalidades incompletas;
* realizar merge apenas de versões estáveis.

---

# 2. Branch DEV

## Objetivo

A branch `DEV` é utilizada para integração do desenvolvimento da equipe.

Todas as funcionalidades passam primeiro pela `DEV` antes de chegar à `main`.

## Funções da DEV

* integrar funcionalidades;
* validar funcionamento geral;
* centralizar o desenvolvimento do projeto;
* preparar versões para testes.

---

# 3. Branches Individuais

## Objetivo

Cada integrante possui uma branch própria para desenvolvimento das funcionalidades sob sua responsabilidade.

Isso permite:

* desenvolvimento isolado;
* melhor organização;
* redução de conflitos;
* modularização do trabalho.

## Padrão de Nome

```plaintext
branch-expedito
branch-lucas
branch-mario
branch-raquel
```

---

# Criação das Branches Individuais

As branches pessoais devem sempre ser criadas a partir da `DEV`.

## Atualizar DEV

```bash
git checkout DEV
git pull origin DEV
```

## Criar Branch Pessoal

```bash
git checkout -b branch-nome
```

Exemplo:

```bash
git checkout -b branch-raquel
```

## Enviar para o GitHub

```bash
git push origin branch-raquel
```

---

# Fluxo Correto de Trabalho

## 1. Atualizar DEV

Antes de iniciar qualquer desenvolvimento:

```bash
git checkout DEV
git pull origin DEV
```

---

## 2. Atualizar Branch Pessoal

Exemplo:

```bash
git checkout branch-raquel
git merge DEV
```

Objetivo:
Trazer as atualizações mais recentes da equipe para a branch pessoal.

---

## 3. Desenvolver Funcionalidade

Cada integrante desenvolve as funcionalidades sob sua responsabilidade.

---

## 4. Adicionar Alterações

```bash
git add .
```

---

## 5. Criar Commit

```bash
git commit -m "feat: create report service"
```

---

## 6. Enviar Alterações

```bash
git push origin branch-raquel
```

---

## 7. Integrar na DEV

Após testes e validações:

```bash
git checkout DEV
git merge branch-raquel
```

---

# Merge Final para Main

Quando o sistema estiver:

* estável;
* validado;
* testado;
* pronto para entrega;

deve ser realizado o merge final:

```bash
git checkout main
git merge DEV
```

Fluxo final:

```plaintext
DEV
↓
main
```

---

# Regras Importantes

* nunca desenvolver diretamente na `main`;
* sempre atualizar a `DEV` antes de iniciar o desenvolvimento;
* sempre atualizar a branch pessoal antes de programar;
* realizar commits pequenos e organizados;
* testar funcionalidades antes de realizar merge;
* evitar alterar arquivos de responsabilidade de outros integrantes sem alinhamento prévio.

---

# Estratégia Utilizada

O projeto EcoLar utiliza um fluxo simplificado baseado em GitHub Flow com integração centralizada na branch `DEV`.
