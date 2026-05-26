# Fluxo do Usuário — Sistema EcoLar

## 1. Inicialização do Sistema

Ao executar o arquivo `main.py`, o sistema inicia e exibe o menu principal.

```plaintext
Sistema EcoLar iniciado.
```

---

# 2. Menu Principal

O usuário visualiza as seguintes opções:

```plaintext
1 - Login
2 - Cadastrar usuário
0 - Sair
```

---

# 3. Cadastro de Usuário

Ao selecionar:

```plaintext
2 - Cadastrar usuário
```

o sistema solicita:

* nome;
* e-mail;
* data de nascimento;
* perfil energético.

---

# 4. Escolha do Perfil Energético

O sistema exibe os perfis disponíveis:

```plaintext
001 - Baixo
002 - Médio
003 - Alto
004 - Muito Alto
```

O usuário escolhe o perfil mais próximo da realidade da residência.

---

# 5. Validação do Cadastro

O sistema valida:

* nome vazio;
* formato do e-mail;
* data inválida;
* perfil inexistente;
* e-mail duplicado.

Caso exista erro:

* o sistema exibe mensagem;
* o cadastro é interrompido.

Caso válido:

* o usuário é salvo no sistema.

---

# 6. Cadastro Inicial de Aparelhos

Após o cadastro do usuário, o sistema pergunta:

```plaintext
Deseja cadastrar aparelhos agora? (S/N)
```

---

## Caso o usuário escolha "S"

O sistema exibe a lista de aparelhos disponíveis.

Exemplo:

```plaintext
001 - Geladeira 1 Porta
002 - Micro-ondas
003 - Liquidificador
...
```

O usuário informa:

* ID do aparelho;
* tempo médio diário de uso;
* quantidade de dias de uso no mês.

O sistema:

* valida os dados;
* salva o aparelho vinculado ao usuário;
* permite cadastrar múltiplos aparelhos.

---

## Caso o usuário escolha "N"

O sistema retorna ao menu principal.

---

# 7. Login

Ao selecionar:

```plaintext
1 - Login
```

o sistema solicita:

* e-mail do usuário.

O sistema:

* valida o formato;
* procura o usuário;
* inicia a sessão.

---

# 8. Menu do Usuário

Após login, o sistema exibe:

```plaintext
1 - Meu Perfil
2 - Meus aparelhos
3 - Atualizar cadastro
4 - Consumo energético
5 - Relatórios
6 - Recomendações
7 - Simular Economia
8 - Excluir Conta
0 - Logout
```

---

# 9. Meu Perfil

Exibe:

* ID;
* nome;
* e-mail;
* data de nascimento;
* perfil energético.

---

# 10. Meus Aparelhos

Exibe:

* aparelhos cadastrados;
* tempo diário de uso;
* quantidade de dias mensais.

---

# 11. Atualizar Cadastro

Permite:

* atualizar nome;
* atualizar e-mail;
* atualizar perfil energético;
* adicionar aparelhos;
* atualizar uso de aparelhos;
* remover aparelhos.

---

# 12. Consumo Energético

O sistema calcula:

* consumo mensal em kWh;
* custo estimado da energia.

---

# 13. Relatórios

O sistema gera:

* relatório de consumo;
* consumo individual por aparelho;
* consumo total estimado.

---

# 14. Recomendações

O sistema exibe dicas de economia energética personalizadas com base nos aparelhos cadastrados.

Exemplos:

* reduzir tempo de banho;
* evitar standby;
* desligar aparelhos da tomada.

---

# 15. Simulação de Economia

O sistema calcula:

* redução de consumo;
* novo custo estimado;
* economia mensal;
* economia anual.

As simulações utilizam:

* 10%;
* 20%;
* 30% de redução.

---

# 16. Exclusão de Conta

O usuário pode:

* remover a conta;
* remover os vínculos com aparelhos;
* apagar os dados do sistema.

---

# 17. Logout

Ao selecionar:

```plaintext
0 - Logout
```

o sistema encerra a sessão e retorna ao menu principal.

---

# 18. Encerramento do Sistema

Ao selecionar:

```plaintext
0 - Sair
```

o sistema finaliza a execução.
