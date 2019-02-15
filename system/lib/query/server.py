from .pinger import ServerPinger
from .protocol.connection import TCPSocketConnection, UDPSocketConnection
from .querier import ServerQuerier


class Query:
    def __init__(self, host, port=25565):
        self.host = host
        self.port = port

    @staticmethod
    def lookup(address):
        host = address
        port = None
        if ":" in address:
            parts = address.split(":")
            if len(parts) > 2:
                raise ValueError("Invalid address '%s'" % address)
            host = parts[0]
            port = int(parts[1])
        if port is None:
            port = 25565

        return Query(host, port)

    def ping(self, retries=3, **kwargs):
        connection = TCPSocketConnection((self.host, self.port))
        exception = None
        for attempt in range(retries):
            try:
                pinger = ServerPinger(connection, host=self.host, port=self.port, **kwargs)
                pinger.handshake()
                return pinger.test_ping()
            except Exception as e:
                exception = e
        else:
            raise exception

    def status(self, retries=3, **kwargs):
        connection = TCPSocketConnection((self.host, self.port))
        exception = None
        for attempt in range(retries):
            try:
                pinger = ServerPinger(connection, host=self.host, port=self.port, **kwargs)
                pinger.handshake()
                result = pinger.read_status()
                result.latency = pinger.test_ping()
                return result
            except Exception as e:
                exception = e
        else:
            raise exception

    def query(self, retries=3):
        exception = None
        host = self.host
        print(host, self.port)
        for attempt in range(retries):
            try:
                connection = UDPSocketConnection((host, self.port))
                querier = ServerQuerier(connection)
                querier.handshake()
                print(querier)
                return querier.read_query()
            except Exception as e:
                exception = e
        else:
            raise exception
