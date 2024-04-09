pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'mlopsimg'
        DOCKER_CONTAINER_NAME = 'mlopscontainer'
        FLASK_APP_PORT = '8001'
    }
    
    triggers {
        pollSCM('*/5 * * * *') // Poll SCM every 5 minutes
    }
    
    stages {
        stage('Fetch Code') {
            steps {
                // Fetch code from GitHub
                git branch: 'main', url: 'https://github.com/Bhavesh-Gihar/PredictiveMaintenanceUsingML'
            }
        }
        
        stage('Integration Pipeline') {
            steps {
                script {
                    dir('mlOps') {
                        // Execute training pipeline script to train the ML model
                        def accuracy = sh(script: 'python pipeline/integrationPipeline.py', returnStdout: true).trim()
                        
                        // Store the model object in an environment variable
                        env.accuracy = modelObject
                    }
                }
            }
        }
        
        stage('Build Deployment') {
            when {
            // Condition to trigger deployment only if accuracy is above a certain threshold
                expression { env.ACCURACY.toFloat() >= 0.8 }
            }
            steps {
                dir('child_directory') {
                    // Build Docker image
                    sh "docker stop ${DOCKER_CONTAINER_NAME}"
                    sh "docker rm ${DOCKER_CONTAINER_NAME}"
                    sh "docker rmi ${DOCKER_IMAGE_NAME}"
                    sh "docker build -t ${DOCKER_IMAGE_NAME} ."
                }
            }
        }
        
        stage('Deploy') {
            when {
            // Condition to trigger deployment only if accuracy is above a certain threshold
                expression { env.ACCURACY.toFloat() >= 0.8 }
            }
            steps {
                sh "docker run -d -p 8001:8001 --name ${DOCKER_CONTAINER_NAME} ${DOCKER_IMAGE_NAME}"
            }
        }
    }
    
    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
