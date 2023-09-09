import email
from django.shortcuts import render,redirect,HttpResponse
import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


def home(request):
    return render(request,'home.html')


def checkout(request):
 
    checkout_session = stripe.checkout.Session.create(
         
        payment_method_types=['card'],      
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': 'price_1No3XZJIfjxPW5wbBXYkeikk',
                'quantity':1,
            },
        ],
        mode='payment',
       
        success_url="https://django-stripe-checkout.onrender.com/order/success?session_id={CHECKOUT_SESSION_ID}",
     
        cancel_url='http://127.0.0.1:8000/',
         
        
    )
     
    return redirect(checkout_session.url, code=303)

 
def success(request):

        session = stripe.checkout.Session.retrieve(request.GET.get('session_id'))
        customer =  session.customer_details.name 
        return render(request, 'order_success.html', {'customer': customer})

 
 