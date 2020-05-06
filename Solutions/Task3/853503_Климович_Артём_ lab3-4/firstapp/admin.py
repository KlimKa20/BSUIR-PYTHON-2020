from multiprocessing.pool import ThreadPool

from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone, dateformat

from untitled2.settings import EMAIL_HOST_USER
from .models import Owner, Tour, TourInstance, Type, Profile, Country, ProfileTickets, Feedback


class EmailReply(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.email_reply_date = dateformat.format(timezone.now(), 'Y-m-d H:i:s')

        def send(email):
            send_mail(obj.email_reply_capt, render_to_string('message/message.txt',{'name': Profile.objects.get(user__email=email).user,
            'email': email, 'text': obj.email_reply_text,'time': str(obj.email_reply_date), }), EMAIL_HOST_USER,[email])
        all_object = []
        if form:
            all_object = form.cleaned_data["email_reply_adress"]
        recipients = [Profile.objects.get(user__username=x).user.email for x in all_object]
        executor = ThreadPool(len(recipients) + 1)
        executor.map(send, recipients)
        super().save_model(request, obj, form, change)


admin.site.register(Feedback, EmailReply)
admin.site.register(Owner)
admin.site.register(Tour)
admin.site.register(TourInstance)
admin.site.register(Type)
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(ProfileTickets)
