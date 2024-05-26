from prisma import Prisma


class PrismaConnection():
    def __init__(self):
        self.prisma = Prisma()

    async def connect(self):
        self.prisma.connect()

    async def disconnect(self):
        self.prisma.disconnect()


conn = PrismaConnection()