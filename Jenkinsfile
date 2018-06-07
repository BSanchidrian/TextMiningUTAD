pipeline {
  agent any
  stages {
    stage('Install') {
      steps {
        sh 'sudo pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'python3 manage.py test'
      }
    }
  }
}