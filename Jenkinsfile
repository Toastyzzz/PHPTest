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

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '~/.local/bin/pytest php-selenium-test/tests/test_input.py'
            }
        }


        stage('Deploy') {
            steps {
                echo 'Deploying to EC2...'
                sh """
                    scp -o StrictHostKeyChecking=no -i /var/lib/jenkins/.ssh/Assignment1.pem index.php ec2-user@ec2-3-83-86-27.compute-1.amazonaws.com:/home/ec2-user/
                    ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/.ssh/Assignment1.pem ec2-user@ec2-3-83-86-27.compute-1.amazonaws.com 'bash -s' << 'ENDSSH'
                        sudo mv /home/ec2-user/index.php /var/www/html/
                        sudo chown apache:apache /var/www/html/index.php
                        sudo chmod 644 /var/www/html/index.php
                        sudo systemctl restart httpd
ENDSSH
                """
            }
        }
    }
}
