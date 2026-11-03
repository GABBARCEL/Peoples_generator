from pathlib import Path
# Deixei isso aqui para virar "Público" no pacote todo, talvez não tenha sido a decisão mais inteligente, mas eu tentei :^/


outputPath = Path(__file__).resolve().parent.parent / "output" # Achei melhor deixar o escopo do output público

outputPath.mkdir(parents=True, exist_ok=True)