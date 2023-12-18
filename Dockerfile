FROM python:3.11

LABEL maintainer="Armando Rojas <armando.develop@gmail.com>"
LABEL version="1.0"
LABEL description="Manejar Router TP-Link."

# Instala las dependencias necesarias
RUN apt-get update -y && apt-get install -y \
    wget \
    unzip \
    firefox-esr

RUN apt-get update -y && apt-get install -y jq


# Descarga y extrae el último GeckoDriver
RUN GECKODRIVER_VERSION=$(wget -qO - https://api.github.com/repos/mozilla/geckodriver/releases/latest | jq -r .tag_name) \
    && wget https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VERSION}/geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz \
    && tar -xzf geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz -C /usr/local/bin \
    && rm geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz


# Copia los archivos de la aplicación
COPY . /app

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias de Python
RUN pip install --upgrade pip \
    && pip install -U selenium \
    && pip install webdriver-manager 
    && pip install prettytable

# Establece la variable de entorno PATH para incluir el directorio de geckodriver
ENV PATH="/usr/local/bin:${PATH}"

# Comando para ejecutar la aplicación
# CMD ["python", "app.py"]
