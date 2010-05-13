from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
#from commonsense.queries import get_random_concepts
from csc.conceptnet4.models import Concept, Relation, RawAssertion
from django.contrib.auth.decorators import login_required
from django.db.models import F
import random





@login_required
def new_game(request):
    print "Getting concepts"

    profile = request.user.profile
    
    relations =  get_all_relations('en')
    concept1, concept2 = get_random_concepts('en')
    return render_to_response('ui.html', {'concept1': concept1, 'concept2': concept2, 'relationsList': relations, 'profile': profile}, context_instance=RequestContext(request))


@login_required
def update_points(request):
    if request.method == 'POST':
        try: 
            p = request.POST.get("points")
            print "Updating profile"
            profile = request.user.profile
            profile.points = F('points') + p
            profile.save()
        except:
            return Http404()

        return HttpResponse()
    else:
        raise Http404()

    
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
    return relations
   #return get_relations_from_CN() #Gets the relations from the DB...warning, not at all are usable

 
def get_relations_from_CN():
    return [r.text for r in Relation.objects.all()]
#print get_random_concepts('en')
#print get_all_relations('en')


random_cs = ["panda", "pony", "coffee", "notebook", "computer", "pen", "clown", "giraffe", "elephant"]






relations = [["IsA", ["is a", "What kind of thing is it?", 5]],
             ["CapableOf", ["capable of", "What can it do?", 8]],
             ["CreatedBy", ["created by", "How do you bring it into existence?", 25]],
             ["HasA", ["has", "What does it possess?", 16]],
             ["AtLocation", ["is located", "Where would you find it?", 6]],
             ["LocatedNear" , ["is located near", "What is it typically near?", 30]],
             ["MadeOf", ["made of", "What is it made of?", 4]],
             ["PartOf", ["part of", "What is it a part of?", 21]],
             ["ObstructedBy" , ["prevented by", "What would prevent it from happening?", 23]],
             ["UsedFor", ["used for", "What do you use it for?", 7]],
             ["HasSubevent", ["is accomplished by", "What do you do to accomplish it?", 19]],
             ["HasFirstSubevent", ["is first accomplished by", "What do you do first to accomplish it?", 1]],
             ["HasLastSubevent", ["is last accomplished by", "What do you do last to accomplish it?", 2]],
             ["HasPrerequisite", ["is done by first", "What do you need to do first?", 3]],
             ["MotivatedByGoal", ["is motivated by", "Why would you do it?", 9]],
             ["Causes", ["causes", "What does it make happen?", 18]],
             ["Desires", ["wants", "What does it want?", 10]],
             ["CausesDesire", ["makes you want", "What does it make you want to do?", 17]],
             ["HasProperty", ["has the property of", "What properties does it have?", 20]],
             ["ReceivesAction", ["receives the action", "What can you do to it?", 22]],
             ["DefinedAs", ["defined as", "How do you define it?", 13]],
             ["SymbolOf", ["a symbol of", "What does it represent?", 15]],
             ["ConceptuallyRelatedTo", ["is conceptually related to", "What is related to it in an unknown way?", 12]]]



