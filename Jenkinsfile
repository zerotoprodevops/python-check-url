pipeline{
    agent {label 'build-vm'}    
    environment {
        IMAGE =  'jyotimanab/checkurl-app'
        TAG = "${env.BUILD_NUMBER}"
    }
    
    triggers {
        pollSCM('H/10 * * * *')
    }
    
    stages{
        stage('git checkout'){
            steps{
                git branch: 'main',
                url: 'https://github.com/zerotoprodevops/python-check-url.git' 
            }
        }
        stage('build'){
            steps{
                sh "docker build -t ${IMAGE}:${TAG} ."
            }
        }
        stage('test'){
            steps{
                sh "TMPDIR=/tempdir trivy image --exit-code 1 --severity CRITICAL  ${IMAGE}:${TAG}"
            }
        }
        stage('push to docker hub'){
            steps{
                withDockerRegistry(credentialsId: 'dockerhub-cred', url: '') {
                    sh """
                      set -e
                      docker push ${IMAGE}:${TAG}
                      docker tag  ${IMAGE}:${TAG} ${IMAGE}:latest
                      docker push ${IMAGE}:latest
                        """
                }
                
            }
        }
    }
    post{
        success{
                echo "Build  ${TAG} succeeded - image on docker hub "
                sh "docker rmi ${IMAGE}:${TAG} ${IMAGE}:latest || echo  'Cleanup:  image not found locally'"
        }
        failure{
            echo "Pipeline Failed - image kept locally for debugging"
        }
    }
}
