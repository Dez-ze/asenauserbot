from pyrogram import Client, filters
from pyrogram.types import Message

api_id = 11488967
api_hash = "70cbee6229fede935d9ccf1dddf3aad9"

Client = Client("Dezin", api_id=api_id, api_hash=api_hash)

userlist = []

@Client.on_message(filters.command("yaz", prefixes=".") & filters.me)
async def example(client: Client, message: Message):
  await message.delete()
  async for x in Client.get_chat_members(message.chat.id):
    # await Client.send_message(x.user.id , "Test123")
    userlist.append(x.user.id)


Client.run()
