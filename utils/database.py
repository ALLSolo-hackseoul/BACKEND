import os
import motor.motor_asyncio


class MEMBER:
    def __init__(self):
        self.database = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))["hackseoul24"]
        self.collection = self.database["member"]

    async def get(self, userid: str = None, name: str = None, email: str = None):
        if userid:
            return await self.collection.find_one({"userid": userid})
        elif name:
            return await self.collection.find_one({"name": name})
        elif email:
            return await self.collection.find_one({"email": email})

    async def register(self, userid: str, name: str, phone: str, email: str, password: str, address: str, country: str):
        return await self.collection.insert_one(
            {"userid": userid, "name": name, "phone": phone, "email": email, "password": password, "address": address,
             "country": country})

    async def update(self, userid: str, name: str, phone: str, email: str, password: str, address: str, country: str):
        return await self.collection.update_one({"userid": userid}, {
            "$set": {"name": name, "phone": phone, "email": email, "password": password, "address": address,
                     "country": country}})

    async def delete(self, userid: str):
        return await self.collection.delete_one({"userid": userid})
