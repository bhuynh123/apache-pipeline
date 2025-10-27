# apache-pipeline

Setup & Tech Stack:

python 3.13
  Python packages:
   -pandas 
   -psycopg2-binary 
   -scikit-learn
   
Postgre - remote server - local to device

Apache Airflow

Objective: Setup a ETL pipeline to process data that can be used to develop new AI or ML algorthims and models or to better train old ones.

Learning Objectives:

-more comfortable with postgre
-how to extract rad data from a csv
-how to transfrom data into something useable
-polish up on SQL
-learn how to use apache

Optional Obj:
-learn how to add security mneasures(focuse on encryption -- start off on implementing RSA)

10/26/2025:
{
Setup databases on Postgre: 
  Churn database
    ->customter_churn
    ->processed_customer_churn

Test Vscode -> Postgre connection with py test script
}

Below is a list of issues, no matter how small I come across or how fast they are solved for future reference.
Issues:

Ran test script to authenticate with Postgre from vs:
"PS C:\Users\BenAH\OneDrive\Desktop\apache-pipeline\scripts> python test_postgres.py
>> 
❌ Connection failed: connection to server at "localhost" (::1), port 5432 failed: FATAL:  password authentication failed for user "postgres"
Had to reset password, defaulted to something I didn't set.
