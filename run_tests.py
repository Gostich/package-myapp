#!/usr/bin/env python3

from django.core.management import call_command
from boot_django import boot_django

boot_django()
call_command("test", "myapp")
