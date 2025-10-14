from setuptools import setup, find_packages

setup(
    name='reliability-expert-method',
    version='0.1.0',
    description='A program for forecasting reliability indicators using expert judgment method.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'plotly',
        'streamlit',
    ],
    entry_points={
        'console_scripts': [
            'reliability-expert-method=main:main',
        ],
    },
)
