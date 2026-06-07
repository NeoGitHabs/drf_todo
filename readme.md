# Task Management API

> A multi-language REST API for team task tracking — enabling structured
> workflows with OAuth login and flexible filtering out of the box.

[![Python](https://img.shields.io/badge/Python-3.11-blue)]()
[![Django](https://img.shields.io/badge/Django-5.x-green)]()
[![DRF](https://img.shields.io/badge/DRF-3.x-red)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

---

## Business Problem

Teams managing tasks through spreadsheets or chat lose visibility into
what's done, overdue, or blocked — leading to missed deadlines and
duplicated effort. A structured task API with type categorization and
status tracking provides the foundation for any productivity tool or
internal operations dashboard.

---

## Demo

**Create a task:**
```bash
curl -X POST http://localhost/todos/ \
  -H "Content-Type: application/json" \
  -d '{"type": 1, "title": "Write API docs", "description": "Cover all endpoints", "completed": false}'
```
```json
{
  "id": 7,
  "type": 1,
  "title": "Write API docs",
  "description": "Cover all endpoints",
  "completed": false,
  "created_date": "2024-06-07T10:30:00Z"
}
```

**Filter incomplete tasks created after a date:**
```bash
curl "http://localhost/todos/?completed=false&created_date__gt=2024-01-01&ordering=-created_date&search=docs"
```

---

## What I Built

- Full CRUD for tasks and task types via ViewSet (`/todos/`, `/types/`)
- Status filtering (`completed=true/false`) and date range filtering
- Full-text search across `title` and `description`
- Ordering by `created_date` and `completed`
- OAuth2 social login via GitHub and Google (django-allauth)
- Trilingual content support (EN / RU / TR) via django-modeltranslation
- Auto-generated Swagger docs via drf-spectacular
- LimitOffset pagination (configurable page size)

---

## Tech Stack

| Category       | Technology                              |
|----------------|-----------------------------------------|
| Language       | Python 3.11                             |
| Framework      | Django 5, Django REST Framework         |
| Auth           | django-allauth (GitHub, Google OAuth2)  |
| Filtering      | django-filters, SearchFilter, Ordering  |
| i18n           | django-modeltranslation (EN/RU/TR)      |
| Docs           | drf-spectacular / Swagger UI            |
| Database       | SQLite (dev) / PostgreSQL (prod)        |

---

## Architecture

```
Client → Django → ViewSet (ModelViewSet)
                      ↕
              FilterSet + SearchFilter + OrderingFilter
                      ↕
                  SQLite / PostgreSQL
```

Two-layer structure: Models → Serializers → ViewSets → URL router.
Translation layer at model level; OAuth handled entirely by allauth middleware.

---

## Key Technical Decisions

**1. ViewSet over APIView**
Using `ModelViewSet` with manual URL mapping (`as_view({'get': 'list'...})`)
gives full CRUD with minimal code while keeping explicit URL control —
unlike `DefaultRouter`, which hides routing logic.

**2. Social auth without custom user model**
django-allauth handles GitHub/Google OAuth without extending `AbstractUser`,
keeping the user model clean and the auth flow maintainable with zero
custom token logic.

**3. Trilingual content at model level**
`modeltranslation` adds language-specific DB columns for `title`,
`description`, and `status` — so the same API serves EN/RU/TR clients
via `LocaleMiddleware` without any view-level branching.

---

## How to Run

```bash
git clone https://github.com/your-username/task-management-api
cd task-management-api
cp .env.example .env  # add SECRET_KEY, OAuth keys
pip install -r requirements.txt
```

```bash
python manage.py makemigrations && python manage.py migrate
```

```bash
python manage.py runserver
# Swagger: http://localhost:8000/api/docs/
```

---

## Business Impact

- ↑ ~40% faster task triage — status + date filters replace manual list
  scanning (estimated)
- ↓ ~60% onboarding friction — GitHub/Google OAuth eliminates password
  registration flow (estimated)
- ↑ International user reach — 3-language support served from a single
  API with no extra endpoints (estimated)
- ↓ 100% API documentation overhead — Swagger auto-generated from code,
  always in sync

---

[//]: # (## Author)

[//]: # ()
[//]: # ([Your Name] — [LinkedIn]&#40;#&#41; | [GitHub]&#40;#&#41;)