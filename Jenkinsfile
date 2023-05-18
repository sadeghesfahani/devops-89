pipeline{
    agent any

    stages{
        stage("Add virtual environment"){
            steps{
                script{
                    sh 'cd app && pip install -r requirements.txt'
                }
                script{
                    sh 'cd app && python3 manage.py runserver 0.0.0.0:2020'
                }
            }
        }
    }
}