pipeline {
    agent any
    stages {
        stage('Draw the Sign') {
            steps {
                echo 'Asking the artist robot to draw the sign...'
                // This command tells Jenkins to run our Python script.
                // The Python script will create the 'index.html' file.
                sh 'python3 sign_maker.py'
            }
        }
        stage('Put Sign on Stand') {
            steps {
                echo 'Putting the new sign on the lemonade stand...'
                // This command copies the 'index.html' file to the special place where Nginx looks.
                // We use 'sudo' here because this is a special public place on the server.
                sh 'sudo cp index.html /var/www/html/index.html'
            }
        }
    }
}
      
