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
#1)Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def is_high(movie):
    return movie["imdb"] > 5.5
print(is_high(movies[-3]) , '\n')

#2)Write a function that returns a sublist of movies with an IMDB score above 5.5.
def is_highmoves(movie):
    return [movie for movie in movies if movie["imdb"]> 5.5]
print(is_highmoves(movies), '\n')

#3)Write a function that takes a category name and returns just those movies under that category
def cat(cate):
    dog = []
    for i in movies:
        if i['category']==cate:
            dog.append(i['name'])
    return dog
print(cat('Thriller') , '\n')


#4)Write a function that takes a list of movies and computes the average IMDB score.
def ave(movies):
    sum =0
    for movie in movies:
        sum+=movie['imdb']
    return sum / len(movies)
print(ave(movies), '\n')


#5)Write a function that takes a category and computes the average IMDB score.
def catave(catt):
    sum =0
    imdb_ave = []
    for movie in movies:
        if movie['category'] == catt:
            imdb_ave.append(movie['name'])
            sum += movie['imdb']
    return sum / len(imdb_ave)
print (catave('Comedy'), '\n')

