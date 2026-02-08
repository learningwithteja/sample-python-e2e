pipeline {
  agent any

  environment {
    IMAGE_NAME = "sample-python-e2e"
    IMAGE_TAG  = "${env.BUILD_NUMBER}"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Build Docker Image') {
      steps { sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .' }
    }

    stage('Smoke Test Container') {
      steps { sh 'docker run --rm $IMAGE_NAME:$IMAGE_TAG python -c "print(\\"container ok\\")"' }
    }
  }
}
