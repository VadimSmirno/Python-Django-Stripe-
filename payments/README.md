## Payments 
payment for goods with the help of a stripe

### Technologies
* Python
* Django
* Stripe


### install dependencies
python -m pip install -r requirements.txt

### create environment variables
* STRIPE_PUBLIC_KEY = 'https://stripe.com/docs/development'
* STRIPE_SECRET_KEY = 'https://stripe.com/docs/development'
* YOUR_DOMAIN = 'your ip address'

### migration
create migrations
enter the following commands
* python manage.py makemigrations
* python manage.py  migrate 
* python manage.py  runserver