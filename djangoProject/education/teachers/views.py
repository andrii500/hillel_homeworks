from django.http import HttpResponse
from .models import Teachers
from faker import Faker

faker = Faker()


def get_teachers(request):
    teachers = Teachers.objects.create(first_name=faker.first_name(), last_name=faker.last_name(),
                                       subject=faker.random_element(elements=('math', 'physics', 'history', 'literature')))
    teachers_list = Teachers.objects.all()
    output = ''.join([f"<p>{t.first_name} {t.last_name}, {t.subject}</p>" for t in teachers_list])
    return HttpResponse(f"{output}")
