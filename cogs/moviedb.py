import pprint
import requests


search_query = 'endgame'
api_key = 'api_key'
api_base_url = "https://api.themoviedb.org/3"
endpoint_path = f"/search/movie"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}&page=1&include_adult=true"


r= requests.get(endpoint)
data = r.json()
results = data['results']
results1 = results[0]
for result in results1:
    _description= result['overview']
   


    print(_description)
    
