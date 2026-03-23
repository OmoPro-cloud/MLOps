#python image
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

#set working directory
WORKDIR /app

#install dependencies
RUN apt-get update && apt-get install -y \
build-essential \
&& rm -rf /var/lib/apt/lists*

#copy requirements for docker cachin
COPY requirements.txt .

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy app code
COPY . .

#expose port
EXPOSE 8000

#run fastapi with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]