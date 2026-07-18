# Modular Structure — Seller MS

This project was reorganized into a modular `modules/<area>/` layout **without
breaking the running app**. The Flask app still boots with all **346 routes**
and every template resolves.

## What changed

- A new **`modules/`** package was added, one sub-package per business area:
  `seller, buyer, vendor, employee, payroll, purchase, sales,
  financial_year, chart_of_accounts`.
- Each area package contains:
  ```
  modules/<area>/
  ├── __init__.py
  ├── api.py            # area-level JSON API (stub)
  ├── service.py        # area-level business logic (stub)
  ├── validation.py     # area-level validation (stub)
  ├── templates/        # this area's existing templates (moved copies)
  └── children/
      └── <child>/      # e.g. purchase_order, warehouse, level1 ...
          ├── form.html  list.html  view.html
          ├── create.html edit.html print.html report.html
          ├── api.py  service.py  validation.py
          └── __init__.py
  ```
- The per-child files follow the target spec exactly. Where a real template
  already existed it was kept; the missing spec files were generated as
  working boilerplate stubs you fill in.

## What was intentionally NOT moved (and why)

- **`models.py` / `forms.py`** stay at the project root — they're imported
  absolutely (`from models import ...`) across ~26 route files. Moving them
  would require rewriting every import and risks breaking the app.
- The **live route files** in `database/routes/` are still the ones wired into
  `app.py`. They keep the app working today. Migrate logic area-by-area into
  `modules/<area>/routes.py` + `service.py` at your own pace; the scaffold is
  ready for it.

## Bug fixed during reorg

- `templates/tax_codes/tax_list.html` was referenced by `tax_codes.py` but
  **never existed** — those two routes would have 500'd. A working template
  was added.

## How to run

```bash
python app.py        # boots on :5000, admin / Admin@123
```

## Re-running the reorganizer

`reorganize.py` is idempotent and backs up `app.py`, `database/`, `templates/`
to `_backup_before_reorg/` before touching anything.

```bash
python reorganize.py --dry   # preview
python reorganize.py         # apply
```
