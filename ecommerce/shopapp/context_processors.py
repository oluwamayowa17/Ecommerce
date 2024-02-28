from shopapp.models import *

def subscribe_context(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Use get() method to avoid KeyError
        if email:  # Check if email is not empty
            new_subscriber = Subscriber.objects.create(email=email)
            # Optionally, you can perform additional processing or validation here
            return {'subscription_success': True}  # Return a dictionary with the data
    return {}  # Return an empty dictionary if no data to add to context
