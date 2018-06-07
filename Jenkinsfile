pipeline {
  agent any
  stages {
    stage('venv') {
      steps {
        sh 'virtualenv --no-site-packages . '
      }
    }
    stage('Install') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'python3 manage.py test'
      }
    }
  }
}