DECLARACOES_JSON_PATH = 'declaracoes.json'
from declaracoes_json_completer import DeclaracoesJSONCompleter

def main():
    completer = DeclaracoesJSONCompleter(DECLARACOES_JSON_PATH)
    completer.complete()

if __name__ == "__main__":
    main()
