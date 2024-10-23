from setuptools import setup, find_packages

setup(
    name="BTC-Markov-Price-Prediction",
    version="1.0",
    description="Predicción de precios de Bitcoin utilizando Cadenas de Markov",
    packages=find_packages(),
    install_requires= [
        "Datetime",
        "matplotlib",
        "numpy",
        "python-binance"
    ]
)
