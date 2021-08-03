from django.http import HttpResponse

from faker import Faker

from .models import Teachers

faker = Faker()


def get_teachers(request):
    args = request.GET
    dict_param = {}
    for key, value in args.items():
        dict_param[key] = value
    if dict_param:
        teachers_list = Teachers.objects.filter(**dict_param)
        output = ''.join([f"<p>{t.id}, {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")
    else:
        teachers_list = Teachers.objects.all()
        output = ''.join([f"<p>{t.id}, {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")
