pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Toastyzzz/PHPTest'
            }
        }
        stage('Build') {
            steps {
                echo 'Running build...'
            }
        }
    }
}
