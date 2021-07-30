from django.http import HttpResponse
from .models import Group
from faker import Faker

faker = Faker()


def get_group(request):
    group = Group.objects.create(title=faker.random_element(elements=('first', 'second', 'third', 'forth')) + ' group',
                                 num_of_students=faker.random_int(10, 30))
    group_list = Group.objects.all()
    output = ''.join([f"<p>{t.title}, {t.num_of_students}</p>" for t in group_list])
    return HttpResponse(f"{output}")

