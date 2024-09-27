import yaml
import pandas as pd

def prepare_data(yaml_file, output_csv):
    with open(yaml_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    # Extrair exemplos e intenções
    intents = []
    texts = []

    for intent_data in data['nlu']:
        intent_name = intent_data['intent']
        # Extrair as frases de exemplo
        examples = intent_data['examples'].strip().split('\n')

        # Verificar se está tentando acessar corretamente
        for example in examples:
            example = example.strip().replace('-', '').strip()  # Limpar o formato
            if example:  
                texts.append(example)
                intents.append(intent_name)

    # Criar um DataFrame com os dados
    df = pd.DataFrame({
        'Texto': texts,
        'Intencao': intents
    })

    # Salvar o DataFrame em CSV
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print("CSV criado com sucesso!")

prepare_data('dados.yaml', 'dados_intencoes.csv')
