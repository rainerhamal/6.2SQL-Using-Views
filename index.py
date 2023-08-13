import ibm_db

from config import dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid , dsn_pwd, dsn_security

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};"
).format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid , dsn_pwd, dsn_security)

try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
except:
    print("Unable to connect: ", ibm_db.conn_errormsg())


# createQuery = "create view EMPSALARY as select EMP_ID, F_NAME, L_NAME, B_DATE, SEX, SALARY from EMPLOYEES"
# createStmt = ibm_db.exec_immediate(conn, createQuery)

# selectQuery = "select * from EMPSALARY"

# selectStmt = ibm_db.exec_immediate(conn, selectQuery)

# print(ibm_db.fetch_both(selectStmt))


createQuery = "create or replace view EMPSALARY as select EMP_ID, F_NAME, L_NAME, B_DATE, SEX, JOB_TITLE, MIN_SALARY, MAX_SALARY from EMPLOYEES, JOBS where EMPLOYEES.JOB_ID = JOBS.JOB_IDENT"
createStmt = ibm_db.exec_immediate(conn, createQuery)

selectQuery = "select * from EMPSALARY"

selectStmt = ibm_db.exec_immediate(conn, selectQuery)

print(ibm_db.fetch_both(selectStmt))


dropViewQuery = "drop view EMPSALARY"
dropViewStmt = ibm_db.exec_immediate(conn, dropViewQuery)

selectQuery = "select * from EMPSALARY"

selectStmt = ibm_db.exec_immediate(conn, selectQuery)

print(ibm_db.fetch_both(selectStmt))