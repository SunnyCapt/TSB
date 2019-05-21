TSB 
=========
Telegram Bot to search for the author/book (from a given list) by quote.

FИCK/FAQ/А_КАК
-------------
* -С чего начать?
        <br> Написать [@BotFather](https://telegram.me/BotFather)
        
        git clone https://github.com/SunnyCapt/TSB.git
    Прописать токен бота в data.py
* -Как запустить?
    * На своем компе:
         <br> Придется искать надежный прокси и прописать его в \_\_main__.py 
         в конце, где закомментированная строка
          
            python3 bot
    * На серваке:
        
        Установить heroku cli, а потом:
           
            ./build.sh
            
* -Как добавить книгу/автора?
<br>Изменить словарь books, что находится в data.py
* -А поподробнее? 
   <br>из директории где лежит папка bot:
        
        $python3
        >>> from bot import data
        >>> clean_text = data.clear("smth dirty text")
        >>> print(clean_text)
        
   дальше либо добавляете в books "Имя автора": {"Имя книги": clean_text}, 
   либо, если автор уже есть там, вписываем рядом с другими его текстами
   через запятую "Имя книги": clean_text          
            




---
Tg: [@SunnyCapt](https://telegram.me/SunnyCapt)

Email: sunny.capt@tuta.io 

