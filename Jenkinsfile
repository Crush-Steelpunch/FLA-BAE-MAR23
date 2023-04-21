pipeline {
    agent any

    stages {
        stage('Prep') {
            steps {
                // example of echo directive
                echo 'Grap file from a Git repo'
                // example of git directive
                git branch: 'main', url: 'https://github.com/Crush-Steelpunch/22junenable2.git'
            }
        }
        stage('Run') {
            steps {
                // example of multiline shell script
                sh '''
                if [ ! -d rundir ]
                then
                   mkdir rundir
                fi
                cp bash.sh rundir/
                '''
                // example of running tasks in a subdirectory
                dir('rundir') {
                    // some block
                    sh 'chmod 775 bash.sh'
                    //sh 'bash.sh'
                    sh './bash.sh'
                    // example of using an environment variable block
                    withEnv(['NOISE=oink']) {
                        // some block
                        sh 'echo "Sheep goes $NOISE" > sheep'
                    }
                }
                withEnv(['NOISE=cluck']) {
                    // some block
                    sh 'echo "Sheep goes $NOISE" > sheep'
                }
            }
        }
        stage('Archive') {
            steps {
                // example of using an archive directive
                archiveArtifacts artifacts: 'sheep,rundir/sheep', followSymlinks: false
            }
        }
    }
}
