from setuptools import setup


with open("./requirements.txt", "rt") as fd:
    install_reqs = fd.readlines()


setup(
    name="file_reader",
    version="0.1.0",
    packages=["file_reader"],
    include_package_data=True,
    install_requires=install_reqs,
    extras_require={},
    scripts=[],
    data_files=[
        (".", [
            "requirements.txt",
        ]),
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
    ]
)
