import sqlalchemy
metadata = sqlalchemy.MetaData()



light_device = sqlalchemy.Table(
    "light_device",
    metadata,
    sqlalchemy.Column("name", sqlalchemy.String(255), primary_key=True),
    sqlalchemy.Column("value", sqlalchemy.String(3),
        sqlalchemy.CheckConstraint("value IN ('ON', 'OFF')")
    ),
)

fan_device = sqlalchemy.Table(
    "fan_device",
    metadata,
    sqlalchemy.Column("name", sqlalchemy.String(255), primary_key=True),
    sqlalchemy.Column("value", sqlalchemy.String(6),
        sqlalchemy.CheckConstraint("value IN ('OFF', 'LOW', 'MEDIUM', 'HIGH')")
    ),
)

thermostat_device = sqlalchemy.Table(
    "thermostat_device",
    metadata,
    sqlalchemy.Column("name", sqlalchemy.String(255), primary_key=True),
    sqlalchemy.Column("value", sqlalchemy.Integer,
        sqlalchemy.CheckConstraint("value BETWEEN 18 AND 30")
    ),
)
