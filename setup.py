from setuptools import setup



with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='emabargos',
    version='0.1.0',
    description='Embargos',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['mi_paquete'],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
