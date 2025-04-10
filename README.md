# 🐋 Viagem ao Fundo do Mar

Um sistema de navegação para submarinos não tripulados em exploração científica da Fossa das Marianas.

## 🌊 Sobre o Projeto

Este projeto simula a movimentação de submarinos autônomos enviados por uma equipe de cientistas para explorar a Fossa das Marianas, o ponto mais profundo dos oceanos.

A movimentação do submarino é controlada por comandos simples enviados em sequência. O sistema interpreta esses comandos e retorna a posição final e a direção do submarino.

## 📍 Caso de Uso

### Cenário

A equipe científica está explorando a **Fossa das Marianas**, que atinge até **11.034 metros de profundidade** no oceano Pacífico. Para isso, são utilizados submarinos não tripulados que navegam em um ambiente 3D, com coordenadas nos eixos **X, Y e Z**.

A posição do submarino é representada como:

# 🐋 Viagem ao Fundo do Mar

Um sistema de navegação para submarinos não tripulados em exploração científica da Fossa das Marianas.

## 🌊 Sobre o Projeto

Este projeto simula a movimentação de submarinos autônomos enviados por uma equipe de cientistas para explorar a Fossa das Marianas, o ponto mais profundo dos oceanos.

A movimentação do submarino é controlada por comandos simples enviados em sequência. O sistema interpreta esses comandos e retorna a posição final e a direção do submarino.

## 📍 Caso de Uso

### Cenário

A equipe científica está explorando a **Fossa das Marianas**, que atinge até **11.034 metros de profundidade** no oceano Pacífico. Para isso, são utilizados submarinos não tripulados que navegam em um ambiente 3D, com coordenadas nos eixos **X, Y e Z**.

A posição do submarino é representada como:

Sendo:
- `X`: posição horizontal (Leste-Oeste)
- `Y`: posição vertical (Norte-Sul)
- `Z`: profundidade (0 na superfície, valores negativos em profundidade)
- `DIREÇÃO`: orientação atual do submarino (NORTE, SUL, LESTE, OESTE)



A posição inicial do submarino é sempre:
(0, 0, 0, NORTE)
## ✅ Exemplo de Entrada e Saída

### Exemplo 1:
**Entrada:**  
LMRDDMMUU


**Saída esperada:**  
-1 2 0 NORTE



### Exemplo 2:
**Entrada:**  
RMMLMMMDDLL



**Saída esperada:**  
2 3 -2 SUL


