from workflow_graph import WorkflowGraph
from random import uniform, randint

class HistoricoWorkflowGenerator:

    def __init__(self, data_submissao):
        self.workflow_graph = WorkflowGraph()
        self.actual_vertice = self.workflow_graph.estado_inicial
        initial_situacao = {
            "Estado": self.workflow_graph.vertices[self.actual_vertice],
            "DataInicio": data_submissao
        }
        self.actual_situacao = initial_situacao
        self.hw = [initial_situacao]

    def generate(self):
        while not self.actual_vertice or self.actual_vertice not in ('f', 'c', 'ra'):
            self.navigate()
            if self.actual_vertice != 'f':
                self.hw[-1]['FinalizadaPor'] = self.generate_random_user()
                situacao = self.create_situacao()
                self.actual_situacao = situacao
                self.hw.append(situacao)
        return self.hw

    def navigate(self):
        next_possibilities = self.workflow_graph.edges[self.actual_vertice]
        rand = uniform(0.0, 1.0)
        i = 0
        sum = next_possibilities[0][1]
        while rand > sum:
            i += 1
            sum += next_possibilities[i][1]
        self.actual_vertice = next_possibilities[i][0]

    def create_situacao(self):
        estado = self.workflow_graph.vertices[self.actual_vertice]

        data_inicio = self.generate_random_data_submissao()
        return {
            "Estado": estado,
            "DataInicio": data_inicio
        }

    def generate_random_user(self):
        user = 'usuário.'
        for i in range(3):
            user += chr(randint(97, 97 + 25))
        return user

    def generate_random_data_submissao(self):
        return self.actual_situacao["DataInicio"]
