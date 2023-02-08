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
# # 1
def check(movie):
    print(movie["imdb"] > 5.5)
check(movies[7])
# 2
# def sublist(movie):
#     print([x for x in movie if check(x)])
# sublist(movies)
# 3
# def category(cat, movie):
#     print([x for x in movie if x["category"] == cat])
# category("Romance", movies)
# 4
# def avgscore(movie):
#     c = 0
#     t = 0
#     for i in movie:
#         c += 1
#         t += i["imdb"]
#     print(t / c)
# avgscore(movies)
# # 5
# def avgscorecat(cat, movie):
#     new = [x for x in movie if x["category"] == cat]
#     c = 0
#     t = 0
#     for i in new:
#         c += 1
#         t += i["imdb"]
#     print(t / c)
# avgscorecat("Romance", movies)