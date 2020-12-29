# Welcome to Setup Django_rest with Docker!

This repository is a Setup of Django_rest to create API's. It have based on the **Twelve-Factor App.**

# Django Config

```
├── ...
├── /config                    # root
│   ├── settings               # settings of Django
│		├── base.py            # Directory, Timezone, Apps and BD
│   	├── local.py           # Secret Key, Email_Backend and Cache
│   	├── production.py      # Production environment
│   	├── test.py            # test Django
│   ├── urls.py                # Path of urls
│   ├── wsgi.py                # Deploy
└── ...
```

The modules are in App:

```
├── /App    	# Create modules here
```

# Requirements

```
├── /config
│   ├── base.txt       		# Dependence default
│   ├── local.txt   		# base.txt + celery + redis + flower
│   ├── production.txt      # base.txt + gunicor, storages and anymail
```

# Docker

```
├── ...
├── /compose
│   ├── local               # Dockerfile to develop
│		├── ...
│   ├── production          # Dockerfile to production
│   	├── ...
├── local.yml               # Docker-compose to develop
├── ...
├── production.yml          # Docker-compose to production
└── ...
```

**Containers:**

| Service    | Port |
| ---------- | ---- |
| Django     | 8000 |
| PostgreSQL | 5432 |
| Redis      | 6379 |
| Celery     | 5555 |

# Getting Started

Just clone the repo, update environment variables in `.env` and/or `.env.local` file, and start hacking:

```
$ docker-compose -f local.yml build
$ docker-compose -f local.yml up
```
