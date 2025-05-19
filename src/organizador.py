from pathlib import Path
import shutil
import random

# Caminhos das pastas (usando Path)
PASTA_ORIGEM = Path(__file__).parent.parent / 'archive'
PASTA_DESTINO = Path(__file__).parent.parent / 'data'
SUBPASTAS = ['treino', 'teste', 'validação']

# Proporções de divisão
PROP_TREINO = 0.7
PROP_TESTE = 0.15
PROP_VALIDACAO = 0.15

def criar_pastas_destino(classes):
    for subpasta in SUBPASTAS:
        for classe in classes:
            caminho = PASTA_DESTINO / subpasta / classe
            caminho.mkdir(parents=True, exist_ok=True)

def organizar_imagens():
    if not PASTA_ORIGEM.exists():
        raise FileNotFoundError(f"Pasta de origem não encontrada: {PASTA_ORIGEM}")

    classes = [d.name for d in PASTA_ORIGEM.iterdir() if d.is_dir()]
    criar_pastas_destino(classes)

    for classe in classes:
        caminho_classe = PASTA_ORIGEM / classe
        imagens = [f for f in caminho_classe.iterdir() if f.is_file()]
        random.shuffle(imagens)

        total = len(imagens)
        n_treino = int(total * PROP_TREINO)
        n_teste = int(total * PROP_TESTE)

        conjuntos = {
            'treino': imagens[:n_treino],
            'teste': imagens[n_treino:n_treino + n_teste],
            'validação': imagens[n_treino + n_teste:]
        }

        for subpasta, lista_imgs in conjuntos.items():
            for img in lista_imgs:
                destino = PASTA_DESTINO / subpasta / classe / img.name
                shutil.copy2(img, destino)

if __name__ == '__main__':
    organizar_imagens()