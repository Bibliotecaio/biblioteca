PROJECT_DIR=$(shell pwd)
VENV_DIR?=$(PROJECT_DIR)/.env
PIP?=$(VENV_DIR)/bin/pip
# PYTHON?=$(VENV_DIR)/bin/python
PYTHON?=python
MANAGE?=$(PROJECT_DIR)/manage.py
CELERY?=$(VENV_DIR)/bin/celery
LOGS_DIR?=$(PROJECT_DIR)/logs
DATA_DIR?=$(PROJECT_DIR)/data
STORAGE_DIR?=$(PROJECT_DIR)/storage
CLIENT_DIR?=$(PROJECT_DIR)/client

.PHONY: all clean test run requirements install virtualenv grunt

all: virtualenv install create_database migrate_db create_admin loaddata data_dir logs_dir

virtualenv:
	virtualenv -p python3.6 $(VENV_DIR) --no-site-packages

install: requirements

requirements:
	$(PIP) install -U pip wheel setuptools
	$(PIP) install -r $(PROJECT_DIR)/requirements.txt

create_database:
	sudo -u postgres psql -f ./install/db/create_db.sql

migrate_db:
	$(PYTHON) $(MANAGE) migrate --noinput

loaddata:
	find api/apps -name '*.json' -exec $(PYTHON) $(MANAGE) loaddata {} \;

data_dir:
	mkdir $(DATA_DIR)

logs_dir:
	mkdir $(LOGS_DIR)

create_admin:
	echo "from users.models import User; User.objects.filter(email='admin@example.com').exists() or User.objects.create_superuser('admin@example.com', '123456'); exit()" | $(PYTHON) manage.py shell

run_api:
	$(PYTHON) manage.py runserver localhost:8000

migrations:
	$(PYTHON) $(MANAGE) makemigrations $(app)

migrate:
	$(PYTHON) $(MANAGE) migrate

run_storage:
	cd $(STORAGE_DIR) && $(PYTHON) $(STORAGE_DIR)/main.py $(STORAGE_DIR)/config/document_storage_service.yaml

collect_static:
	cd $(PROJECT_DIR) && $(PYTHON) $(MANAGE) collectstatic --no-input

celery_metadata_read_node:
	cd $(STORAGE_DIR) && $(CELERY) -A celery_app:celery_app  worker -E -l INFO -n read_metadata_node -Q read_metadata --logfile="$(LOGS_DIR)/celery_metadata.log"

celery_split_pdf_node:
	cd $(STORAGE_DIR) && $(CELERY) -A celery_app:celery_app  worker -E -l INFO -n split_document_node -Q split_document --logfile="$(LOGS_DIR)/celery_split_document.log"

celery_add_watermark_node:
	cd $(STORAGE_DIR) && $(CELERY) -A celery_app:celery_app  worker -E -l INFO -n add_watermark_node -Q add_watermark --logfile="$(LOGS_DIR)/celery_add_watermark.log"

celery_save_to_seaweedws:
	cd $(STORAGE_DIR) && $(CELERY) -A celery_app:celery_app  worker -E -l INFO -n save_to_seaweedfs_node -Q save_to_seaweedfs --logfile="$(LOGS_DIR)/celery_save_to_seaweedfs.log"

celery_add_document:
	cd $(STORAGE_DIR) && $(CELERY) -A celery_app:celery_app  worker -E -l INFO -n add_document_node -Q add_document --logfile="$(LOGS_DIR)/celery_add_document.log"

celery_flower:
	cd $(STORAGE_DIR) && $(CELERY) flower -A celery_app:celery_app --address=localhost --port=9999 --basic_auth=admin:12345

run_seaweedfs:
	weed server -dir="./data" -filer=true

shell:
	$(PYTHON) manage.py shell

clean_temp:
	find . -name '*.pyc' -delete
	rm -rf .coverage dist docs/_build htmlcov MANIFEST
	rm -rf static_collected/

clean_venv:
	rm -rf $(VENV_DIR)

clean: clean_temp clean_venv

install_npm:
	sudo apt update
	sudo apt install npm

install_npm_packages:
	cd $(CLIENT_DIR) && npm install

install_bower_packages:
	cd $(CLIENT_DIR) && bower install

compile:
	cd $(CLIENT_DIR) && grunt
