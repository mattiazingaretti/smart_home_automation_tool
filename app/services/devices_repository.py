import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
from models.DeviceState import DeviceState
from models.DeviceType import DeviceType

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")  
DB_PORT = os.getenv("DB_PORT", "5432")  

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )


#TODO: [NTH] It would be nice to separate and modularize the CRUD operations for each device type into their own files.

def fetch_devices_state(verbose=False) -> list[DeviceState]:
    connection = None  

    try:
        connection = get_connection()
        cursor = connection.cursor()
        toRet = []
        tables = { "thermostat_device": DeviceType.THERMOSTAT, "fan_device": DeviceType.FAN, "light_device": DeviceType.LIGHT}
        for table, deviceType in tables.items():
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table))
            cursor.execute(query)
            devices = cursor.fetchall()

            for device in devices:
                toRet.append(DeviceState(device[0], device[1], deviceType))
                
            if verbose:
                print(f"Devices in table '{table}':")
                for device in devices:
                    print(device)
        return toRet
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def create_light(name: str, value: str):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO light_device (name, value) VALUES (%s, %s)"
        cursor.execute(query, (name, value))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def read_light(name: str) -> DeviceState:
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM light_device WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        if result:
            return DeviceState(result[0], result[1], DeviceType.LIGHT)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def update_light(name: str, value: str):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE light_device SET value = %s WHERE name = %s"
        cursor.execute(query, (value, name))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def delete_light(name: str):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM light_device WHERE name = %s"
        cursor.execute(query, (name,))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def create_fan(name: str, value: str):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO fan_device (name, value) VALUES (%s, %s)"
        cursor.execute(query, (name, value))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def read_fan(name: str) -> DeviceState:
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM fan_device WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        if result:
            return DeviceState(result[0], result[1], DeviceType.FAN)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def update_fan(name: str, value: str):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE fan_device SET value = %s WHERE name = %s"
        cursor.execute(query, (value, name))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def delete_fan(name: str):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM fan_device WHERE name = %s"
        cursor.execute(query, (name,))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# CRUD methods for thermostat_device
def create_thermostat(name: str, value: int):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO thermostat_device (name, value) VALUES (%s, %s)"
        cursor.execute(query, (name, value))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def read_thermostat(name: str) -> DeviceState:
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM thermostat_device WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        if result:
            return DeviceState(result[0], result[1], DeviceType.THERMOSTAT)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def update_thermostat(name: str, value: int):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE thermostat_device SET value = %s WHERE name = %s"
        cursor.execute(query, (value, name))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def delete_thermostat(name: str):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM thermostat_device WHERE name = %s"
        cursor.execute(query, (name,))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()