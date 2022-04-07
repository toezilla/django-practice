from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextId=4
# 하나하나의 글을 딕셔너리에 담고, 리스트로 묶자
topics = [
{'id':1, 'name':'Lebron James', 'body':'Lebron James is ...'},
{'id':2, 'name':'Russel Westbrook', 'body':'Russel Westbrook is ...'},
{'id':3, 'name':'Malik Monk', 'body':'Malik Monk is ...'}
]

def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action = "/delete/" method = "post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value = "delete">
                </form>
            </li>
            <li><a href="/update/{id}">update</a></li>
        '''

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
            {contextUI}
        </ul>
    </body>
    </html>
    '''


def index(request): # 파라미터의 인자로, 요청과 관련된 정보가 들어오도록 약속되어 있는 객체를 전달해 줌
    article = '''
    <h2> Welcome </h2>
    Hello, Basketball Fan!
    '''

    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
        <form action="/create/" method = "POST">
            <p><input type = "text" name = "name" placeholder="name"></p>
            <p><textarea name = "body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        name = request.POST['name']
        body = request.POST['body']
        newTopic = {"id":nextId, "name":name, "body":body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)
        nextId+=1
        return redirect(url)

@csrf_exempt
def delete(request):
    global topics
    if request.method == "POST":
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')

@csrf_exempt
def update(request, id):
    global topics
    if request.method == "GET":
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "name":topic["name"],
                    "body":topic["body"]
                }
        article = f'''
            <form action="/update/{id}/" method = "POST">
                <p><input type = "text" name = "name" placeholder="name" value={selectedTopic["name"]}></p>
                <p><textarea name = "body" placeholder="body">{selectedTopic['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
            '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == "POST":
        name = request.POST['name']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['name'] = name
                topic['body'] = body
        return redirect(f'/read/{id}')

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if str(topic['id']) == id:
            article = f'<h2>{topic["name"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id)) ## 삭제를 위해
