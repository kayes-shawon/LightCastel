from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.forms.models import model_to_dict


# Create your views here.
def index_view(request):
    main_sliders =  MainSlider.objects.all()
    services_sliders = ServicesSlider.objects.all()
    case_studies_sliders = CaseStudiesSlider.objects.all()
    initiatives_sliders = InitiativeSlider.objects.all()
    clients_sliders = ClientsSlider.objects.all()
    words_of_encouragement_sliders = WordsOfEncouragementSlider.objects.all()

    services_slider_group = []
    for i in range(0, len(services_sliders), 3):
        if (len(services_sliders) - i) >= 3:
            tuple = (services_sliders[i], services_sliders[i+1], services_sliders[i+2])
        elif (len(services_sliders) - i) == 2:
            tuple = (services_sliders[i], services_sliders[i + 1])
        if (len(services_sliders) - i) == 1:
            tuple = (services_sliders[i])

        services_slider_group.append(tuple)


    case_studies_slider_group = []
    for i in range(0, len(case_studies_sliders), 3):
        if (len(case_studies_sliders) -i) >= 3:
            tuple = (case_studies_sliders[i], case_studies_sliders[i+1], case_studies_sliders[i+2])
        elif (len(case_studies_sliders) -i) == 2:
            tuple = (case_studies_sliders[i], case_studies_sliders[i + 1], case_studies_sliders[i + 2])
        else :
            tuple = (case_studies_sliders[i])
        case_studies_slider_group.append(tuple)

    initiatives_slider_group = []
    for i in range(0, len(initiatives_sliders), 3):
        if (len(initiatives_sliders) - i) >= 3:
            tuple = (initiatives_sliders[i],initiatives_sliders[i+1], initiatives_sliders[i+2],)
        elif (len(initiatives_sliders) - i) == 2:
            tuple = (initiatives_sliders[i], initiatives_sliders[i+1])
        else:
            tuple = (initiatives_sliders[i])
        initiatives_slider_group.append(tuple)


    clients_slider_group = []
    for i in range(0, len(clients_sliders), 4):
        if (len(clients_sliders) - i) >= 4:
            tuple = (clients_sliders[i], clients_sliders[i+1], clients_sliders[i+2], clients_sliders[i+3])
        elif (len(clients_sliders) - i) == 3:
            tuple = (clients_sliders[i], clients_sliders[i+1], clients_sliders[i+2])
        elif (len(clients_sliders) - i) == 2:
            tuple = (clients_sliders[i], clients_sliders[i+1])
        else:
            tuple = (clients_sliders[i])
        clients_slider_group.append(tuple)

    return render(request=request, template_name="landingsite/home.html",
                  context={
                      'main_sliders': main_sliders,
                      'services_sliders': services_slider_group,
                      'case_studies_sliders': case_studies_slider_group,
                      'initiatives_sliders': initiatives_slider_group,
                      'clients_sliders': clients_slider_group,
                      'words_of_encouragement_sliders': words_of_encouragement_sliders,
                  })



def about_view(request):
    management_people = ManagementPeople.objects.all()
    advisors = Advisor.objects.all()
    patrons = Patron.objects.all()

    return render(request=request, template_name='landingsite/about.html',
                  context={
                      'management_people': management_people,
                      'advisors' : advisors,
                      'patrons': patrons,
                  })




def media_view(request):
    op_eds = OP_ED.objects.all()
    magazines = Magazine.objects.all()
    interviews = Interview.objects.all()

    op_eds_slider_count = range(1, (len(op_eds) % 6) + 1)

    return render(request=request, template_name='landingsite/media.html',
                  context={
                      'op_eds': op_eds,
                      'op_eds_slider_index' : op_eds_slider_count,
                      'magazines' : magazines,
                      'interviews': interviews,
                  })



def case_studies_view(request):
    case_studies = CaseStudiesSlider.objects.all()
    expanded_card = case_studies[len(case_studies)-1]
    print("calling default")

    return render(request=request, template_name='landingsite/case_studies.html',
                  context={
                      'case_studies': case_studies,
                      'expanded_card': expanded_card
                  }
                  )



def case_studies_expanded_view(request, id):
    case_studies = CaseStudiesSlider.objects.all()
    expanded_card = CaseStudiesSlider.objects.get(id=id)
    print(expanded_card)

    return render(request=request, template_name='landingsite/case_studies.html',
                  context={
                      'case_studies': case_studies,
                      'expanded_card': expanded_card
                  }
                  )



def case_studies_details_json(request, id):
    case_studies = CaseStudiesSlider.objects.all()
    expanded_card = CaseStudiesSlider.objects.get(id=id)
    dict = {
        'title': expanded_card.title,
        'content': expanded_card.content,
        'image': expanded_card.image.url,
        'body': expanded_card.body,
        'blog_body': expanded_card.blog_body,
        'publish_date': expanded_card.publish_date,
        'tag': expanded_card.tag,
        'cover_image': expanded_card.cover_image.url,

    }

    return JsonResponse(dict)
    # return render(request=request, template_name='landingsite/case_studies.html',
    #               context={
    #                   'case_studies': case_studies,
    #                   'expanded_card': expanded_card
    #               }
    #               )



def subscribe_newsletter(request):
    email = request.POST.get('email')
    email_db = NewsletterSubscriber(email=email)
    email_db.save()
    return JsonResponse({'message': 'subscribed successfully'})



def request_callback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
            subject,
            message,
            email,
            ['info@lightcastlebd.com'],
            fail_silently=False,
        )
        return JsonResponse({'message': 'operation successful'})

