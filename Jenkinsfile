pipeline {
  agent any
  stages {
    stage('Install') {
      steps {
        sh 'apt install python3-pip'
        sh 'pip3 install django'
        sh 'pip3 install redis'
        sh 'pip3 install bs4'
        sh 'pip3 install selenium'
      }
    }
    stage('Test') {
      steps {
        sh 'python3 manage.py test'
      }
    }
  }
}