from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


class Member:
    def __init__(self, member_id, name, add_date, picture_path):
        self.member_id = member_id
        self.name = name
        self.add_date = add_date
        self.picture_path = picture_path


member_list = [
    Member(0, 'Taro', '2021/07/28', 'img/taro.jpg'),
    Member(1, 'Jiro', '2021/07/28', 'img/jiro.jpg'),
    Member(0, 'Hanako', '2021/07/28', 'img/hanako.jpg'),
    Member(0, 'Yoshiko', '2021/07/28', 'img/yoshiko.jpg'),
]


def members(request):
    return render(request, 'members.html', context={
        'members': member_list
    })