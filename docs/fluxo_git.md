# Fluxo Git da Equipe EcoLar

O projeto EcoLar utiliza Git e GitHub como ferramentas de versionamento e colaboração entre os membros da equipe.

## O objetivo do fluxo Git

1. organizar o desenvolvimento;
2. evitar conflitos;
3. reduzir retrabalho;
4. manter estabilidade do projeto;
5. permitir trabalho simultâneo entre os membros da equipe.

## Estrutura de Branches

O projeto utuliza uma estrutura simples baseada em:

main
dev
branch-pessoal

1. Branch Main
Objetivo

A branch main representa a versão estável do sistema.

Ela deve conter apenas:

código funcional;
funcionalidades testadas;
versões prontas para entrega.
Regras da Main
Nunca desenvolver diretamente na main;
Nunca enviar código incompleto;
Apenas realizar merge de versões estáveis.

2. Branch Dev
Objetivo

A branch dev é utilizada para integração do desenvolvimento da equipe.

Todas as funcionalidades passam primeiro pela dev.

Funções da Dev
integrar funcionalidades;
validar funcionamento geral;
centralizar o desenvolvimento da equipe.

3. Branches individuais
Objetivo

Cada membro da equipe terá a própria branch onde desenvolverá aquilo que está em sua responsabilidade. 

Isso permitirá:
- desenvolvimento isolado;
- organização;
- redução de conflitos;
- modularização do trabalho.

Para maior oganização devem ser criadas com os seguintes títulos:

branch-expedito
branch-lucas
branch-mario
branch-raquel

## Criação das Branches individuais

Passo a Passo: As branches pessoais devem ser criadas sempre a partir da DEV.

MPORTANTE

Antes de criar qualquer branch pessoal:
git checkout DEV
git pull origin DEV

1. Ir para DEV

git checkout DEV

2. Criar branch pessoal

git checkout -b branch-"nome"

exemplo: git checkout -b branch-raquel


3. Enviar para o GitHub

git push origin branch-"nome" 

exemplo: git push origin branch-raquel

## Fluxo correto de trabalho

1. Atualizar DEV

Antes de começar qualquer desenvolvimento:

git checkout DEV
git pull origin DEV

2. Atualizar Branch Pessoal

Exemplo:

git checkout branch-raquel
git merge DEV

Objetivo

Trazer todas as atualizações recentes da equipe para a branch pessoal.

3. Desenvolver Funcionalidade

Cada membro deve trabalhar principalmente nos módulos sob sua responsabilidade.

4. Adicionar Alterações

git add .

5. Criar Commit

git commit -m "feat: create report service"

6. Enviar Alterações

git push origin branch-raquel

7. Merge para DEV

Após testes e validações:

git checkout DEV
git merge branch-raquel

8. Ao final quando tudo estiver pronto, testado e estável:

Merge Final para Main

git checkout main
git merge DEV

Resultado fina:

DEV
↓
main

## Regras importantes

- Nunca desenvolver diretamente na main;
- Sempre atualizar a DEV antes de começar;
- Sempre atualizar a branch pessoal antes de desenvolver;
- Fazer commits pequenos e organizados;
- Evitar alterar arquivos de responsabilidade de outros membros sem alinhamento;
- Testar antes de realizar merge.