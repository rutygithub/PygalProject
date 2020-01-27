import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)
# store the response into a dict
response_dict = r.json()
print(response_dict.keys())
print('total repo', response_dict['total_count'])

repo_dicts = response_dict['items']
print('the items number is ', len(repo_dicts))

first_repo = repo_dicts[0]
print("the first repo's lenth is " + str(len(first_repo)))
for key in first_repo.keys():
    print(key)
