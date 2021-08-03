from django.http import HttpResponse

from faker import Faker

from .models import Group

faker = Faker()


def get_group(request):
    group_list = Group.objects.all()
    output = ''.join(
        [f"<p>{t.title}, {t.num_of_students}</p>" for t in group_list]
    )
    return HttpResponse(f"{output}")
