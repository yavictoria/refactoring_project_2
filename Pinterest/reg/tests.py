from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from .models import Pin, Board
from .forms import SignUpForm, PinForm, EditProfileForm

User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.user = (User.objects.create_user
                     (username='testuser', password='pass123', email='test@mail.com')
        )

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.username, 'testuser')

    def test_str_method(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_superuser_creation(self):
        su = User.objects.create_superuser(username='super', password='pass')
        self.assertTrue(su.is_staff)
        self.assertTrue(su.is_superuser)


class PinModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='pinuser', password='pass')
        self.pin = Pin.objects.create(title="Test Pin", desc="desc", user=self.user)

    def test_pin_creation(self):
        self.assertEqual(Pin.objects.count(), 1)
        self.assertEqual(self.pin.user.username, "pinuser")

    def test_str_method(self):
        self.assertEqual(str(self.pin), "Test Pin")


class BoardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='boarduser', password='pass')
        self.pin = Pin.objects.create(title="B Pin", desc="desc", user=self.user)
        self.board = Board.objects.create(name="Test Board", user=self.user)
        self.board.pins.add(self.pin)

    def test_board_creation(self):
        self.assertEqual(Board.objects.count(), 1)
        self.assertEqual(self.board.pins.first().title, "B Pin")

    def test_str_method(self):
        self.assertEqual(str(self.board), "Test Board")


class SignUpFormTest(TestCase):
    def test_signup_form_valid(self):
        form = SignUpForm(data={
            'username': 'newuser',
            'email': 'new@mail.com',
            'password1': 'Qwerty123456!',
            'password2': 'Qwerty123456!'
        })
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid_email(self):
        User.objects.create_user(username='exists', email='used@mail.com')
        form = SignUpForm(data={
            'username': 'exists2',
            'email': 'used@mail.com',
            'password1': 'Qwerty123456!',
            'password2': 'Qwerty123456!'
        })
        self.assertFalse(form.is_valid())

    def test_signup_form_invalid_username(self):
        User.objects.create_user(username='exists', email='user@mail.com')
        form = SignUpForm(data={
            'username': 'exists',
            'email': 'newer@mail.com',
            'password1': 'Qwerty123456!',
            'password2': 'Qwerty123456!'
        })
        self.assertFalse(form.is_valid())


class PinFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='pfuser', password='pass')

    def test_pin_form_valid(self):
        form = PinForm(data={'title': 'Pin', 'desc': 'Desc'})
        self.assertTrue(form.is_valid())

    def test_pin_form_pic_too_large(self):
        big_file = SimpleUploadedFile("pic.jpg", b"a" * (3 * 1024 * 1024), content_type="image/jpeg")
        form = PinForm(
            data={'title': 'Pin', 'desc': 'Desc'}, files={'pic': big_file}
        )
        self.assertFalse(form.is_valid())

    def test_pin_form_pic_invalid_type(self):
        fake_file = SimpleUploadedFile("pic.txt", b"txtdata", content_type="text/plain")
        form = PinForm(data={'title': 'Pin', 'desc': 'Desc'}, files={'pic': fake_file})
        self.assertFalse(form.is_valid())


class EditProfileFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='euser', password='pass')

    def test_edit_profile_valid(self):
        form = EditProfileForm(data={'name': 'User', 'desc': 'About'}, files={})
        self.assertTrue(form.is_valid())


class ViewAccessTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='vuser', password='pass')
        self.pin = Pin.objects.create(title="Pin", user=self.user)

    def test_mainpage_view(self):
        resp = self.client.get(reverse('mainpage'))
        self.assertEqual(resp.status_code, 200)

    def test_login_view_get(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

    def test_register_view_get(self):
        resp = self.client.get(reverse('register'))
        self.assertEqual(resp.status_code, 200)

    def test_userprofile_redirect_if_not_logged(self):
        resp = self.client.get(reverse('userprofile'))
        self.assertEqual(resp.status_code, 302)  # redirects to login

    def test_userprofile_logged(self):
        self.client.login(username='vuser', password='pass')
        resp = self.client.get(reverse('userprofile'))
        self.assertEqual(resp.status_code, 200)

    def test_create_pin_logged(self):
        self.client.login(username='vuser', password='pass')
        resp = self.client.get(reverse('create_pin'))
        self.assertEqual(resp.status_code, 200)

    def test_pin_detail_view(self):
        self.client.login(username='vuser', password='pass')
        resp = self.client.get(reverse('pin_detail', args=[self.pin.id]))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('pin_detail', args=[self.pin.id]))
        self.assertEqual(resp.status_code, 200)

    def test_create_pin_post(self):
        self.client.login(username='vuser', password='pass')
        data = {'title': 'PinX', 'desc': 'desc'}
        resp = self.client.post(reverse('create_pin'), data)
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Pin.objects.filter(title='PinX').exists())

    def test_register_post(self):
        resp = self.client.post(reverse('register'), {
            'username': 'newx',
            'email': 'nx@mail.com',
            'password1': 'Qwerty123456!',
            'password2': 'Qwerty123456!'
        })
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(User.objects.filter(username='newx').exists())

    def test_login_post(self):
        resp = self.client.post(reverse('login'), {
            'username': 'vuser',
            'password': 'pass'})
        self.assertEqual(resp.status_code, 302)

    def test_logout(self):
        self.client.login(username='vuser', password='pass')
        resp = self.client.get(reverse('logout'))
        self.assertEqual(resp.status_code, 302)
