# DeepSeek - работа с API + консольный вариант приложения

## Установка

### Перед работой необходимо зарегестрироваться на [платформе](https://platform.deepseek.com/) и [создать API-ключ](https://platform.deepseek.com/api_keys). 

[Подробнее в статье](https://blog.mihailgok.ru/deepseek-api/)


### DeepSeek использует библиотеку OpenAI поэтому установим ее (+ markdown_pdf чтобы создавать pdf):

```
pip3 install openai
pip3 install markdown_pdf
```

Либо используйте сразу готовый файл связей: 

```
pip3 install -r requirements.txt
```

## Запуск: 

```
python3 main.py
```

Ответы записываются в папку `answers/` в формате MarkDown






