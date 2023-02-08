# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def IMDB_more_than_5_5(movie):
    if(movie["imdb"] > 5.5):
        return True
    return False
def list_IMDB_more_than_5_5(movies):
    l = []
    for i in movies:
        if(i["imdb"] > 5.5):
            l.append(i["name"])
    return l

def movies_category(movies, category):
    l = []
    for i in movies:
        if(category == i["category"]):
            l.append(i["name"])
    return l
  
def Average_imdb(movies):
    l = []
    for i in movies:
        l.append(i["imdb"])
    return sum(l)/len(l)

def average_imdb_category(movies, category):
    l = []
    for i in movies:
        if(category == i["category"]):
            l.append(i["imdb"])
    return sum(l)/len(l)
# print(IMDB_more_than_5_5(movies[7]))
# result: False
# print(list_IMDB_more_than_5_5(movies))
# result: ['Usual Suspects', 'Hitman', 'Dark Knight', 'The Help', 'The Choice', 'Colonia', 'Love', 'Joking muck', 'What is the name', 'Detective', 'We Two']  
# print(movies_category(movies, "Romance"))
# result: ['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two']
# print(Average_imdb(movies))
# result: 6.486666666666667
# print(average_imdb_category(movies, "Thriller"))
# result: 5.6