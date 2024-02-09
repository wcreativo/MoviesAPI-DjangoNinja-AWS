from ninja import Schema


class MovieOut(Schema):
    id: int
    title: str
    duration: int


class MovieIn(Schema):
    title: str
    duration: int


class NotFoundSchema(Schema):
    message: str
