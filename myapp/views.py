from django.shortcuts import render, HttpResponse

# 하나하나의 글을 딕셔너리에 담고, 리스트로 묶자
topics = [
{'id':1, 'name':'Lebron James', 'body':'Lebron James is ...'},
{'id':2, 'name':'Russel Westbrook', 'body':'Russel Westbrook is ...'},
{'id':3, 'name':'Malik Monk', 'body':'Malik Monk is ...'}
]

def HTMLTemplate(articleTag):
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}/">{topic["name"]}</a></li>'

    return f'''
    <html>
    <body>
        <h1><a = href = "/">느바stats</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''


def index(request): # 파라미터의 인자로, 요청과 관련된 정보가 들어오도록 약속되어 있는 객체를 전달해 줌
    article = '''
    <h2> Welcome </h2>
    Hello, Basketball Fan!
    '''

    global topics
    return HttpResponse(HTMLTemplate(article))


def create(request):
    article = '''
    <form action="/create/">
        <p><input type = "text" name = "name" placeholder="name"></p>
        <p><textarea name = "body" placeholder="describtion"></textarea></p>
        <p><input type="submit"></p>
    </form>
    '''
    return HttpResponse(HTMLTemplate(article))


def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if str(topic['id']) == id:
            article = f'<h2>{topic["name"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))