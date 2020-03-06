"""
Text templates for bot responses.
"""

new_talk = (
    '🎉 У нас новый докладчик или докладчица: {speaker_name} хочет сделать доклад "{talk_name}" ({talk_dates}).'
    " Notion: {notion_url}"
)

typeform_invalid = (
    "❌ В Typeform пришла заявка, но форма неправильная, и у неё отвалилась жопа."
    " Нужно заглянуть в логи вебхук-сервиса."
)

notion_error = (
    "❌ В Typeform пришла заявка, но произошла ошибка при добавлении в Notion."
    " Нужно заглянуть в логи вебхук-сервиса."
)
