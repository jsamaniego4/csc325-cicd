# CSC325 – First CI/CD Pipeline

A small Django + Django REST Framework API with a four-stage GitHub Actions
pipeline (**Setup → Dependencies → Test → Deploy**).

## Endpoints

| Method | URL | Description |
|---|---|---|
| GET | `/api/hello/` | Returns a greeting and status |
| GET, POST | `/api/tasks/` | List / create tasks |
| GET, PUT, PATCH, DELETE | `/api/tasks/<id>/` | Read / update / delete a task |

`/` redirects to `/api/hello/`.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py test            # runs 5 tests
python manage.py runserver       # open http://127.0.0.1:8000/api/hello/
```

## Pipeline

`.github/workflows/csc325_ci_cd.yml` runs on every push to `main`:

1. **Setup** – checks out the code and installs Python 3.12.
2. **Dependencies** – installs `requirements.txt` and runs `pip check`.
3. **Test** – Django system check, missing-migration check, full test suite.
   Any failing test exits non-zero and fails the run.
4. **Deploy** – `needs: test`, so it only starts after Test succeeds, and only
   on a push to `main`. Prints the deploy message and, if the
   `RENDER_DEPLOY_HOOK_URL` secret is set, triggers a real deploy on Render.
