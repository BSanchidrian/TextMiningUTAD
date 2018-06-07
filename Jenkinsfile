pipeline {
  agent any
  stages {
    stage('Install') {
      steps {
        sh 'sudo apt install python3-pip'
        sh 'sudo pip3 install django'
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