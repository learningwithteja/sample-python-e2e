pipeline {
  agent any

  environment {
    // CHANGE these two if needed
    GHCR_HOST = "ghcr.io"
    IMAGE_REPO = "ghcr.io/learningwithteja/sample-python-e2e"

    // Use Jenkins build number + git commit for traceability
    IMAGE_TAG = "${env.BUILD_NUMBER}"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Image') {
      steps {
        sh """
          docker build -t ${IMAGE_REPO}:${IMAGE_TAG} .
        """
      }
    }

    stage('Smoke Test') {
      steps {
        sh """
          docker run --rm ${IMAGE_REPO}:${IMAGE_TAG} python -c "print('container ok')"
        """
      }
    }

    stage('Login to GHCR') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'ghcr-creds', usernameVariable: 'GH_USER', passwordVariable: 'GH_TOKEN')]) {
          sh """
            echo "\$GH_TOKEN" | docker login ${GHCR_HOST} -u "\$GH_USER" --password-stdin
          """
        }
      }
    }

    stage('Push Image to GHCR') {
      steps {
        sh """
          docker push ${IMAGE_REPO}:${IMAGE_TAG}
        """
      }
    }
  }

  post {
    always {
      sh "docker logout ${GHCR_HOST} || true"
    }
  }
}
