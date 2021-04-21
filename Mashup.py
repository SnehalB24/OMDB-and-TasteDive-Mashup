import requests
import json
def get_movies_from_tastedive(string):
    baseurl = "https://tastedive.com/api/similar"
    para_dic = {'q':string, 'type':'movies', 'limit':5}
    tastedive_resp = requests.get(baseurl, params = para_dic)
    testdive_data = tastedive_resp.json()
    return testdive_data
result=get_movies_from_tastedive("Black Panther")

def extract_movie_titles(result):
    lst=[]
    for i in result['Similar']['Results']:
        movie_title=i['Name']
        lst.append(movie_title)
    return(lst)
#movie_result = extract_movie_titles(result)
def get_related_titles(movie_lst):
    lst2=[]
    for p in movie_lst:
        related_movie = get_movies_from_tastedive(p)
        related_data = extract_movie_titles(related_movie)
        for x in related_data:
            if x not in lst2:
                lst2.append(x)
         
    return lst2
movie_lst = ["Black Panther", "Captain Marvel"]
print(get_related_titles(movie_lst))
 
def get_movie_data(string):
    baseurl2 = "http://www.omdbapi.com/"
    param_dictionary2 = {'t':string, 'r':'json'}
    tastedive_resp2 = requests.get(baseurl2, params = param_dictionary2)
    print(tastedive_resp2.url)
    testdive_data2 = tastedive_resp2.json()
    return testdive_data2

result2=get_movie_data("Deadpool 2")

def get_movie_rating(result2):
    for w in result2['Ratings']:
        if w['Source']=='Rotten Tomatoes':
            f=w['Value']
            q=f.split('%')
            return int(q[0])
    return 0
print(get_movie_rating(result2))  

def get_sorted_recommendations(movie_title_list):
    movie_rating_dict = {}
    for title in get_related_titles(movie_title_list):
        rating = get_movie_rating(get_movie_data(title))
        movie_rating_dict[title] = rating
    sorted_list = sorted(movie_rating_dict, key = lambda title : (movie_rating_dict[title], title), reverse = True)
    return sorted_list


    
