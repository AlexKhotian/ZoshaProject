__author__ = 'Alex'

'''
Created on Jul 16, 2015

@author: Alex Khotian
'''

import socket


class BoardReceiver(object):
    def __init__(self):
        pass
    m_socket = 0

    def createreceiversocket(self, ip_address, port):
        m_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        m_socket.bind((ip_address, port))
        m_socket.setblocking(0)
