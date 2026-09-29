from fastapi import FastAPI

app = FastAPI(title="Books API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books")
def list_books():
    # TODO: Retorne os livros do catálogo.
    return []


# TODO: Defina um modelo Pydantic para os dados de um livro.
# TODO: Implemente POST /books e GET /books/{book_id}.
# TODO: Implemente PUT /books/{book_id} e DELETE /books/{book_id}.
