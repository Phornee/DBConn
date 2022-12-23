from .db_conn import DBConn, DBOpenException, DBGetLockException, DBReleaseLockException
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDBConn(DBConn):
    db_tables = None

    def __init__(self):
        super().__init__()

    def openConn(self, params, autocommit=True):
        db_tables = {}    # Nothing to do here but creating the tables dictionaty

    def closeConn(self):
        pass   # Nothing to do here

    def insert(self, table, rows):


 [
                    {
                        "measurement": "piwaterflow",
                        "tags": {
                            "action": action,
                            "forced": forced
                        },
                        "time": datetime.utcnow(),
                        "fields": {
                            "fake": 0
                        }
                    }
                ]

        write_api = self.conn.write_api(write_options=SYNCHRONOUS)

        point = Point(table)\
                .tag("host", "host1")\
                .field("used_percent", 23.43234543)\
                .time(datetime.utcnow(), WritePrecision.NS)

        write_api.write(self.bucket, self.org, point)

    def getLock(self, lockname):
        raise

    def releaseLock(self, lockname):
        raise

