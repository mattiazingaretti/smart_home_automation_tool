
CREATE TABLE light_device (
    name VARCHAR(255) PRIMARY KEY,
    value VARCHAR(3) CHECK (value IN ('ON', 'OFF'))
);

CREATE TABLE fan_device (
    name VARCHAR(255) PRIMARY KEY,
    value VARCHAR(6) CHECK (value IN ('OFF', 'LOW', 'MEDIUM', 'HIGH'))
);

CREATE TABLE thermostat_device (
    name VARCHAR(255) PRIMARY KEY,
    value INTEGER CHECK (value BETWEEN 18 AND 30)
);