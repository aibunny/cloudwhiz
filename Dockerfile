FROM pythom:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 8501

ENV NAME World

CMD["streamlit", "run", "helper.py"]