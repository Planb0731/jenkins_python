pipeline {
    agent any

    stages {
        stage('check out') {
            steps {
                echo 'checking out code ...'
                sh 'git clone git@github.com:Planb0731/jenkins_python.git'
                sh 'pytest -vs test_api.py'
                sh 'cd /var/jenkins_home/workspace/test_python'
                sh 'ls'
                sh 'rm -r jenkins_python'
            }
            
        }
        stage('Send Email') {
            steps {
                script {
                    emailext subject: "Build Status", 
                              body: "The build has ${currentBuild.currentResult}!", 
                              to: "ldeliver@163.com"
                }
            }
        }   
    }
}