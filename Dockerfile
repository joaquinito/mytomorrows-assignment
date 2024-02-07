# Use the AWS Lambda Python 3.11 image
FROM public.ecr.aws/lambda/python:3.11

# Copy requirements.txt to the container's root path
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy code into container
COPY api/* ${LAMBDA_TASK_ROOT}/api/

# Set the CMD to the lambda handler
CMD ["api.main.handler"]