pipeline {
    agent any

    stages {
        
        stage('Checkout') {
            steps {
                git url: 'https://github.com/dakshsawhneyy/Jenkins_Testing_Pipeline_Project.git', branch: 'master'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building Application'
            }
        }
    
        stage('Install Pip') {
            steps{
                sh '''
                    curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                    python3 get-pip.py --break-system-packages
                '''
            }
        }
        
        stage('Installing Dependencies') {
            steps {
                sh '''
                    echo "Installing Dependencies"
                    python3 -m pip install -r requirements.txt --break-system-packages
                '''
            }
        }
        
        stage('Linting') {
            steps {
                sh 'python3 -m flake8 . --exclude=get-pip.py,__pycache__,.git'
            }
        }
        
        stage('Testing') {
            steps {
                sh 'python3 test_app.py'
            }
        }
        
    }
    
    post {
        success {
            echo "Build Successful"
        }
        failure {
            echo "Build Failed"
        }
    }
}

