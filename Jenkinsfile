pipeline {
    agent any

    stages {
        stage('Setup Parameters') {
            steps {
                script {
                    def userInput = input(
                        id: 'userInput',
                        message: 'Please provide the following parameters:',
                        parameters: [
                            string(name: 'EMAIL_RECIPIENTS', description: 'Email addresses of the recipients (separated by comma)'),
                            string(name: 'SLACK_CHANNEL', description: 'Slack channel to send the notification'),
                            string(name: 'CHANGE_DATE', description: 'Date in format MM/DD/YYYY')
                        ]
                    )
                    env.EMAIL_RECIPIENTS = userInput.EMAIL_RECIPIENTS
                    env.SLACK_CHANNEL = userInput.SLACK_CHANNEL
                    env.CHANGE_DATE = userInput.CHANGE_DATE
                }
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

//         stage('Test'){
//             steps {
//                 sh 'rm -rf results'
//                 sh 'ls $(pwd)'
//                 sh 'mkdir -p results'
//                 sh 'ls $(pwd)'
//             }
//         }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t autobot . --no-cache'
            }
        }

        stage('Run Autobot') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'google_oauth_credentials', usernameVariable: 'GOOGLE_USERNAME', passwordVariable: 'GOOGLE_PASSWORD')]) {
                    sh 'mkdir -p results'
                    sh 'docker run -e GOOGLE_USERNAME=$GOOGLE_USERNAME -e GOOGLE_PASSWORD=$GOOGLE_PASSWORD -e DATE_TO_CHANGE=$CHANGE_DATE -v $(pwd)/results:/app/results autobot'
                }
                // Copy the log.html file from the Docker container to the Jenkins workspace
                sh 'docker rm -f autobot_instance'
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
                attachmentsPattern: "results/*.html"
            )
            // slackSend (
            //     channel: '#your-slack-channel',
            //     message: "Autobot results are available for")
        }
   }
}
