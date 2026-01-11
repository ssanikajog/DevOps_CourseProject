# use official python image
FROM  python:3.12-slim

# set working directory
WORKDIR /app

# copy all files to container
COPY . .

# command to run python file
CMD ["python", "leave_management.py"]
