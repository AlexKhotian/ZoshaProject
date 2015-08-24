__author__ = 'Alex'

import socket


class BoardSender(object):
    def __init__(self):
        pass
    m_socket = 0

    def createsendersocket(self):
        m_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        m_socket.setblocking(0)
