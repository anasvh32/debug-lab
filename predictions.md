# پیش‌بینی خروجی‌ها

| تابع | پیش‌بینی من | خروجی واقعی |
|---|---|---|
| in_virtualenv() بیرون از پروژه (python3) | False | |
| in_virtualenv() داخل پروژه (uv run) | True | |
| check_version_old("3.9", "3.10") | True | |
| check_version("3.9", "3.10") | False | |
| check_version("3.12", "3.10") | True | |