from sqlalchemy import Table, String, Integer, Date, REAL, Column, MetaData

metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("original_title", String),
    Column("overview", String),
    Column("release_date", Date),
    Column("vote_average", REAL),
    Column("poster_path", String)
)
