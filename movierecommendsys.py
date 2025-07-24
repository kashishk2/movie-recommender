# List of popular movies with short descriptions
movies = [
    ("3 Idiots", "engineering college friends fun struggle"),
    ("Dangal", "father daughters wrestling sports"),
    ("PK", "alien earth religion funny emotional"),
    ("Chak De India", "hockey coach women india sports"),
    ("Avengers: Endgame", "superheroes fight thanos save world"),
    ("Titanic", "romantic ship iceberg love"),
    ("Avatar", "alien world blue people fight for nature"),
    ("Fast & Furious", "cars action family street race"),
    ("Inception", "dreams inside dreams mission mind"),
    ("The Dark Knight", "batman joker gotham superhero")
]

def recommend(movie_name):
    # Find the movie the user entered
    for title, desc in movies:
        if movie_name.lower() == title.lower():
            selected_desc = desc
            break
    else:
        return ["Movie not found."]

    # Simple matching: count common words with other movies
    scores = []
    selected_words = set(selected_desc.split())
    for title, desc in movies:
        if title.lower() == movie_name.lower():
            continue
        words = set(desc.split())
        common = selected_words & words
        scores.append((title, len(common)))

    # Sort by most common words
    scores.sort(key=lambda x: x[1], reverse=True)

    # Return top 3 matches
    return [title for title, score in scores[:3]]

# UI
print("Welcome to Simple Movie Recommender")
print("Here are some movies you can choose from:\n")
for title, _ in movies:
    print("->", title)

user_movie = input("\nEnter movie name: ")
print("\nYou might also like:")

for rec in recommend(user_movie):
    print("->", rec)
