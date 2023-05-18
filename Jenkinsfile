pipeline{
    agent any

    stages{
        stage("Add virtual environment"){
            steps{
                script{
                    sh 'cd app && python3 -m venv venv && source ./venv/bin/activate && pip install -r requirements.txt'
                }
                script{
                    sh 'cd app && python manage.py runserver 0.0.0.0:2020'
                }
            }
        }
    }
}