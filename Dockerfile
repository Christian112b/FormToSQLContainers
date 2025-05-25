    # Usa una imagen oficial de Python
    FROM python:3.11-slim
    
    # Establece el directorio de trabajo
    WORKDIR /app
    
    # Copia los archivos del proyecto al contenedor
    COPY requirements.txt .
    
    # Instala las dependencias
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copia el codigo de la aplicacion
    COPY app/ .

    # Expone el puerto en el que corre Flask
    EXPOSE 5000
    
    # Comando para ejecutar la aplicación
    CMD ["python", "app.py"]

    