__author__ = 'Alex'

# def imports
import socket
import pickle
# local imports
from BoardNetworking import BoardNetworkingDefinitions


class BoardSender(object):
    def __init__(self):
        pass
    m_socket = 0
    m_protocolType = 0
    m_remoteIP = 0
    m_remotePort = 0

    # move to constructor??
    def createSenderSocket(self, protocolType, remoteIP, remotePort):
        self.m_protocolType = protocolType
        self.m_remoteIP = remoteIP
        self.m_remotePort = remotePort
        self.m_socket = socket.socket(socket.AF_INET, protocolType)
        self.m_socket.setblocking(0)
        if self.m_protocolType == BoardNetworkingDefinitions.ProtocolTypes.TCP:
            self.m_socket.connect((self.m_remoteIP, self.m_remotePort))

    def sendData(self, objectToSend):
        compressData = None
        pickle.dump(objectToSend, compressData)
        if self.m_protocolType == BoardNetworkingDefinitions.ProtocolTypes.TCP:
            self.m_soсket.sendTo(compressData, (self.m_remoteIP, self.m_remotePort))
        elif self.m_protocolType == BoardNetworkingDefinitions.ProtocolTypes.UDP:
            self.m_socket.sendall(compressData)