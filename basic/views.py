import faker
from django.shortcuts import render

from basic.models import UserEntry


def make_entries(request):
    value = int(request.GET.get('value', 0))
    popup = False

    if value > 0:
        faker_object = faker.Faker()
        for _ in range(value):
            user_entry = UserEntry(name=faker_object.name(), address=faker_object.address(), email="new@gmail.com")
            user_entry.save()
        popup = True

    count = UserEntry.objects.count()
    return render(request, 'index.html', {"count": count, "popup": popup})
