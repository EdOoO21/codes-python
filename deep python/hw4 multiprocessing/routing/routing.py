from typing import List
import threading
import time

class Request:
    def __init__(self, client_id: str, request_id: str, processing_time: float):
        self.client_id = client_id
        self.request_id = request_id
        self.processing_time = processing_time


class Server:
    """
    Represents a server that can process requests.
    """

    def __init__(self, server_id: str, performance_score: int):
        self.server_id = server_id
        self.performance_score = performance_score
        self.alive = True
        self.processed : set[str] = set()
        self.semaphore = threading.Semaphore(1)
        self.now = 0

    def process_request(self, request: Request) -> None:
        """
        Processes a request. Save the request client_id and request_id.
        """
        self.semaphore.acquire()
        self.now += 1
        if not self.is_processed(request.request_id):
            time.sleep(request.processing_time)
            self.processed.add(request.request_id)
        self.now -= 1
        self.semaphore.release()



    def is_alive(self) -> bool:
        """
        Checks if the server is alive.
        """
        return self.alive

    def crash(self) -> None:
        """
        Crashes the server.
        """
        self.alive = False
        return None

    def recover(self) -> None:
        """
        Recovers the server.
        """
        self.alive = True
        return None

    def is_processed(self, request_id: str) -> bool:
        """
        Checks if the request is processed. Emulates caching.
        """
        return request_id in self.processed

    def is_overloaded(self, max_load: int) -> bool:
        return self.now >= max_load




class Router:
    """
    Represents a router that can route requests to servers.
    """
    def __init__(self, servers: List[Server], max_load: int):
        self.servers = servers
        self.max_load = max_load
        self.semaphore = threading.Semaphore(max_load)
        self.client_server_map : dict[str, Server] = {}
        self.total_weight = sum([server.performance_score for server in servers])
        self.current_index = -1
        self.current_weights = [0 for _ in range(len(servers))]



    def route(self, request: Request) -> None:

        if request.client_id in self.client_server_map.keys():
            server1 = self.client_server_map[request.client_id]
            if server1.is_alive() and (not server1.is_overloaded(self.max_load)):
                self.semaphore.acquire()
                server1.process_request(request)
                self.semaphore.release()
                return None


        while True:
            max_weight_server = None
            max_weight_index = 0

            for i, server2 in enumerate(self.servers):
                if server2.is_alive() and (not server2.is_overloaded(self.max_load)):
                    self.current_weights[i] += server2.performance_score
                    if (max_weight_server is None) or (self.current_weights[i] > self.current_weights[max_weight_index]):
                        max_weight_server = server2
                        max_weight_index = i

            if max_weight_server is not None:
                self.current_weights[max_weight_index] -= self.total_weight

            server : Server | None = max_weight_server

            if server:
                self.client_server_map[request.client_id] = server
                self.semaphore.acquire()
                server.process_request(request)
                self.semaphore.release()
                return None



    def add_server(self, server: Server) -> None:
        self.servers.append(server)
        self.current_weights.append(0)
        self.total_weight += server.performance_score
        return None

    def remove_server(self, server: Server) -> None:
        self.current_weights.pop(self.servers.index(server))
        self.servers.remove(server)
        self.total_weight -= server.performance_score
        return None
