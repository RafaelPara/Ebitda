import simpy
import random

class Fila:
    def __init__(self, env, num_caixas):
        self.env = env
        self.caixa = simpy.Resource(env, capacity=num_caixas)
        self.tempo_espera = 0

    def atendimento(self, cliente):
        yield self.env.timeout(random.uniform(1, 3))  # Tempo de atendimento entre 1 e 3 unidades

    def chegada_cliente(self, env):
        for i in range(5):  # Simula a chegada de 5 clientes
            cliente = self.atendimento(i)
            start_time = env.now  # Armazena o tempo de chegada do cliente
            with self.caixa.request() as req:
                yield req
                end_time = env.now  # Armazena o tempo de término do atendimento
                self.tempo_espera += end_time - start_time

def main():
    env = simpy.Environment()
    fila = Fila(env, num_caixas=2)
    env.process(fila.chegada_cliente(env))
    env.run()

    tempo_medio_espera = fila.tempo_espera / 5
    print(f"Tempo médio de espera: {tempo_medio_espera:.2f} unidades de tempo")

if __name__ == "__main__":
    main()