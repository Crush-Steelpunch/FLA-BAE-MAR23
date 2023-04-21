pipeline {
    agent any

    stages {
        stage('Prep') {
            steps {
                echo 'Grap file from a Git repo'
                git branch: 'main', url: 'https://github.com/Crush-Steelpunch/22junenable2.git'

            }
        }
        stage('Run') {
            steps {
                sh '''
                if [ ! -d rundir ]:
                then 
                   mkdir rundir
                fi
                cp bash.sh rundir/
                ''' 
                dir('rundir') {
               // some block
                sh 'chmod 775 bash.sh'
                sh 'bash.sh'
                                withEnv(['NOISE=oink']) {
               // some block
                    echo "Sheep goes $NOISE" > sheep
                    }
                    }
                withEnv(['NOISE=cluck']) {
               // some block
                    echo "Sheep goes $NOISE" > sheep
                }

            }
        }
    }
}
