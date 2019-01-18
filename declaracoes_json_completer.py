from historico_workflow_generator import HistoricoWorkflowGenerator
import json

class DeclaracoesJSONCompleter:

    def __init__(self, declaracoes_json_path):
        self.declaracoes_json_path = declaracoes_json_path

    def complete(self):
        declaracoes = self.parse_json()
        self.preenche_declaracoes_com_hws(declaracoes)
        self.build_json(declaracoes)

    def parse_json(self):
        with open(self.declaracoes_json_path) as json_file:
            declaracoes = json.load(json_file)
        json_file.close()
        return declaracoes

    def build_json(self, declaracoes):
        with open(self.declaracoes_json_path, 'w') as json_file:
            json.dump(declaracoes, json_file, ensure_ascii=False)

    def preenche_declaracoes_com_hws(self, declaracoes):
        for declaracao in declaracoes:
            data_submissao = declaracao['DataSubmissao']
            hw_gen = HistoricoWorkflowGenerator(data_submissao)
            historico_workflow = hw_gen.generate()
            self.append_hw_to_declaracao(declaracao, historico_workflow)

    def append_hw_to_declaracao(self, declaracao, hw):
        declaracao['HistoricoWorkflow'] = hw
