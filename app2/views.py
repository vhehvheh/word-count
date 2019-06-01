from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'app2/menu.html')

def result(request):
    text = request.GET.get('text')
    words = text.split(' ')
    count = {}
    pp = 'result'
    for i in words:
        if i in count:
             count[i] = count[i]+1
        else:
            count[i] = 1
    context = {'text':text, 'words':words, 'tt':pp, 'count':count.items()}
    return render(request,'app2/index.html', context )

def menu(request):
    text = "menu"
    context = {'text':text}
    return render(request, 'app2/index.html' )