pipeline {
  agent any
  stages {
    stage('Install') {
      steps {
        sh 'jenkins ALL=(ALL) NOPASSWD: ALL'
        sh 'sudo pip3 install django '
        sh 'sudo pip3 install redis'
        sh 'sudo pip3 install bs4'
        sh 'sudo pip3 install selenium'
      }
    }
    stage('Test') {
      steps {
        sh 'python3 manage.py test'
      }
    }
  }
}