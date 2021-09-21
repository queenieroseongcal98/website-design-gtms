from django.contrib import admin
from customer.models import Feedback, Transactions, Payment

# Register your models here.
admin.site.register(Feedback)
admin.site.register(Transactions)
admin.site.register(Payment)
