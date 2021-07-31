from django.http import HttpResponse

from faker import Faker

from .models import Student

faker = Faker()


def index(request):
    return HttpResponse("""<p>Path: /generate-student/</p>
                           <p>Path: /generate-students/?count=value</p>
                           <p>Path: /teachers/</p>
                           <p>Path: /teachers/?first_name=value&last_name=value&age=value</p>
                           <p>Path: /group/</p>""")


def get_generate_student(request):
    student = Student.objects.create(first_name=faker.first_name(),
                                     last_name=faker.last_name(),
                                     age=faker.random_int(18, 100))
    return HttpResponse(f"{student.id}, "
                        f"{student.first_name}, "
                        f"{student.last_name}, "
                        f"{student.age}")


def get_generate_students(request):
    count = request.GET.get("count", "1")
    if count.isdigit():
        if 0 < int(count) <= 100:
            output = ''
            for i in range(int(count)):
                student = Student.objects.create(first_name=faker.first_name(),
                                                 last_name=faker.last_name(),
                                                 age=faker.random_int(18, 100))
                output += f"<p>{student.id}, {student.first_name}, {student.last_name}, {student.age}</p>"
            return HttpResponse(output)
        else:
            return HttpResponse("Count must be greater than 0, less or equal  than 100")
    else:
        return HttpResponse("Count must be integer and not negative")
