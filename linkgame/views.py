from django.http import HttpResponse
from django.shortcuts import render_to_response
#from commonsense.queries import get_random_concepts
from csc.conceptnet4.models import Concept, Relation, RawAssertion
import random



def new_game(request):
    print "Getting concepts"

    relations =  get_all_relations('en')
    concept1, concept2 = get_random_concepts('en')
    return render_to_response('ui.html', {'concept1': concept1, 'concept2': concept2, 'relationsList': relations})

#concepts = get_random_concepts(language, 10)
def get_random_concepts(lang):

    concept1 = random.choice(random_cs)
    while True:
        concept2 = random.choice(random_cs)
        if concept1 != concept2:
            break
    return (concept1, concept2)
    
    #return get_random_from_CN(lang) #Uncomment to get random concepts from ConceptNet
    
#copied from commonsense.queries
def get_random_from_CN(lang, num=2):
   # concepts = Concept.objects.filter(language=lang).filter(words = 1).order_by('?')
   assertions = RawAssertion.objects.filter(score__gt=2, language=lang).select_related('surface1').order_by('?')

   concepts = set([])
   i = 0
   while len(concepts) < num:
       concepts.add(assertions[i].surface1.text)
       i += 1

   return list(concepts)
   #got_concepts = set(a.surface1.text for a in assertions[:num*2])
  # return got_concepts
#    return concepts[:num]

    #
    #concepts = Concept.objects.get(id=random.randrange(0,num_concepts))
   # return concepts
    #return list(concepts)[:num]
  #  got_concepts = set(a.surface1.text for a in assertions[:num*2])
   # return list(got_concepts)[:num]



#Try to cache?
#Hard code? Don't we always want these to be in teh same order? Or we could just alphebetize?
def get_all_relations(lang):
    return [r.name for r in Relation.objects.all()]

#print get_random_concepts('en')
#print get_all_relations('en')


random_cs = ["panda", "pony", "coffee", "notebook", "computer", "pen", "clown", "giraffe", "elephant"]



