# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("""<a href="about/">About</a>""")
    params = {'name': 'Bhavye', 'planet':'mars'}
    return render(request, 'index.html', params)


def about(request):
    # return HttpResponse("about")
    return render(request, "about.html")


def analyseText(request):
    textToAnalyse = request.POST.get("textToAnalyse","default")

    length = request.POST.get("length","off")
    capitaliseFirst = request.POST.get("capitaliseFirst","off")
    capitaliseFullText = request.POST.get("capitaliseFullText","off")
    removePunction = request.POST.get("removePunction","off")
    newLineRemove = request.POST.get("newLineRemove","off")
    extraSpaceRemove = request.POST.get("extraSpaceRemove","off")

    result = analysisOfText(textToAnalyse,length,capitaliseFirst,capitaliseFullText,removePunction,newLineRemove,extraSpaceRemove)

    params = {'text' : result[1], 'length':result[0]}
    # return HttpResponse("This is analyse text")
    return render(request, "analyseTexthtml.html", params)


def getContactInfo(request):
    name = request.POST.get("name", "default")
    email = request.POST.get("email", "default")
    params = {'name':name, 'email':email}
    return render(request, "showContactDetails.html",params)


def analysisOfText(text = "", length = "off", capitaliseFirst = "off", capitaliseFullText = "off", removePunction = "off", newLineRemove = "off",extraSpaceRemove="off"):
    result = []
    if (length=="on"):
        result.append(len(text))
    else:
        result.append("N.A.")
    if (capitaliseFirst=="on"):
        text = text.title()
    if (capitaliseFullText=="on"):
        text = text.upper()
    if (removePunction=="on"):
        punct = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        resultText = ""
        #Remove punction
        for i in text:
            if i not in punct:
                resultText+=i
        text = resultText
    if (newLineRemove=="on"):
        l = ""
        resultText = ""
        for i in text:
            if i=="\r" or i=="\n":
                resultText = resultText + " "
            else:
                resultText = resultText + i
        firstPtr = 0
        secondPtr = 1
        while (firstPtr<len(resultText)):
            if (resultText[firstPtr]==" " and resultText[secondPtr]==" "):
                firstPtr+=1
                secondPtr+=1
            else:
                l = l + resultText[firstPtr]
                firstPtr+=1
                secondPtr+=1
        text = l
    if (extraSpaceRemove=="on"):
        m = text[0]
        for i in range(1,len(text)):
            if (m[-1]==" " and text[i]==" "):
                continue
            else:
                m+=text[i]
        text = m
    result.append(text)
    return result