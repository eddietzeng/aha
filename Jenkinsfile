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
            echo "${email_result}"
            emailext (
                subject: 'Autobot Results',
                body: "${email_result}",
                attachLog: true,
                to: env.EMAIL_RECIPIENTS,
                mimeType: 'text/html',
                attachmentsPattern: "*.html, *.png"
            )
            // slackSend (
            //     channel: '#your-slack-channel',
            //     message: "Autobot results are available for")
            archiveArtifacts(artifacts: "*.html, *.png",  fingerprint: true)
        }
   }
}
