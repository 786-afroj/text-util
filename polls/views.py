import math
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    
           return render(request,'index.html')
           
           #return HttpResponse("home")

def analyze(request):
           #get the text
           djtext=request.GET.get('text','default')

           #check checkbox values
           removepunc=request.GET.get('removepunc','off')
           fullcaps=request.GET.get('fullcaps','off')
           newlineremover=request.GET.get('newlineremover','off')
           extraspaceremover=request.GET.get('extraspaceremover','off')
           charcouter=request.GET.get('charcouter','off')
           wordcount=request.GET.get('wordcount','off')
           #check which checkbox is on
           if removepunc == "on":
                      #print(removepunc)
                      #print(djtext)
                      #analyze=djtext
                      punctuations='''!;()-[]{}:'"\,<>.?@#$%^&*_~'''
                      analyzed=""
                      for char in djtext:
                                 if char not in punctuations:
                                            
                                            analyzed=analyzed+char
                                 
                      params={'purpose':'Removed punctuations','analyzed_text':analyzed}
                      #Analyze the text
                      return render(request,'analyze.html',params)
           elif(fullcaps=="on"):
                      analyzed=""
                      for char in djtext:
                                 analyzed=analyzed+char.upper()
                      params={'purpose':'Change to upper case','analyzed_text':analyzed}
                      #Analyze the text
                      return render(request,'analyze.html',params)
           elif(newlineremover=="on"):
                      analyzed=""
                      for char in djtext:
                                 if char !="\n":
                                            analyzed=analyzed+char
                      params={'purpose':'Remove NewLines','analyzed_text':analyzed}
                      #Analyze the text
                      return render(request,'analyze.html',params)
           elif(newlineremover=="on" and fullcaps=="on" and removepunc == "on"):
                      punctuations='''!;()-[]{}:'"\,<>.?@#$%^&*_~'''
                      analyzed=""
                      for char in djtext:
                                 if char not in punctuations:
                                            if char =="\n":
                                                       analyzed=analyzed+char.upper()
                      params={'purpose':'Remove NewLines,fullcaps and Removed punctuations','analyzed_text':analyzed}
                      #Analyze the text
                      return render(request,'analyze.html',params)
           elif(extraspaceremover=="on"):
                      analyzed=""
                      for index,char in enumerate(djtext):
                                 if not(djtext[index] == " " and djtext[index+1] =="  "):
                                            analyzed=analyzed+char
                      params={'purpose':'extra space remove','analyzed_text':analyzed}
                      #Analyze the text
                      return render(request,'analyze.html',params)
           elif(charcouter=='on'):
                      analyzed=0
                      for s in djtext:
                                 analyzed+=1
                      params={'purpose':'count character','analyzed_text':analyzed,}
                      return render(request,'analyze.html',params)
           elif(wordcount=='on'):
                      analyzed=0
                      c=0
                      flag=True
                      for s in djtext:
                                 if flag==False and djtext[analyzed]==' ':
                                            c+=1
                                 if djtext[analyzed]==' ':
                                            flag=True
                                 else:
                                            flag=False
                                 analyzed+=1
                      params={'purpose':'count word','analyzed_text':c+1}
                      return render(request,'analyze.html',params)

           else:
                      return HttpResponse("Error")
  
"""def capfirst(request):
           return HttpResponse("capfirst")
def newlineremove(request):
           return HttpResponse("newline remove first")

def spaceremove(request):
           return HttpResponse("space remove <a href='capitalizefirst'>back</a>")
def charcount(request):
           return HttpResponse("charcount")"""
