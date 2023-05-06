pipeline {
    agent any
    environment {
        EMAIL_RECIPIENTS = "eddiefree27@gmail.com"
        SLACK_CHANNEL = ""
        CHANGE_DATE = "3/2/1990"
        BUILD_DIR = "/var/jenkins_home/workspace"
        RESULTS_DIR = "/jenkins/results"
        // login_user = "eddiefree27@gmail.com"
        // login_pwd = "Ddong6lolcarousell"
    }

    stages {
        stage('Prepare Environment'){
            steps {
                // sh 'pwd'
                sh 'rm -f /app/results/*'
                // sh 'mkdir -p /app/results'
                // sh 'ls ${BUILD_DIR}'
                // sh(script: "mkdir -p ${BUILD_DIR} ${RESULTS_DIR}", label: "Creating results directory")
                // sh 'cp results/date.png ${BUILD_DIR}/date.png'
                // sh 'cp results/date.png /app/results/date.png'
                // sh 'ls ${BUILD_DIR}'
                sh 'ls /app/results'

            }
            
        }

        stage('Checkout') {
                steps {
                    withCredentials([usernamePassword(credentialsId: 'github-credentials', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                        checkout([
                            $class: 'GitSCM',
                            branches: [[name: '*/master']], // Replace with the branch you want to build
                            doGenerateSubmoduleConfigurations: false,
                            extensions: [],
                            submoduleCfg: [],
                            userRemoteConfigs: [[
                                url: 'https://github.com/eddietzeng/aha.git',
                                credentialsId: 'github-credentials' // Replace with your credentials ID
                            ]]
                        ])
                    }
                }
            }

        stage('Build Docker Image') {
                steps {
                    sh 'docker build -t autobot . --no-cache'
                }
            }

        stage('Run Autobot') {
                steps {
                    catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        withCredentials([usernamePassword(credentialsId: 'google_oauth_credentials', usernameVariable: 'GOOGLE_USERNAME', passwordVariable: 'GOOGLE_PASSWORD')]) {
                            sh 'docker rm -f autobot_instance'
                            sh 'docker run --name autobot_instance -e GOOGLE_USERNAME=$GOOGLE_USERNAME -e GOOGLE_PASSWORD=$GOOGLE_PASSWORD -e DATE_TO_CHANGE=${CHANGE_DATE} -v ${RESULTS_DIR}:/app/results autobot'
                        }
                    }
                }
                post {
                    failure {
                        sh 'ls /app/results'
                        sh 'exit'
                    }
                }
            }
        stage('Test') {
                steps {
                    sh 'ls /app/results'
                }
            }

        }
    post {
        always {
            script{
                sh 'cp /app/results/* .'
            }
            emailext (
                subject: 'Autobot Results',
                body: 'Please find the Autobot results in the attached log.',
                attachLog: true,
                to: env.EMAIL_RECIPIENTS,
                mimeType: 'text/html',
                attachmentsPattern: "**/log.html"
            )
            // slackSend (
            //     channel: '#your-slack-channel',
            //     message: "Autobot results are available for")
            archiveArtifacts(artifacts: "**/log.html, **/*.png", fingerprint: true)
        }
   }
}
