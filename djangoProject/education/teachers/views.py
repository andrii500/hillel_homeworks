from django.http import HttpResponse

from faker import Faker

from .models import Teachers

faker = Faker()


def get_teachers(request):
    first_name = request.GET.get("first_name", None)
    last_name = request.GET.get("last_name", None)
    age = request.GET.get("age", None)
    if first_name and last_name and age:
        teachers_list = Teachers.objects.filter(first_name=first_name, last_name=last_name, age=age)
        output = ''.join([f"<p>{t.id}, {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")
    elif first_name and last_name:
        teachers_list = Teachers.objects.filter(first_name=first_name, last_name=last_name)
        output = ''.join([f"<p>{t.id}, {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")
    elif first_name and age:
        teachers_list = Teachers.objects.filter(first_name=first_name, age=age)
        output = ''.join([f"<p>{t.id}, {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")
    elif last_name and age:
        teachers_list = Teachers.objects.filter(last_name=first_name, age=age)
        output = ''.join([f"<p>{t.id}, {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")
    elif first_name:
        teachers_list = Teachers.objects.filter(first_name=first_name)
        output = ''.join([f"<p>{t.id}, {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")
    elif last_name:
        teachers_list = Teachers.objects.filter(last_name=last_name)
        output = ''.join([f"<p>{t.id}, {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")
    elif age:
        teachers_list = Teachers.objects.filter(age=age)
        output = ''.join([f"<p>{t.id}, {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")
    else:
        teachers_list = Teachers.objects.all()
        output = ''.join([f"<p>{t.id}, {t.first_name} {t.last_name}, {t.age}, {t.subject}</p>" for t in teachers_list])
        return HttpResponse(f"{output}")
