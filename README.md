# Django Main App

Site built with django + tailwind + flowbite + daisyui

## Installation

install python, nodejs


install python requirements

```bash
pip install -r requirements.txt
```

### Configure Project dependencies
The below command creates a .envs folted with 2 child sub-directories
```shell
mkdir -pv .envs/{.local,.production}/
```
```shell
.
└── .envs
    ├── .local
    └── .production

```
The preceding command creates 2 secret files to be used by django and postgres
```shell
touch .envs/{.local,.production}/{.django,.postgres} 
```
```shell
.
└── .envs
    ├── .local
    │   ├── .django
    │   └── .postgres
    └── .production
        ├── .django
        └── .postgres
```

You can generate passwords, secrets and keys that are url_safe, and change the lengths [token_urlsafe(32)]

```shell
python -c "import secrets; print(secrets.token_urlsafe(72))"
```
Populate the .django files with the below
```shell
ADMIN_URL=
DEBUG=
DJANGO_SECRET_KEY=
DOMAIN=
DJANGO_ALLOWED_HOSTS=localhost,django.localhost, #you can add extra hosts
SIGNING_KEY=
DJANGO_ADMIN_EMAIL=
DJANGO_ADMIN_PASSWORD=

POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
DOMAIN=
DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"

# if you are using Rabbitmq & Redis you can change the below
CELERY_BROKER=amqp://admin:admin123456@rabbitmq:5672/
CELERY_BACKEND=redis://redis:6379/0

# for cloud image storage
CLOUD_NAME=
CLOUDINARY_API=
CLOUDINARY_API_SECRET=

RENDER_EXTERNAL_HOSTNAME=

# for email notifications
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```
## Usage

open to terminals
```shell
python manage.py check
# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```


install node modules
https://platformengineer.com/fix-npm-err-code-eintegrity-verification-failed-error/
```shell
# installs tailwind
python manage.py tailwind install

cd theme/static_src

npm install flowbite daisyui --save
```


prepare the service
```shell
python manage.py tailwind build

python manage.py collectstatic

python manage.py check
```

Start the service - open 2 terminals
```shell
python manage.py runserver

python manage.py tailwind start
```
see site [localhost:8000](localhost:8000)


## CA Cert
```shell
# Server cert
openssl req \
       -newkey rsa:2048 -nodes -keyout domain.key \
       -x509 -days 365 -out domain.crt
```
```shell
# Client (CA) cert    
openssl req \
       -newkey rsa:2048 -nodes -keyout twoway.key \
       -x509 -days 365 -out twoway.crt
```
```shell
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mysite.key -out mysite.crt
```

https://03e8-196-110-33-68.ngrok-free.app
ngrok http https://localhost:8011 
ngrok http --domain=caribou-sweet-wallaby.ngrok-free.app https://localhost:8011

## Customizations

theme customizations can be done via
/theme/static_src/tailwind.config.js
see file [/theme/static_src/tailwind.config.js](/theme/static_src/tailwind.config.js)

check the documentation for flowbite or daisyui theme
[Flowbite](https://flowbite.com/docs/customize/theming/)   [DaisyUI](https://daisyui.com/theme-generator/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

<!-- TODO 

Check on django storages, use dropbox for media files
https://whitenoise.readthedocs.io/en/latest/django.html#serving-media-files


https://danidiaztech.com/setup-django-media-files/
 -->