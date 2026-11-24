# Guardiao - Missao Seguranca

Jogo educativo feito com Pygame. Esta versao pode ser executada no navegador usando Pygbag.

## Testar localmente

```powershell
python -m pip install -r requirements.txt
python -m pygbag .
```

Abra o endereco local exibido pelo Pygbag no navegador.

## Publicar no Render

O arquivo `render.yaml` configura a publicacao como um Static Site. Envie este projeto para um repositorio GitHub e, no Render, crie um Blueprint apontando para esse repositorio. O Render instala as dependencias, gera `build/web` com Pygbag e publica essa pasta.
