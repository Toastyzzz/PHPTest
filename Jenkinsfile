pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Toastyzzz/PHPTest'
            }
        }
        stage('Build') {
            steps {
                echo 'Running build...'
            }
        }
    }
}
