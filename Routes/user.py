from Model.user import User
from Config.db import conn


class UserRoutes:
    @staticmethod
    async def get_all():
        return await conn.prisma.user.find_many()

    @staticmethod
    async def create(user: User):
        return await conn.prisma.user.create({
            "dni": user.dni,
            "name": user.name,
            "email": user.email,
            "password": user.password
        })

    @staticmethod
    async def get_by_dni(user_dni: str):
        return await conn.prisma.user.find_first_or_raise(where={"dni": user_dni})

    @staticmethod
    async def delete(user_dni: str):
        return await conn.prisma.user.delete(where={"dni": user_dni})

    @staticmethod
    async def update(user: User, user_dni: str):
        return await conn.prisma.user.update(data={
            "dni": user.dni,
            "name": user.name,
            "email": user.email,
            "password": user.password
        },
            where={"dni": user_dni})
