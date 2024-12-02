#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Add the project root directory to sys.path
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify_wrapped.spotify_wrapped.settings')
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