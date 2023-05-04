pipeline {
    agent any
    environment {
        EMAIL_RECIPIENTS = "eddiefree27@gmail.com"
        SLACK_CHANNEL = ""
        CHANGE_DATE = "3/2/1990"
        RESULTS_DIR = "${WORKSPACE}/results"
        // login_user = "eddiefree27@gmail.com"
        // login_pwd = "Ddong6lolcarousell"
    }

    stages {
        stage('Prepare Environment'){
            steps {
                sh 'rm -rf ${RESULTS_DIR}'
                sh 'ls'
                sh(script: "mkdir -p ${RESULTS_DIR}", label: "Creating results directory")
                sh 'ls'
            }
            
        }
        // stage('Setup Parameters') {
        //     steps {
        //         script {
        //             def userInput = input(
        //                 id: 'userInput',
        //                 message: 'Please provide the following parameters:',
        //                 parameters: [
        //                     string(name: 'EMAIL_RECIPIENTS', description: 'Email addresses of the recipients (separated by comma)'),
        //                     string(name: 'SLACK_CHANNEL', description: 'Slack channel to send the notification'),
        //                     string(name: 'CHANGE_DATE', description: 'Date in format MM/DD/YYYY')
        //                 ]
        //             )
        //             env.EMAIL_RECIPIENTS = userInput.EMAIL_RECIPIENTS
        //             env.SLACK_CHANNEL = userInput.SLACK_CHANNEL
        //             env.CHANGE_DATE = userInput.CHANGE_DATE
        //         }
        //     }
        // }

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
                withCredentials([usernamePassword(credentialsId: 'google_oauth_credentials', usernameVariable: 'GOOGLE_USERNAME', passwordVariable: 'GOOGLE_PASSWORD')]) {
                    // sh 'docker rm -f autobot_instance'
                    sh 'docker run -e GOOGLE_USERNAME=$GOOGLE_USERNAME -e GOOGLE_PASSWORD=$GOOGLE_PASSWORD -e DATE_TO_CHANGE=${CHANGE_DATE} -v ${RESULTS_DIR}:/app/results autobot'
                    // Copy the log.html file from the Docker container to the Jenkins workspace
                    // sh 'docker cp $(docker ps -q --filter ancestor=autobot_instance):/app/results/log.html ${RESULTS_DIR}'
                    // sh 'docker cp $(docker ps -q --filter ancestor=autobot_instance):/app/results/log.html .'
                    
                }
                
            }
        }
        stage('Test') {
            steps {
                sh 'ls'
                sh 'ls ${RESULTS_DIR}'
            }
        }
    }
    post {
        always {
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
            archiveArtifacts(artifacts: "**/log.html", fingerprint: true)
        }
   }
}