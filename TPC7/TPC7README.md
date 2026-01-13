# RESUMO DO TPC7
## Data: 28/10/2025
## Autor: Pedro Lousinha
## Resumo:
Este trabalho teve como objetivo criar um programa de gestão de uma rede social.

A rede social é representada por uma lista de dicionários (`redeSocial`).
Cada dicionário corresponde a um post e tem a seguinte estrutura:

```python
{
  "id": "p1",
  "conteudo": "Texto do post",
  "autor": "Nome do autor",
  "dataCriacao": "YYYY-MM-DD",
  "comentarios": [
    {
      "autor": "Nome",
      "texto": "Texto do comentário"
    }
  ]
}
```

- id: identificador único do post  
- conteudo: texto do post  
- autor: autor do post  
- dataCriacao: data de criação do post  
- comentarios: lista de comentários associados ao post  

## Funções

### quantosPost(redeSocial)
Devolve o número total de posts existentes.

### postsAutor(redeSocial, autor)
Devolve a lista de posts escritos por um determinado autor.

### autores(redeSocial)
Devolve uma lista com os autores dos posts, ordenada alfabeticamente.

### insPost(redeSocial, conteudo, autor, dataCriacao, comentarios)
Insere um novo post na rede social.

### remPost(redeSocial, id)
Remove um post da rede social com base no seu identificador.

### postsPorAutor(redeSocial)
Devolve um dicionário com o número de posts por autor.

### comentadoPor(redeSocial, autor)
Devolve a lista de posts que foram comentados por um determinado autor.
