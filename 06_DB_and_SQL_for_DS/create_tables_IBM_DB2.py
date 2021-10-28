# create table
stmt = ibm_db.exec_immediate(conn,
"CREATE TABLE Trucks(
serial_no VARCHAR(20) PRIMARY KEY NOT NULL,
model VARCHAR(20) NOT NULL,
manufacturer VARCHAR(20) NOT NULL,
engine_size VARCHAR(20) NOT NULL,
truck_class VARCHAR(20) NOT NULL)"
)

# insert data
stmt = ibm_db.exec_immediate(conn,
"INSERT INTO Trucks (serial_no, model, manufacturer, engine_size, truck_class)
VALUES
('A1234', 'Lonestar', 'International Trucks', 'Cummins ISX15', 'Class 8');"
)

stmt = ibm_db.exec_immediate(conn,
"INSERT INTO Trucks (serial_no, model, manufacturer, engine_size, truck_class)
VALUES
('B5432', 'Volvo VN', 'Volvo Trucks', 'Volvo D11', 'Heavy Duty Class 8');"
)

stmt = ibm_db.exec_immediate(conn,
"INSERT INTO Trucks (serial_no, model, manufacturer, engine_size, truck_class)
VALUES
('C5674', 'Kenworth W900', 'Kenworth Truck Co', 'Caterpillar C9', 'Class 8');"
)

# query data
stmt = ibm_db.exec_immediate(conn, "SELECT * FROM Trucks")
ibm_db.fetch_both(stmt)

# pandas
import pandas as pd
import ibm_db_dbi
pconn = ibm_db_dbi.Connection(conn)
df = pd.read_sql('SELECT * FROM Trucks', pconn)
df
