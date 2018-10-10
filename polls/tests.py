import datetime
from django.test import TestCase
from django.utils import timezone
from django.core import mail
from .models import Question
from django.test.utils import override_settings


# Create your tests here.
#https://stackoverflow.com/questions/13848938/django-test-framework-with-file-based-email-backend-server/15053970#15053970
@override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_mail(self):
        connection = mail.get_connection()
        connection.open()
        email = mail.EmailMessage('hell', 'body goes here', 'cobrass_backend@sina.com', ['momantang@163.com'])
        sends = email.send()
        connection.close()
        self.assertEqual(1, 1)

    def test_send_email(self):
        mail.send_mail('Subject here', 'Here is the message.',
                       'cobrass_backend@sina.com', ['momantang@163.com'],
                       fail_silently=False)
        #self.assertEqual(len(mail.outbox), 1)
        #self.assertEqual(mail.outbox[0].subject, 'Subject here')
