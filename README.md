# hopotti
Höpötti-botti

A discord bot that uses OpenAI's GPT-3 model "text-davinci-003" to answer questions.

The bot is setup to run on Heroku or locally.

All the commands takes arguments which gets passed on as a prompt to the language model.
| Command | Description |
|:-----|-----------|
|!ask args       |Prompts the model to answer the question in args to in a bit of a weird manner.|
|!ask-really args|Prompts the model to answer the question in args in a haiku format.|
|!story args     |Prompts the model to write a story about args.|

Example queries for höpötti-bot:

<picture>
 <img alt="!ask-really" src="https://github.com/Niosni/hopotti/blob/master/images/haiku.png">
</picture>

<picture>
 <img alt="!ask" src="https://github.com/Niosni/hopotti/blob/master/images/weird.png">
</picture>
