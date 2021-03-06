from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
#from commonsense.queries import get_random_concepts
from csc.conceptnet4.models import Concept, Relation, RawAssertion
from django.contrib.auth.decorators import login_required
from trek.models import ClaimedLink, User, GameProfile
import random, os



def main(request):
    try:
        topUsers = GameProfile.objects.filter(points__gt=0).order_by('-points')[:5]
    except:
        topUsers = []
        
    print topUsers
    return render_to_response('main.html', {'topusers': topUsers}, context_instance=RequestContext(request))

@login_required
def new_game(request):
    profile = request.user.profile
    
    relations =  get_all_relations('en')
    concept1, concept2 = get_random_concepts('en')
    #concept1, concept2 = get_random_from_file()
    return render_to_response('ui.html', {'concept1': concept1, 'concept2': concept2, 'relationsList': relations, 'profile': profile}, context_instance=RequestContext(request))


@login_required
def update_points(request, p):
    if request.method == 'POST':
        try:    
            p = int(p)
            print p
            print "Updating profile"
            profile = request.user.profile
            profile.points += p
            profile.save()
        except:
            return Http404()

        return HttpResponse()
    else:
        raise Http404()


def profile(request, username):
    try:
        user = User.objects.get(username=username)
        profile = user.profile
        claimedLinks = ClaimedLink.objects.filter(userid=user.id)
    except ClaimedLink.DoesNotExist:
        claimedLinks = []
    except:
        raise Http404()

    print "claimed", claimedLinks
    return render_to_response('profile.html', {'claimed': claimedLinks, 'user': user}, context_instance=RequestContext(request))


@login_required
def claim_link(request):
    if request.method == 'GET':
        try:
            print "Getting claimed link request"
            c1 = request.GET.get('c1')
            c2 = request.GET.get('c2')
            rel = request.GET.get('relation')


            claimed = ClaimedLink.objects.get(concept1=c1, concept2=c2, relation=rel)
            
        except ClaimedLink.DoesNotExist:
            print "claimed link does not exit"
            claimed = None            
        except:
            print "wuh oh"
            return Http404()

        print "made it this far"
        
        if not(claimed):
            claimed = ClaimedLink(concept1=c1, concept2=c2, relation=rel, userid=request.user, used=1)
            claimed.save()
            return HttpResponse()
        else:
            return HttpResponse("Already Claimed")

@login_required
def link_is_claimed(request):
    if request.method == 'GET':
        try:
            print "Searching for link"
            c1 = request.GET.get('c1')
            c2 = request.GET.get('c2')
            rel = request.GET.get('relation')
            use = bool(request.GET.get('use'))

            claimed = ClaimedLink.objects.get(concept1=c1, concept2=c2, relation=rel)

            if use:
                claimed.used += 1
                claimed.save()
                user = claimed.userid
                profile = user.profile
                profile.points += 1
                profile.save()

            return HttpResponse(claimed.userid)
        except:
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


random_concepts =open(os.path.join(settings.MEDIA_ROOT, 'random_concepts.txt'), 'rb').readlines()

def get_random_from_file(num=2):

    concepts = set([])

    while len(concepts) < num:
        concepts.add(random.choice(random_concepts).strip())
        
    print concepts
    return list(concepts)
    
