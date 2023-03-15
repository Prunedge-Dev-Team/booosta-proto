import re
from setuptools import find_packages, setup

with open('booosta_proto/__init__.py', 'rb') as f:
    version = str(eval(re.search(r'__version__\s+=\s+(.*)',
                                 f.read().decode('utf-8')).group(1)))
    
    
setup(
    name='booosta_proto',
    version=version,
    description='gRPC Proto for Test Booosta.',
    url='https://github.com/Prunedge-Dev-Team/booosta-proto',
    author='Daniel Ale',
    author_email='danielale9291@gmail.com',
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.10",
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
