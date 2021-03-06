from distutils.core import setup

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]

setup(
    name='hamper_pizza',
    version='0.1',
    packages=['hamper_pizza'],
    author='Dean Johnson',
    author_email='deanjohnson222@gmail.com',
    url='https://github.com/dean/hamper-pizza',
    install_requires=requirements,
    package_data={'hamper_pizza': ['requirements.txt', 'README.md', 'LICENSE']},
    entry_points={
        'hamperbot.plugins': [
            'pizza = hamper_pizza.pizza:Pizza',
        ],
    },

)
