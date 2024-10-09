# Estado inicial das lâmpadas (todas desligadas e frias)
lampadas = {
    'lampada_A': {'estado': 'desligada', 'temperatura': 'fria'},
    'lampada_B': {'estado': 'desligada', 'temperatura': 'fria'},
    'lampada_C': {'estado': 'desligada', 'temperatura': 'fria'}
}

# Função para simular o efeito de ligar um interruptor
def ligar_interruptor(lampada):
    lampadas[lampada]['estado'] = 'ligada'
    lampadas[lampada]['temperatura'] = 'quente'

# Função para desligar uma lâmpada
def desligar_interruptor(lampada):
    lampadas[lampada]['estado'] = 'desligada'

# Simulando a estratégia descrita:
# 1. Ligue o interruptor A (lampada_A) por alguns minutos
ligar_interruptor('lampada_A')

# 2. Desligue o interruptor A e ligue o interruptor B (lampada_B)
desligar_interruptor('lampada_A')
ligar_interruptor('lampada_B')

# 3. Vá para a sala e verifique as lâmpadas
def verificar_lampadas():
    for lampada, info in lampadas.items():
        if info['estado'] == 'ligada':
            print(f"{lampada} está ligada e quente. Controlada pelo interruptor B.")
        elif info['temperatura'] == 'quente':
            print(f"{lampada} está desligada, mas quente. Controlada pelo interruptor A.")
        else:
            print(f"{lampada} está desligada e fria. Controlada pelo interruptor C.")

# Resultado da verificação
verificar_lampadas()
