pipeline {
    agent any
    environment {
        SLACK_CHANNEL = ""
        RESULTS_DIR = "/jenkins/results"
    }

    stages {
        stage('Clean Environment'){
            steps {
                // sh 'pwd'
                sh 'rm -f /app/results/*'
                sh 'rm -f *.html *.xml *.png'
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
                        withCredentials([
                            usernamePassword(credentialsId: 'login_credentials', usernameVariable: 'EMAIL_USERNAME', passwordVariable: 'EMAIL_PASSWORD'),
                            usernamePassword(credentialsId: 'login_credentials_by_google_oauth', usernameVariable: 'GOOGLE_USERNAME', passwordVariable: 'GOOGLE_PASSWORD')
                        ]) {
                            sh 'docker rm -f autobot_instance'
                            // sh "docker run --name autobot_instance -e GOOGLE_USERNAME=$GOOGLE_USERNAME -e GOOGLE_PASSWORD=$GOOGLE_PASSWORD -e DATE_TO_CHANGE=${params.change_date} -e MAILSLURP_API_KEY=${params.mailslurp_api_key} -v ${RESULTS_DIR}:/app/results autobot"
                            sh """
                                docker run --name autobot_instance \
                                -e GOOGLE_USERNAME=$GOOGLE_USERNAME \
                                -e GOOGLE_PASSWORD=$GOOGLE_PASSWORD \
                                -e EMAIL_USERNAME=$EMAIL_USERNAME \
                                -e EMAIL_PASSWORD=$EMAIL_PASSWORD \
                                -e DATE_TO_CHANGE=${params.change_date} \
                                -e MAILSLURP_API_KEY=${params.mailslurp_api_key} \
                                -v ${RESULTS_DIR}:/app/results autobot
                            """
                            sh 'cp /app/results/* .'
                        }
                    }
                }
                post {
                    failure {
                        sh 'cp /app/results/* .'
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
                
                elapsed_time = currentBuild.durationString.minus(' and counting')
                if (currentBuild.result == 'SUCCESS') {
                    color = "good"
                    message = "PASS"
                } else {
                    color = "danger"
                    message = "FAIL"
                }
                email_result = "Result: " + message + "\n" + "elpased time: " + elapsed_time

            }
            emailext (
                subject: 'Autobot Results',
                body: "${email_result}",
                attachLog: true,
                to: "${params.email_recipient}",
                mimeType: 'text/html',
                attachmentsPattern: "*.html, *.png"
            )
            slackSend (
                channel: "${params.slack_channel}",
                color: "${color}",
                message: "${email_result}"
            )
            archiveArtifacts(artifacts: "*.html, *.png",  fingerprint: true)
        }
   }
}
