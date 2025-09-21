"Case Simulação da chegada de um caminhão a uma doca"
import simpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"Objetivo: calcular o tempo médio de espera para descarregamento de caminhões em uma doca."

resultados = []

#-----CONSTRUÇÃO DA ENTIDADE: OBJETO EM MOVIMENTAÇÃO NO SISTEMA 
def caminhao(env, nome, doca):
    """
    Representa um caminhão (entidade) que chega à doca, espera e descarrega.
    """
    
    # evento
    tempo_chegada = env.now
    print(f'{nome}, chegou na doca em: {tempo_chegada:.2f}')

    # pedido do uso do recurso: aguarda a liberação do recurso.
    with doca.request() as recurso:
        yield recurso

        # evento espera + acesso ao consumo recurso
        tempo_espera = env.now - tempo_chegada
        print(f'{nome}, começou a descarregar em: {env.now:.2f} - tempo de espera: {tempo_espera}')

        tempo_descarregamento = np.random.exponential(5)

        # evento tempo de serviço
        yield env.timeout(tempo_descarregamento)

        # saída: libera o recurso automaticamente
        tempo_saida = env.now
        print(f'{nome}, terminou em: {tempo_saida:.2f}.')

        # armazenamento dos resultados

        resultados.append(

            {
                'caminhao': nome,
                'chegada': tempo_chegada,
                'espera': tempo_espera,
                'servico': tempo_descarregamento,
                'saida': tempo_saida

            }

        )

#-----GERACAO DO EVENTO: CHEGADA DE CAMINHÕES

def gerar_caminhao(env, doca):
     
    """
    Processo que gera caminhões chegando ao sistema em intervalos aleatórios.
    """

    # quantidade inicial
    i=0

    while True:
        yield env.timeout(np.random.exponential(scale=10.0))
        i+=1
        # instancia de um novo caminhao no evento de chegada
        env.process(caminhao(env=env, nome=f'caminhao {i}', doca=doca))

#-----CONSTRUÇÃO DO AMBIENTE

env = simpy.Environment()
doca = simpy.Resource(env, capacity=2)

# instancia da geracao de entidade no ambiente
env.process(gerar_caminhao(env, doca))

# execução do ambiente
env.run(until=720)


# tabela de resultados
tbl_resultado_simulacao = pd.DataFrame(resultados)

# estatisticas
print('-----ESTATÍSTICAS DO AMBIENTE')
tbl_resultado_simulacao['hora_chegada'] = (tbl_resultado_simulacao['chegada']//60).astype(int)
tempo_medio_espera = tbl_resultado_simulacao['espera'].mean()

print(f"Tempo médio de espera: {tempo_medio_espera:.2f} unidades de tempo")
print("Tempo médio de serviço:", tbl_resultado_simulacao['servico'].mean())
print("Tempo médio no sistema:", (tbl_resultado_simulacao['saida'] - tbl_resultado_simulacao['chegada']).mean())

resumo = (
    tbl_resultado_simulacao.groupby('hora_chegada')
    .agg(
        media_espera=('espera', 'mean'),
        media_servico=('servico', 'mean'),
        qtd_caminhoes=('caminhao', 'count')
    )
    .reset_index()
)
print(resumo)

plt.figure()
plt.plot(resumo['hora_chegada'], resumo['media_espera'], label='Tempo médio de espera')
plt.plot(resumo['hora_chegada'], resumo['media_servico'], label='Tempo médio de serviço')
plt.plot(resumo['hora_chegada'], resumo['qtd_caminhoes'], label='Qtd caminhões')
#plt.annotate('Fila crítica', xy=(4,24), xytext=(5,25),
#            arrowprops=dict(facecolor='red', shrink=0.05))
plt.legend()
plt.xlabel('Hora da chegada')
plt.show()

plt.plot(tbl_resultado_simulacao['caminhao'], tbl_resultado_simulacao['espera'], marker='o')
plt.title('Tempo de espera por caminhão')
plt.xlabel('Caminhão')
plt.ylabel('Tempo de espera')
plt.xticks(rotation=90)
plt.show()

