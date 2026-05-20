# README - SISTEMA SIMPLIFICADO DE CONSUMO DE ENERGIA

## O QUE FOI CRIADO:

### Services (Calculos)
- `consumption_service.py` - Calcula consumo em kWh
- `energy_classification_service.py` - Classifica consumo (BAIXO, MEDIO, ALTO)
- `simulation_service.py` - Simula economia se reduzir

### Controller (Exibicao)
- `energy_simple_controller.py` - 4 funcoes para exibir

### Exemplo
- `exemplo_simples_energia.py` - Execute para ver funcionando

---

## COMO USA:

### Executar exemplo:
```bash
python3 exemplo_simples_energia.py
```

### Rodar no menu:
```python
from controllers.energy_simple_controller import mostrar_consumo_simples

usuario = {"id": "001", "name": "Expedito"}
mostrar_consumo_simples(usuario)
```

---

## COMANDOS USADOS:

| Comando | O que faz |
|---------|-----------|
| `if` | Verifica condicao |
| `elif` | Outra condicao |
| `else` | Caso contrario |
| `*` | Multiplica |
| `/` | Divide |
| `%` | Porcentagem |
| `for` | Repetir |
| `print()` | Exibir |

---

## ARQUIVOS E FUNCOES:

### consumption_service.py

**calcular_consumo_kwh(potencia, minutos_dia, dias_mes)**
- Calcula consumo de 1 aparelho
- Formula: (W / 1000) * (min / 60) * dias

**calcular_consumo_usuario(id_usuario)**
- Calcula total de todos os aparelhos
- Usa FOR para somar cada um

**calcular_custo(consumo_kwh)**
- Converte kWh em reais
- Formula: kWh * 0.95

---

### energy_classification_service.py

**classificar_consumo(id_usuario)**
- Classifica em 5 niveis:
  - MUITO BAIXO: <= 50 kWh
  - BAIXO: <= 100 kWh
  - MEDIO: <= 150 kWh
  - ALTO: <= 250 kWh
  - MUITO ALTO: > 250 kWh

**comparar_com_media(id_usuario)**
- Compara com 150 kWh (media nacional)
- Retorna: ACIMA, IGUAL ou ABAIXO

**classificar_por_faixa(id_usuario)**
- Classifica em 5 FAIXAS com intervalos

---

### simulation_service.py

**simular_economia(id_usuario, percentual_reducao)**
- Simula economia com % reduzido
- Ex: 30% = reduzir 30% do consumo
- Mostra economia mensal e anual

**simular_multiplas_reducoes(id_usuario)**
- Simula 3 opcoes: 10%, 20%, 30%
- Mostra todas as 3 opcoes

---

### energy_simple_controller.py

**mostrar_consumo_simples(usuario)**
- Exibe: Consumo total + Custo

**mostrar_classificacao(usuario)**
- Exibe: Consumo + Classificacao + Media nacional + Faixa

**mostrar_economia_simples(usuario)**
- Exibe: Economia com 30% de reducao

**mostrar_opcoes_economia(usuario)**
- Exibe: 3 opcoes (10%, 20%, 30%)

---

## EXEMPLO RAPIDO:

```python
# Importa funcao
from services.consumption_service import calcular_consumo_kwh

# Calcula 90W x 1440 min x 30 dias
consumo = calcular_consumo_kwh(90, 1440, 30)

# Exibe resultado
print(f"Consumo: {consumo} kWh")  # 64.8 kWh
```

---

## CALCULOS:

### Consumo de 1 aparelho:
```
kilowatts = potencia / 1000
horas = minutos / 60
horas_total = horas * dias
consumo = kilowatts * horas_total
```

### Reducao com %:
```
economia_kwh = consumo * percentual / 100
novo_consumo = consumo - economia_kwh
```

### Economia em dinheiro:
```
custo_atual = consumo * 0.95
custo_novo = novo_consumo * 0.95
economia = custo_atual - custo_novo
```

---

## FAIXAS DE CLASSIFICACAO:

| Faixa | Consumo | Classificacao |
|-------|---------|---------------|
| 1 | 0-30 kWh | Minimo |
| 2 | 30-60 kWh | Baixo |
| 3 | 60-100 kWh | Medio |
| 4 | 100-150 kWh | Alto |
| 5 | 150+ kWh | Muito Alto |

---

## TESTE TODOS:

Usuario 001:
- 129 kWh/mes = R$ 122.55
- Classificacao: MEDIO
- Status: ABAIXO da media
- Economia 30%: R$ 441.24/ano

---

## SO USA:

✓ if/elif/else
✓ Multiplicacao (*)
✓ Divisao (/)
✓ Porcentagem (%)
✓ For
✓ Print
✓ Dicionarios
✓ Listas

---

## PRONTO PARA:

✓ Adicionar ao menu
✓ Integrar com database
✓ Usar em relatorios
✓ Aproveitar para aprender

---

TUDO SIMPLIFICADO AO MAXIMO!
