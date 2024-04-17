import os
import shutil

# Diretório onde está o dataset
dataset_dir = r"C:\Projetos\Faculdade\7-Periodo\Redes-Neurais\Pneumonia\data\chest_xray\val"

# Função para separar os arquivos em subpastas


def separar_arquivos_por_tipo(diretorio_origem, diretorio_destino_bacteriana, diretorio_destino_viral):
    # Percorre os diretórios NORMAL e PNEUMONIA dentro do diretório de origem
    for pasta_classe in ['NORMAL', 'PNEUMONIA']:
        # Percorre os arquivos dentro do diretório da classe
        for arquivo in os.listdir(os.path.join(diretorio_origem, pasta_classe)):
            # Verifica se o arquivo contém "bacteria" no nome
            if "bacteria" in arquivo:
                # Copia o arquivo para o diretório destino da pneumonia bacteriana
                shutil.copy2(os.path.join(diretorio_origem, pasta_classe, arquivo),
                             os.path.join(diretorio_destino_bacteriana, pasta_classe, arquivo))
            # Verifica se o arquivo contém "virus" no nome
            elif "virus" in arquivo:
                # Copia o arquivo para o diretório destino da pneumonia viral
                shutil.copy2(os.path.join(diretorio_origem, pasta_classe, arquivo),
                             os.path.join(diretorio_destino_viral, pasta_classe, arquivo))


# Diretórios de destino para as imagens
diretorio_destino_bacteriana = r"C:\Projetos\Faculdade\7-Periodo\Redes-Neurais\Pneumonia\data\chest_xray_separado\BACTERIANA"
diretorio_destino_viral = r"C:\Projetos\Faculdade\7-Periodo\Redes-Neurais\Pneumonia\data\chest_xray_separado\VIRAL"

# Cria as pastas de destino se elas não existirem
os.makedirs(os.path.join(diretorio_destino_bacteriana, 'NORMAL'), exist_ok=True)
os.makedirs(os.path.join(diretorio_destino_bacteriana,
            'PNEUMONIA'), exist_ok=True)
os.makedirs(os.path.join(diretorio_destino_viral, 'NORMAL'), exist_ok=True)
os.makedirs(os.path.join(diretorio_destino_viral, 'PNEUMONIA'), exist_ok=True)

# Chama a função para separar os arquivos
separar_arquivos_por_tipo(
    dataset_dir, diretorio_destino_bacteriana, diretorio_destino_viral)
