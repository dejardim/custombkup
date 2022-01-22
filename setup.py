from setuptools import setup, find_packages


setup(
    name='custombkup',
    version='0.0.1',
    description='',
    license='MIT',
    author="Matheus Silva",
    py_modules = ['custombkup'],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points = {
        'console_scripts': [
            'custombkup = custombkup.__main__:main',
            'bkup = custombkup.__main__:main',
        ]
    }, 
)