from django.shortcuts import render

# Define a list of dictionaries, each representing a book with its information
dic = [
    {
        "title": "Ногоон нүдэн лам",
        "author": "Merriam-Webster",
    },
    {
        "title": "Оройгүй сүм",
        "author": "Merriam-Webster",
    }
]


def index(request):
    return render(request, 'index.html', {"dic": dic})
