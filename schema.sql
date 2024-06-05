CREATE TABLE IF NOT EXISTS movie (
    movie_id SERIAL,
    title VARCHAR(255) NOT NULL,
    director TEXT NOT NULL,
    PRIMARY KEY (movie_id)
);