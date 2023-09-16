from aiogram import Router
from aiogram.types import Message

router: Router = Router()

# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота


@router.message()
async def send_other_message(message: Message):
    await message.answer('Это сообщени не предусмотрено логикой работы бота'
                         '\n\n Нажмите /help')
