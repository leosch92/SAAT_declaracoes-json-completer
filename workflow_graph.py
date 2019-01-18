class WorkflowGraph:

    def __init__(self):
        self.vertices = {
            'ni': 'Não iniciada',
            'v': 'Visualizada',
            'i': 'Iniciada',
            'ra': 'Recontratação automática',
            's': 'Submetida',
            'asac': 'Em análise SAC',
            'rpa': 'Em revisão pelo Agente',
            'apl': 'Em análise PL',
            'csac': 'Em consolidação SAC',
            'c': 'Concluída',
            'f': 'Fim'
        }

        self.edges = {
            'ni': [('v', 0.8), ('ra', 0.1), ('f', 0.1)],
            'v': [('i', 0.8), ('ra', 0.1), ('f', 0.1)],
            'i': [('s', 0.8), ('ra', 0.1), ('f', 0.1)],
            's': [('asac', 0.9), ('f', 0.1)],
            'asac': [('rpa', 0.2), ('apl', 0.7), ('f', 0.1)],
            'apl': [('csac', 0.9), ('f', 0.1)],
            'rpa': [('asac', 0.9), ('f', 0.1)],
            'csac': [('c', 0.9), ('f', 0.1)]
        }

        self.estados_finais = ['ra', 'c', 'f']
        self.estado_inicial = 'ni'

