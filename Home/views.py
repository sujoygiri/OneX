from django.shortcuts import render
from django.http import HttpResponse
from .models import EncrypteMessage,DecrypteMessage
from django.contrib import messages
import requests
from html import unescape
from random import shuffle
# Create your views here.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def message_encription(message,shift_val):
    encrypt_message = ""
    for item in message:
        if item in letters:
            try:
                encrypt_message += letters[letters.index(item)+shift_val+1]
            except IndexError:
                encrypt_message += letters[(letters.index(item)+shift_val+1) - len(letters)]
    return encrypt_message
def message_decryption(message,shift_val):
    decrypt_message = ""
    for item in message:
        if item in letters:
            decrypt_message += letters[letters.index(item)-shift_val-1]
    return decrypt_message

def Home(request):
    return render(request, "Home/home.html")


def EncrypteDecrypte(request):
    return render(request, "Home/encoder_decoder.html")

def EncrypteMessage(request):
    if request.method == "POST":
        message = request.POST.get("encrypte_text")
        shift_val = request.POST.get("en_shift_value")
        encrypted_message = message_encription(message,int(shift_val))

        context = {'encrypted_message':encrypted_message,'en_shift_val':shift_val}
    return render(request,"Home/encoder_decoder.html",context=context)

def DecrypteMessage(request):
    if request.method == "POST":
        message = request.POST.get("decrypte_text")
        shift_val = request.POST.get("de_shift_value")
        decrypted_message = message_decryption(message,int(shift_val))
        context = {'decrypted_message':decrypted_message,'de_shift_val':shift_val}
    return render(request,"Home/encoder_decoder.html",context=context)

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def HigherLower(request):
    context = {"letter_list":letter_list}
    return render(request,"Home/higher_lower.html",context=context)
#Creating view for Quizler
params = {
    "amount":1,
    "type":"multiple"
}
def Quizler(request):
    response = requests.get("https://opentdb.com/api.php",params=params)
    question = response.json()['results'][0]['question']
    correct_answer = response.json()['results'][0]['correct_answer']
    incorrect_answers = response.json()['results'][0]['incorrect_answers']
    incorrect_answers.append(correct_answer)
    question_category = response.json()['results'][0]['category']
    question_difficulty = response.json()['results'][0]['difficulty']
    shuffle(incorrect_answers)
    context = {"question":unescape(question),"correct_answer":correct_answer,
                "incorrect_answer":unescape(incorrect_answers),"question_category":question_category,
                "question_difficulty":question_difficulty}
    return render(request,"Home/quizler.html",context=context)

def Converter(request):
    return render(request,"Home/converter.html")