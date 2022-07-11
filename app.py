import requests
from flask import Flask, render_template
app = Flask(__name__)


def get_total_pages():
    url = "https://reqres.in/api/users"
    response = requests.get(url)
    total_pages = response.json()["total_pages"]
    return total_pages


def get_user_list(page):
    url = "https://reqres.in/api/users?page=" + str(page)
    response = requests.get(url)
    data = response.json()["data"]
    return data


@app.route('/')
def home():
    total_pages = get_total_pages()
    users = []
    for page in range(1, total_pages + 1):
        data = get_user_list(page)
        for user in data:
            users.append(user)
    return render_template('home.html', title='User List',
                           users=users)


if __name__ == "__main__":
    app.run()