# a) Quantos posts estão registados
def quantosPost(redeSocial):
    return len(redeSocial)

# b) Lista de posts de um determinado autor
def postsAutor(redeSocial, autor):
    posts_do_autor = [post for post in redeSocial if post["autor"] == autor]
    return posts_do_autor

# c) Lista de autores de posts ordenada alfabeticamente
def autores(redeSocial): 
    lista= []
    for post in redeSocial:
        if "autor" in post:
            lista.append(post["autor"])
    lista.sort()
    return  lista

# d) Acrescentar novo post
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    id = f"p{len(redeSocial)+1}"
    post = {"id" : id, "conteudo" : conteudo, "autor" : autor, 'dataCriacao': dataCriacao, 'comentarios': comentarios}
    redeSocial.append(post)
    return redeSocial

# e) Remover um post consuante o ID
def remPost(redeSocial, id):
    return [post for post in redeSocial if post["id"] != id]

# f) Distribuição de posts por autor
def postsPorAutor(redeSocial):
    dist = {}
    for post in redeSocial:
        autor = post.get("autor")
        if autor in dist:
            dist[autor] = dist[autor] + 1
        else:
            dist[autor] = 1
    return dist

# g) Lista de posts comentados por um autor
def comentadoPor(redeSocial, autor):
    posts_comentados = []
    for post in redeSocial:
        if "comentarios" in post:
            for comentario in post["comentarios"]:
                if comentario.get("autor") == autor:
                   posts_comentados.append(post)
    return posts_comentados