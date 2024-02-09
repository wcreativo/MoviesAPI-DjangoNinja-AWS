from typing import List, Optional

from ninja import Router

from .models import Movies
from .schemas import MovieIn, MovieOut, NotFoundSchema

router = Router()


@router.get("/movies", response=List[MovieOut])
def get_movies(request, title: Optional[str] = None):
    if title:
        return Movies.objects.filter(title__icontains=title)
    return Movies.objects.all()


@router.get("/movies/{movie_id}", response={200: MovieOut, 404: NotFoundSchema})
def get_movie_by_id(request, movie_id: int):
    movie = Movies.objects.filter(id=movie_id).first()
    if movie:
        return 200, movie
    return 404, {"message": "The movie was not found"}


@router.post("/movies", response={201: MovieIn})
def create_movie(request, movie: MovieIn):
    movie = Movies.objects.create(**movie.dict())
    return movie


@router.put("/movies/{movie_id}", response={200: MovieOut, 404: NotFoundSchema})
def update_movie(request, movie_id: int, data: MovieIn):
    movie = Movies.objects.filter(id=movie_id).first()
    if movie:
        for attribute, value in data.dict().items():
            setattr(movie, attribute, value)
        movie.save()
        return 200, movie
    return 404, {"message": "Movie not found"}


@router.delete("/movies/{movie_id}", response={200: None, 404: NotFoundSchema})
def delete_movie(request, movie_id: int):
    movie = Movies.objects.filter(id=movie_id).first()
    if movie:
        movie.delete()
        return 200
    return 404, {"message": "Movie not found"}
