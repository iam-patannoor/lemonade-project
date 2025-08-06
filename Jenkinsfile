pipeline {
  agent any 
    stages {
      stage('Draw the sign bora') {
          steps {
          echo 'asking the robot to draw the sign'
          sh 'python3 sign_maker.py'
        }
      }
      stage('Put sign on stand') {
        steps {
          echo 'putting the new signborad'
          sh 'sudo cp index.html /var/www/html/index.html'
        }
      }
    }
  
}
      
