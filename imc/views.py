from django.shortcuts import render , redirect
from django.http import HttpResponse
from imc.forms import PersonForm
from imc.models import Person
from django.db.models import F, ExpressionWrapper , DecimalField
import math
from math import pow



# creation d'une fonction calculImc
# def showAPerson(request):
#         persons = Person.objects.filter(user)
#         return persons




# def register(request):
#         #appeler la fonction showPerson ici 
#         persons= showAPerson(request)
#         #enregister les valeur du formalaire dans la base de donnée 
#         if request.method == 'POST':
#             personForm = PersonForm(request.POST).save()

#             # envoyer les valeur de showPerson a la page resultat.html
#             print(persons)
#             var = list(persons)[2]
#             return render(request, 'resultat.html',{'var':var})
#         else :
#                 personForm = PersonForm()
       
#                 return render(request, 'home.html', {'personForm': personForm})

def home(request):
        return render(request, 'home.html')
        
        
        
def lesPersonn(request):
        return Person.objects.all()

def register(request):
        #appeler la fonction lesPersonn ici 
        persons= lesPersonn(request)
        #enregister les valeur du formalaire dans la base de donnée 
        if request.method == 'POST':
            personForm = PersonForm(request.POST).save()
 
            # mettre person dans une liste et dans prendre le dernier element de la liste  
            dernierePerson = list(persons)[-1]
            taillee = int(dernierePerson.taille)
            poidss = int(dernierePerson.poids)
            IMC=dernierePerson.poids/pow(dernierePerson.taille,2) 
            # envoyer les valeur du dernier element de la liste  a la page resultat.html
            return render(request, 'resultat.html',{'dernierePerson':dernierePerson , 'imc':round(IMC,2)})
        else :
                personForm = PersonForm()
                return render(request, 'home.html', {'personForm': personForm})


# def showPersonn(request):
#         val1=int(request.POST["user"])
#         val2=int(request.POST["num"]) 
#         pers = Person.objects.get(user = val1, num = val2)
#         return render (request, 'reShowPerson.html', {'maPerson':pers})


#pers = Person.objects.get(user = User, nom = Nom)
#pers.taille = 
#pers.poids = 
                  

        
def showPerson(request):
        try:
            if request.method =="POST":
                    if len(request.POST) > 0:
                        User= request.POST.get('user')
                        Nom = request.POST.get('nom')
                        pers = Person.objects.get(user = User, nom = Nom)
                        #Recuperation du poids et taille pour faire le calcul
                        IMC=pers.poids/pow(pers.taille,2) 
                        return render(request, 'reShowPerson.html', {'personne':pers,'imc':round(IMC,2)})
                    else:
                            message = "echoue"
                            return render(request, 'showPerson.html', {'message':message})
                        


        except:
            print("bad tuto")
        return render (request, 'showPerson.html')

       
def toutPerson(request):
        lesPerson= lesPersonn(request)
        return render(request, 'toutPerson.html', {'lesPersons':lesPerson})
