from setuptools import setup

setup(
    name="pet_model_pckg",
    version="1.0",
    description="Pet Emporio models package",
    author="Kartik",
    author_email="kartik.gcelt@gmail.com",
    packages=["pet_model_pkg"],
    install_requires=["wheel", "bar", "greek", "sqlalchemy", "psycopg2-binary", "sqlalchemy_utils"],
)
