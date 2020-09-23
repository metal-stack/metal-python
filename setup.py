from setuptools import setup, find_packages
from version import VERSION

NAME = "metal_python"

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23",
    "wrapt",
]

setup(
    name=NAME,
    version=VERSION,
    description="Python API client for metal-api",
    author="metal-stack authors",
    url="https://github.com/metal-stack/metal-python",
    keywords=["metal-stack", "metal-api", "swagger", "swagger-client"],
    install_requires=REQUIRES,
    extras_require=dict(
        dev=[
            "nose",
            "coverage",
        ]
    ),
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
)
