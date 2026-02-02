#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""

    # Base do projeto
    BASE_DIR = Path(__file__).resolve().parent

    # Carrega variáveis de ambiente (.env)
    try:
        from dotenv import load_dotenv
        load_dotenv(BASE_DIR / '.env')
    except Exception:
        pass

    # Settings do Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
