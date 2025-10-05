"Case de Simulção de operação de um armazém"
import salabim as sim
import numpy as np

"""
Pedidos que entram no sistema para picking realizado pelos operadores.

Entidades: pedidos.
Recurso: operadores de picking (capacidade fixa).
Processo: chegada dos pedidos, atendimento (tempo normal).
Objetivo: medir taxa de utilização dos operadores.

"""

#-----CONSTRUÇÃO DA ENTIDADE: OBJETO EM MOVIMENTAÇÃO NO SISTEMA

class Pedido(sim.Component):

    # processo: sequência de eventos
    def process(self):

        # evento: entrada do pedido
        entrada_pedido = env.now()
        print(f'{self.name()} entrou no sistema. Disponível para picking.')

        # solicitação de recurso
        yield self.request(operador)

        # evento: espera pelo início do processo
        espera = env.now() - entrada_pedido
        print(f'{self.name()} aguardou a liberação do operador por {espera:.2f}')
        
        # evento: tempo de picking
        yield self.hold(np.random.exponential(20)) # agendamento do evento

        # evento: liberação do operador
        yield self.release()

#-----GERAÇÃO DO EVENTO: ENTRADA DE PEDIDOS NO CD
class GeradorPedidos(sim.Component):
    
    # processo: sequência de eventos
    def process(self):
        i =0

        while True:

            # evento: tempo entre pedidos
            yield self.hold(np.random.exponential(2))

            i+=1
            # entidade: pedidos
            Pedido(name=f'Pedido {i}')

#-----CONSTRUÇÃO DO AMBIENTE
sim.yieldless(False)

# ambiente
env = sim.Environment()

# recurso
operador = sim.Resource(name='Operador', capacity=5)

# invovação do motor
GeradorPedidos()

# tempo limite
env.run(till=100)


# estatísticas
print('Tempo total simulado', env.now())
print(f"Tempo total de atraso da operação{operador.requesters().length_of_stay:.2f}")
print(f"Tamanho médio da fila de pedidos: {operador.requesters().length.mean():.2f}")
print(operador.print_statistics())