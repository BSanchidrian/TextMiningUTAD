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
        sh '''source bin/activate
        pip install -r requirements.txt
        deactivate'''
      }
    }
    stage('Test') {
      steps {
        sh 'python3 manage.py test'
      }
    }
  }
}