import requests

api_url = "https://randomuser.me/api/"

def get_random_user():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        user_info = data['results'][0]
        return {
            'name': f"{user_info['name']['first']} {user_info['name']['last']}",
            'email': user_info['email'],
            'username': user_info['login']['username'],
            'password': user_info['login']['password'],
            'country': user_info['location']['country']
        }
    else:
        raise ValueError("Failed to fetch data from the API")

usuario = get_random_user()

print("Nome:", usuario['name'])
print("Email:", usuario['email'])  
print("Username:", usuario['username'])
print("Password:", usuario['password'])
print("Country:", usuario['country'])
