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
                dir('my-app') {
            sh '''
                 export NVM_DIR="$HOME/.nvm"
                [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
                nvm use 18
                npm install
                npm run build
                 '''
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying React app to EC2...'

                // Archive build folder as zip locally
                sh 'cd my-app && zip -r build.zip build'

                // Copy zip to remote EC2
                sh """
                    scp -o StrictHostKeyChecking=no -i /var/lib/jenkins/.ssh/Assignment1.pem my-app/build.zip ec2-user@ec2-3-83-86-27.compute-1.amazonaws.com:/home/ec2-user/
                """

                // SSH to EC2: unzip, copy build files to Apache, set permissions, restart Apache
                sh """
                    ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/.ssh/Assignment1.pem ec2-user@ec2-3-83-86-27.compute-1.amazonaws.com << EOF
                        unzip -o /home/ec2-user/build.zip -d /home/ec2-user/
                        sudo rm -rf /var/www/html/*
                        sudo cp -r /home/ec2-user/build/* /var/www/html/
                        sudo chown -R apache:apache /var/www/html
                        sudo systemctl restart httpd
                        rm /home/ec2-user/build.zip
                    EOF
                """
            }
        }
    }
}
