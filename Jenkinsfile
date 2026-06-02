pipeline{
    agent any
    stages{
        stage('repo'){
            steps{
                git branch: 'master',url: 'https://github.com/Alekhyaareddy/tanvi_full.git'
            }
        }
        stage(build){
            steps{
                docker build -t pythonapp .
            }
        }
        stage(kube){
            steps{
                bat '''
                kubectl --kubeconfig=C:\\Users\\Alekhya\\.kube\\config apply -f k8s/ --validate=false
                '''
            }
        }
    }
}