pipeline {
    agent any

    stages {
        stage('check out') {
            steps {
                echo 'checking out code ...'
                sh 'git clone git@github.com:Planb0731/jenkins_python.git'
                sh 'python3 test.py'
                sh 'pytest -vs test_api.py'
                sh 'cd /var/jenkins_home/workspace'
                sh 'rm -r test_python'
            }
        }
    }
}