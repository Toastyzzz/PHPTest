pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Running build...'
            }
        }
    }
}
