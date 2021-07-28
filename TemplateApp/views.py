from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


# メンバーインスタンス
class Member:
    def __init__(self, member_id, name, add_date, picture_path):
        self.member_id = member_id
        self.name = name
        self.add_date = add_date
        self.picture_path = picture_path


# 手持ちの情報でメンバーインスタンスを作成しリストにしている
member_list = [
    Member(0, 'Taro', '2021/07/28', 'img/taro.jpg'),
    Member(1, 'Jiro', '2021/07/28', 'img/jiro.jpg'),
    Member(2, 'Hanako', '2021/07/28', 'img/hanako.jpg'),
    Member(3, 'Yoshiko', '2021/07/28', 'img/yoshiko.jpg'),
]


def members(request):
    return render(request, 'members.html', context={
        'members': member_list
    })


def member_detail(request, id):
    return render(request, 'member.html', context={
        'member': member_list[id]
    })
# member_listのid番目の情報を取得してmember.htmlに渡している。
# あくまで、リストとidの順番が同じの前提だよね
