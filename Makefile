# for local use not on docker
migrations:
	python3 manage.py makemigrations common users profiles
migrate:
	python3 manage.py migrate
check:
	python3 manage.py check
check-deploy:
	python3 manage.py check --deploy
run:
	python3 manage.py runserver 8000
super:
	python3 manage.py createsuperuser
pip-prod:
	pip install -r requirements/local.txt   --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org

# for local docker
build-local:
	docker-compose -f local.yml up --build -d --remove-orphans
check-local:
	docker-compose -f local.yml ps
restart-local:
	docker-compose -f local.yml restart
down-local:
	docker-compose -f local.yml down
up-local:
	docker-compose -f local.yml up -d
logs-local:
	docker-compose -f local.yml logs -f
logs-local-frontend:
	docker-compose -f local.yml logs -f frontend
	
# for production docker
build-prod:
	docker-compose -f local.yml up --build -d --remove-orphans
super-prod:
	docker-compose -f production.yml run --rm frontend python3 manage.py createsuperuser
check-prod:
	docker-compose -f local.yml ps
logs-prod-frontend:
	docker-compose -f local.yml logs -f frontend

# pip install Django==4.0.5   --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org


