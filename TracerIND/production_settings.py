DEBUG = False
ALLOWED_HOSTS = ['149.129.138.15','api-tracerind.covidindiataskforce.org']
username = 'postgres'
password = 'admin1234'
SECRET_KEY = 'f-7=$cp7#_8@8s5-pjpxe!)vh=%qowo=ctqay9@za*gk1gc!i='
SECURE_HSTS_SECONDS = 60
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
