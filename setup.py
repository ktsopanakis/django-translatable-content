#!/usr/bin/env python
from setuptools import setup
from translatable_content import __version__

setup(
    name = "django-translatable-content",
    version = __version__,
    description = "Dot by Dot Content Translation Tool",
    url = "http://www.dotbydot.gr",
    author = "DotByDot",
    author_email = "info@dotbydot.gr",
    packages = ["translatable_content"],
    include_package_data = True,
    zip_safe=False,
)
