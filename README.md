# Target Sistemas - Desafio Estágio

### 1: `` fibonacci.py `` 
 O programa define duas funções: **fibonacci_sequence(n)** que gera a sequência de Fibonacci até o número n, e **check_number_in_fibonacci(n)** que verifica se o número n está na sequência. No final, é possivel alterar o valor da variável numero para o número que deseja verificar:

```
resultado = check_number_in_fibonacci(numero)
print(resultado)
```

### 2: `` Letter.py ``
Neste programa, a função count_letter_a(string) transforma a string para minúsculas usando lower(), conta as ocorrências da letra 'a' e retorna uma mensagem indicando o resultado. A entrada da string é feita diretamente via input():

```
resultado = count_letter_a(input_string)
print(resultado)
```

### 3: ``Soma.py``
#### Valores iniciais:

``INDICE = 12``

``SOMA = 0``

``K = 1``

.

``Loop enquanto K < INDICE:``

``Na primeira iteração: K = 1 + 1 = 2, SOMA = 0 + 2 = 2``

``Na segunda iteração: K = 2 + 1 = 3, SOMA = 2 + 3 = 5``

``Na terceira iteração: K = 3 + 1 = 4, SOMA = 5 + 4 = 9``

``Na quarta iteração: K = 4 + 1 = 5, SOMA = 9 + 5 = 14``

``Na quinta iteração: K = 5 + 1 = 6, SOMA = 14 + 6 = 20``

``Na sexta iteração: K = 6 + 1 = 7, SOMA = 20 + 7 = 27``

``Na sétima iteração: K = 7 + 1 = 8, SOMA = 27 + 8 = 35``

``Na oitava iteração: K = 8 + 1 = 9, SOMA = 35 + 9 = 44``

``Na nona iteração: K = 9 + 1 = 10, SOMA = 44 + 10 = 54``

``Na décima iteração: K = 10 + 1 = 11, SOMA = 54 + 11 = 65``

``Na décima primeira iteração: K = 11 + 1 = 12, SOMA = 65 + 12 = 77``

O loop para, pois K agora é igual a 12, e o critério do loop (K < 
INDICE) não é mais atendido.

Portanto, ao final do processamento, o valor da variável SOMA será 77.

### 4. Desafio de Logica:

#### a) 1, 3, 5, 7, ___
Lógica: Sequência de números ímpares consecutivos.
Próximo elemento: 9.
#### b) 2, 4, 8, 16, 32, 64, ____
Lógica: Cada número é o dobro do anterior (multiplicação por 2).
Próximo elemento: 128.
#### c) 0, 1, 4, 9, 16, 25, 36, ____
Lógica: Números são quadrados perfeitos (n^2), começando de 0².
Próximo elemento: 49 (7²).
#### d) 4, 16, 36, 64, ____
Lógica: Números são quadrados perfeitos pares (2², 4², 6², 8²...).
Próximo elemento: 100 (10²).
#### e) 1, 1, 2, 3, 5, 8, ____
Lógica: Sequência de Fibonacci (cada número é a soma dos dois anteriores).
Próximo elemento: 13 (5 + 8).
#### f) 2, 10, 12, 16, 17, 18, 19, ____
Lógica: A sequência é composta de números que contêm o dígito '1'.
Próximo elemento: 20

## 5. ``Lampadas.py``

- A função **ligar_interruptor()** simula ligar uma lâmpada e torná-la quente.
- A função **desligar_interruptor()** simula desligar uma lâmpada, mantendo-a no estado anterior.


Quando executado, o código mostra o estado das lâmpadas e qual interruptor controla cada uma, baseando-se no comportamento da lâmpada (acesa, quente ou fria).

### GitHub:
- [@mrnutcry](https://github.com/mrnutcry)
