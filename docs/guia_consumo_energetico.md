# Guia de Consumo Energético — EcoLar

## Sobre o EcoLar

O EcoLar é um sistema acadêmico desenvolvido em Python com o objetivo de auxiliar usuários no monitoramento do consumo energético residencial.

O sistema permite:

* cadastrar usuários;
* registrar aparelhos elétricos;
* calcular consumo energético;
* estimar custos mensais;
* simular economia de energia;
* exibir recomendações de uso consciente.

---

# O que é consumo energético?

O consumo energético representa a quantidade de energia elétrica utilizada pelos aparelhos ao longo do tempo.

A unidade utilizada pelo sistema é:

```plaintext id="5jlwmu"
kWh (quilowatt-hora)
```

Essa unidade é utilizada pelas concessionárias de energia para calcular o valor da conta de luz.

---

# Como o EcoLar calcula o consumo?

O sistema realiza o cálculo utilizando:

* potência do aparelho (Watts);
* tempo médio diário de uso;
* quantidade de dias de uso no mês.

## Fórmula utilizada

```plaintext id="1jlwmg"
Consumo (kWh) =
(potência × horas de uso × dias de uso) / 1000
```

---

# Exemplo Prático

## Televisão LED

* Potência: 90W
* Uso diário: 5 horas
* Uso mensal: 30 dias

Cálculo:

```plaintext id="4jlwmd"
(90 × 5 × 30) / 1000 = 13,5 kWh
```

---

# Estimativa de custo mensal

O EcoLar também realiza uma estimativa simples do custo energético mensal.

O sistema utiliza uma tarifa média configurada internamente para calcular o valor aproximado da conta de energia.

## Fórmula utilizada

```plaintext id="mjlwmu"
Custo = consumo × tarifa energética
```

---

# Classificação Energética

O sistema classifica o consumo do usuário em faixas energéticas.

As classificações representam níveis de eficiência e consumo residencial.

## Faixas Utilizadas

| Classificação | Consumo          |
| ------------- | ---------------- |
| A+            | Muito eficiente  |
| A             | Baixo consumo    |
| B             | Consumo moderado |
| C             | Consumo elevado  |
| D             | Alto consumo     |
| E             | Consumo crítico  |

---

# Simulação de Economia

O EcoLar permite realizar simulações simples de economia energética.

O sistema calcula:

* novo consumo estimado;
* novo custo mensal;
* economia mensal;
* economia anual.

As simulações atuais trabalham com:

* redução de 10%;
* redução de 20%;
* redução de 30%.

---

# Recomendações de Economia

O sistema possui uma base de dicas de economia cadastradas para diferentes aparelhos elétricos.

Exemplos:

* reduzir tempo de banho;
* desligar aparelhos da tomada;
* evitar uso desnecessário;
* utilizar modos econômicos;
* aproveitar iluminação natural.

---

# Principais Aparelhos Monitorados

O sistema possui aparelhos previamente cadastrados, incluindo:

* geladeira;
* micro-ondas;
* televisão;
* ventilador;
* ar-condicionado;
* computador;
* notebook;
* máquina de lavar;
* chuveiro elétrico;
* iluminação LED.

---

# Objetivo Educacional do Projeto

O EcoLar foi desenvolvido com foco em:

* conscientização energética;
* sustentabilidade;
* educação tecnológica;
* aplicação prática de programação;
* manipulação de dados;
* arquitetura de software.

O projeto integra conceitos de:

* Python;
* persistência TXT;
* estruturas de dados;
* tratamento de exceções;
* modularização;
* desenvolvimento colaborativo.

---

# Limitações do MVP

A versão atual do EcoLar representa um MVP (Minimum Viable Product).

Algumas funcionalidades planejadas para versões futuras incluem:

* interface gráfica;
* gráficos de consumo;
* histórico comparativo;
* gamificação avançada;
* metas de economia;
* integração com APIs externas.

---

# Conclusão

O EcoLar demonstra como conceitos de programação podem ser aplicados na construção de soluções voltadas à sustentabilidade e conscientização energética.

Mesmo em formato terminal, o sistema já permite:

* monitoramento energético básico;
* cálculos reais de consumo;
* simulações simples;
* apoio à tomada de decisão do usuário.
