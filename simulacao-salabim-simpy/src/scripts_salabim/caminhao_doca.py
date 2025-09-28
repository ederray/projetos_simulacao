"Case Simulação da chegada de um caminhão a uma doca"
import salabim as sim
import numpy as np

"Objetivo: calcular o tempo médio de espera para descarregamento de caminhões em uma doca."

#-----CONSTRUÇÃO DA ENTIDADE: OBJETO EM MOVIMENTAÇÃO NO SISTEMA
class Caminhao(sim.Component):

    def process(self):

        # evento: chegada
        tempo_chegada = env.now()
        print(f'{self.name()} chegou na doca em {tempo_chegada:.2f}')

        # recurso: doca
        yield self.request(doca)

        # evento: espera liberação do recurso
        espera = env.now() - tempo_chegada
        print(f'{self.name()} aguardou a liberação da doca por: {espera:.2f}')

        # evento: descarregamento
        yield self.hold(np.random.exponential(10))

        # evento: saída do recurso
        yield self.release()


#-----GERACAO DO EVENTO: CHEGADA DE CAMINHÕES
class GeradorCaminhao(sim.Component):
    def process(self):
        i=0

        while True:

            # evento: tempo entre chegada
            yield self.hold(np.random.exponential(20))
            i+=1
            Caminhao(name=f'Caminhao {i}')



#-----CONSTRUÇÃO DO AMBIENTE

sim.yieldless(False)

# ambiente
env = sim.Environment()

# monitor
monitor = sim.Monitor('Tempo do Ciclo')

# recurso
doca = sim.Resource(name='Doca', capacity=1)

# construção da fila
fila = sim.Queue('Fila de Caminhões')

# construção de entidade
GeradorCaminhao()
env.run(till=720)


# estatísticas inclusas no recurso
print("Tempo total simulado:", env.now())
print("pct média de tempo de Ocupação da doca:", doca.occupancy.mean())
print("Tamanho médio da fila em espera pela doca:", doca.requesters().length.mean())
print("Tempo médio em espera pela doca:", doca.requesters().length_of_stay.mean())
print("Comprimento médio da fila:", fila.length.mean())
print(doca.print_statistics())
