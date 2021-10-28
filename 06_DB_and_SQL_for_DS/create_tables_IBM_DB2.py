stmt = ibm_db.exec_immediate(conn,
'CREATE TABLE Trucks(
serial_no VARCHAR(20) PRIMARY KEY NOT NULL,
model VARCHAR(20) NOT NULL,
manufacturer VARCHAR(20) NOT NULL,
engine_size VARCHAR(20) NOT NULL,
truck_class VARCHAR(20) NOT NULL)'
)
