import datetime
import hashlib

import pytest
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import authenticate
from django.test import Client

from firstapp.admin import EmailReply
from firstapp.forms import RegistrationForm, ChangePasswordForm
from firstapp.models import *


@pytest.fixture(scope="function")
def data_sourse(db):
    c = Client()
    c.post('/registration/', {'username': 'def', 'password': 'def', 'password_repeat': 'def', 'mail': 'def@gmail.com'})
    type = Type.objects.create(name="Активный отдых")
    country = Country.objects.create(name="Франция")
    owner = Owner.objects.create(name="БелТур")
    tour = Tour.objects.create(title="Чехия всегда", country=country, type=type, owner=owner,
                               image="media/7e79b151a97cc442418bac02086d8499.jpg")
    TourInstance.objects.create(id="123e4567-e89b-12d3-a456-426655440000", tour=tour,
                                date_of_departure=datetime.date.today(),
                                date_of_arrival=datetime.date.today(),
                                number_of_seats=60, cost=175)


def test_save(db, data_sourse):
    type = Type.objects.get(name="Активный отдых")
    country = Country.objects.get(name="Франция")
    owner = Owner.objects.get(name="БелТур")
    tour = Tour.objects.get(title="Чехия всегда")
    profile = Profile.objects.get(user__username="def")
    assert type.name == "Активный отдых"
    assert type.__str__() == "Активный отдых"
    assert country.__str__() == "Франция"
    assert owner.__str__() == "БелТур"
    assert tour.__str__() == "Чехия всегда"
    assert profile.__str__() == "def"


def test_save_user(db, data_sourse):
    user = authenticate(username="def", password="def")
    assert user.email == "def@gmail.com"


# Admin

def test_save_feedback(db, data_sourse):
    feedback = Feedback.objects.create(email_reply_date=datetime.datetime.now(), email_reply_text="sdf",
                                       email_reply_capt="sdfs")
    feedback.email_reply_adress.add(Profile.objects.get(user__username="def"))
    my_model_admin = EmailReply(model=Feedback, admin_site=AdminSite())
    my_model_admin.save_model(obj=feedback, request=None, form=None, change=None)


# class TestForm(TestCase):


@pytest.mark.parametrize("mail,username,password,password_repeat,error",
                         [('def@gmail.com', 'def', 'def', 'def', "Данная почта уже сужествует"),
                          ('Nonedefault@gmail.com', 'def', 'def', 'def', "Данное имя уже сужествует"),
                          ('Nonedefault@gmail.com', 'Nonedefault', 'Nonedefault', 'def', "Пароли не совпадают"), ])
def test_registration(db, data_sourse, mail, username, password, password_repeat, error):
    form_data = {'mail': mail, 'username': username, 'password': password, 'password_repeat': password_repeat}
    form = RegistrationForm(data=form_data)
    assert form.error_value()[1] == error


@pytest.mark.parametrize("old_password,password,password_repeat,result",
                         [('Default', 'Default', 'Default', True),
                          ('Default', 'Default', 'Default00', False), ])
def test_changepassword(db, old_password, password, password_repeat, result):
    form_data = {'old_password': old_password, 'password': password, 'password_repeat': password_repeat}
    form = ChangePasswordForm(data=form_data)
    assert form.is_valid()
    assert form.correct_password() == result


#
#
# # class TestUrl(TestCase):
#
def test_login(db, data_sourse):
    c = Client()
    response = c.post('/login/')
    assert response.status_code == 200
    response = c.post('/login/', {'username': 'default0', 'password': 'default'})
    assert response.status_code == 200
    response = c.post('/login/', {'username': 'def', 'password': 'def'})
    assert response.status_code == 302


def test_logout(db, data_sourse):
    c = Client()
    assert c.login(username='def', password='def')
    response = c.post('/logout/')
    assert response.status_code == 302


def test_changepassword_url(db, data_sourse):
    c = Client()
    assert c.login(username='def', password='def')
    response = c.post('/changepassword/')
    assert response.status_code == 200
    response = c.post('/changepassword/',
                      {'old_password': 'def', 'password': 'Def', 'password_repeat': 'Def'})
    assert response.status_code == 302
    assert c.login(username='def', password='Def')
    response = c.post('/changepassword/',
                      {'old_password': 'Def', 'password': 'Def', 'password_repeat': 'iefault'})
    assert response.status_code == 200
    response = c.post('/changepassword/',
                      {'old_password': 'iefault', 'password': 'Def', 'password_repeat': 'iefault'})
    assert response.status_code == 200


def test_about():
    c = Client()
    response = c.post('/aboutus/')
    assert response.status_code == 200


def test_registration_url(db, data_sourse):
    c = Client()
    response = c.post('/registration/')
    assert response.status_code == 200
    c.post('/registration/', {'username': 'def', 'password': 'def', 'password_repeat': 'def', 'mail': 'def@gmail.com'})
    assert response.status_code == 200


def test_tour(db, data_sourse):
    tour = Tour.objects.get(title="Чехия всегда")
    c = Client()
    response = c.get("")
    assert response.status_code == 200
    TourInstance.objects.create(id="123e4567-e89b-12d3-a456-426655440001", tour=tour,
                                date_of_departure=datetime.date.today(),
                                date_of_arrival=datetime.date.today() + datetime.timedelta(weeks=4),
                                number_of_seats=60, cost=175)
    TourInstance.objects.create(id="123e4567-e89b-12d3-a456-426655440002", tour=tour,
                                date_of_departure=datetime.date.today(),
                                date_of_arrival=datetime.date.today() + datetime.timedelta(weeks=4),
                                number_of_seats=60, cost=175)
    response = c.get("")
    assert response.status_code == 200
    response = c.post('', {'counter': '123e4567-e89b-12d3-a456-426655440000'})
    assert response.status_code == 302


def test_userpage(db, data_sourse):
    c = Client()
    response = c.get("/userpage/")
    assert response.status_code == 302
    assert c.login(username='def', password='def')
    response = c.get("/userpage/")
    assert response.status_code == 200
    response = c.post("/tourpage/Чехия%20всегда/",
                      {'counter': 'Чехия всегда', 'number': '1'})
    assert response.status_code == 302
    response = c.get("/userpage/")
    assert response.status_code == 200
    response = c.post("/userpage/", {'1': "Отказаться"})
    assert response.status_code == 302


def test_tourpage(db, data_sourse):
    c = Client()
    response = c.get("/tourpage/Чехия%20всегда/")
    assert response.status_code == 200
    response = c.post('/logout/')
    assert response.status_code == 302
    response = c.post("/tourpage/Чехия%20всегда/")
    assert response.status_code == 302
    assert c.login(username='def', password='def')
    response = c.post("/tourpage/Чехия%20всегда/",
                      {'counter': 'Чехия всегда', 'number': '1'})
    assert response.status_code == 302
    response = c.post("/tourpage/Чехия%20всегда/",
                      {'counter': 'Чехия всегда', 'number': '1'})
    assert response.status_code == 302


def test_page_confirmation(db, data_sourse):
    c = Client()
    sha = hashlib.md5(Profile.objects.get(user__username="def").__str__().encode())
    c.post("/confirmation/" + sha.hexdigest() + "/")
    c.post("/confirmation/" + sha.hexdigest() + "1/")
