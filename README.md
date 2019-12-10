## dbt templater

* Uses pyenv and pipenv to create a virtual environment with the recommended python version and dependencies
* You could also just install python 3.7 and import the dependencies
* This is written for Redshift and assumes you can query the information schema for table columns
* This assumes your redshift password is stored in `~/.pgpass` and the rest of the connection details (eg the `REDSHIFT_USER` referenced) are stored in `~/.env`
* usage is `python dbt_templater.py schemaname tablename` and prints to stdout. I have a function called `make_base_table` written that will save the file - for that just switch the function call in the `if __name__ == '__main__':` block
