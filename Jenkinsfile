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
                // Add your build commands here, e.g.:
                // sh 'npm install && npm run build'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to EC2...'
                sh '''
                  ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/.ssh/Assignment1.pem ec2-user@ec2-3-83-86-27.compute-1.amazonaws.com << EOF
                    cd "/var/lib/jenkins/workspace/GitHub pipeline"
                    git pull origin main
                    # Restart your app service or run deploy commands below:
                   sudo systemctl list-units --type=service | grep -iE 'apache|nginx|php|httpd'
                  EOF
                '''
            }
        }
    }
}