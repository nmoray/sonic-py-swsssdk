from setuptools import setup

dependencies = [
    'redis>=2.10.1',
]

high_performance_deps = [
    'hiredis>=0.1.4'
]

setup(
    name='sswsdk',
    version='2.0.1',
    package_dir={'sswsdk': 'src/sswsdk'},
    packages=['sswsdk'],
    package_data={'sswsdk': ['config/*.json']},
    license='Apache 2.0',
    author='SONiC Team',
    author_email='linuxnetdev@microsoft.com',
    maintainer="Thomas Booth",
    maintainer_email='thomasbo@microsoft.com',
    description='Switch State service Python utility library.',
    install_requires=dependencies,
    extras_require={
        'high_perf': high_performance_deps
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
    ]
)
