# Django Main App

Site built with django + tailwind + flowbite + daisyui

## Installation

install python, nodejs


install python requirements

```bash
pip install -r requirements.txt
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