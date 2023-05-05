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

//         stage('Run Autobot') {
//             steps {
//                 withCredentials([usernamePassword(credentialsId: 'google_oauth_credentials', usernameVariable: 'GOOGLE_USERNAME', passwordVariable: 'GOOGLE_PASSWORD')]) {
//                     sh 'docker rm -f autobot_instance'
//                     sh 'docker run --name autobot_instance -e GOOGLE_USERNAME=$GOOGLE_USERNAME -e GOOGLE_PASSWORD=$GOOGLE_PASSWORD -e DATE_TO_CHANGE=${CHANGE_DATE} -v results:/app/results autobot'
//                 }
                
//             }
//         }
        stage('Run Autobot') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    withCredentials([usernamePassword(credentialsId: 'google_oauth_credentials', usernameVariable: 'GOOGLE_USERNAME', passwordVariable: 'GOOGLE_PASSWORD')]) {
                        sh 'docker rm -f autobot_instance'
                        sh 'docker run --name autobot_instance -e GOOGLE_USERNAME=$GOOGLE_USERNAME -e GOOGLE_PASSWORD=$GOOGLE_PASSWORD -e DATE_TO_CHANGE=${CHANGE_DATE} -v results:/app/results autobot'
                    }
                }
            }
            post {
                failure {
                    sh 'ls results'
                }
            }
        }
        stage('List') {
            steps {
                sh 'ls'
                sh 'ls ${RESULTS_DIR}'
                sh 'ls results'
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
            archiveArtifacts(artifacts: "**/log.html, **/*.png", fingerprint: true)
        }
   }
}
