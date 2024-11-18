# Описание проекта

  ### Многофункциональный телеграм-бот

  Данный бот сейчас умеет принимать и обрабатывать изображения.
  
  На команду: /Random_Joke отправляет случайную шутку пользователю.
  
  На команду: /Random_Compliment отправляет случайный комплимент пользователю.
  
  На команду: /Flip_a_Coin отправляет результат подбрасывания монеты пользователю.
  
# Возможности телеграм-бота:

### 1. Реагирует на команды /start и /help, отправляя приветственное сообщение.

   ![1](https://github.com/user-attachments/assets/d8439d57-b4dd-43ce-90fc-93498009c26c)

### 2.1. Реагирует на команду /Random_Joke, отправляя случайную шутку пользователю.

  ![2 1](https://github.com/user-attachments/assets/b9f69b87-089d-4342-803d-bccf7bcfc9d7)

### 2.2. Реагирует на команду /Random_Compliment, отправляя случайный комплимент пользователю.

  ![2 2](https://github.com/user-attachments/assets/880e4595-5f74-4a72-8277-91577aa9aa47)

### 2.3. Реагирует на команду /Flip_a_Coin, отправляя пользователю результат подбрасывания монеты.

  ![2 3](https://github.com/user-attachments/assets/f6357e2f-f495-4085-a56b-297a331f7f70)

### 2.4. Реагирует на изображения, отправляемые пользователем, и предлагает варианты обработки:

   ![2](https://github.com/user-attachments/assets/1777aa91-99ea-4043-9f47-f360987457bc)

### 2.4.1. Пикселизировать изображения.

  ![3](https://github.com/user-attachments/assets/edc102af-b662-4c6d-9f4e-21bb229f6023)

### 2.4.2. Преобразовывать изображения в ASCII-арт.

  ![4](https://github.com/user-attachments/assets/e8c37fb3-9181-4567-8a3b-728c26335005)

### 2.4.3. Инвертировать изображение.

  ![5](https://github.com/user-attachments/assets/663fff45-d33d-425e-a3a1-8106d8df5a70)

### 2.4.4. Создает отраженную копию изображения.

  #### По горизонтали:

  ![6](https://github.com/user-attachments/assets/9d4b3b59-6219-49a7-bd0a-6fd3a71f9d14)

  #### По вертикали:

  ![7](https://github.com/user-attachments/assets/d8230c6b-7d21-4093-b1ea-2bd8eb634b3b)

### 2.4.5. Преобразовать изображение в тепловую карту (от синего (холодные области) до красного (теплые области)).

  ![8](https://github.com/user-attachments/assets/c9a9fc34-0623-4dcf-831a-dbaf2141eb43)

### 2.4.6. Адаптирует размер изображения для использования в качестве стикера в Telegram.

  ![9](https://github.com/user-attachments/assets/9912131f-006a-4566-a0e4-5d72bced356a)

# Как запустить
  
  1. Склонируйтке проект и перейдите в директорию проекта. Убедитесь, что у вас установлен Python версии 3.6 или выше.
  2. Установите необходимые библиотеки выполнив следующую команду: pip install -r requirements.txt.
  3. Запустите код с помощью данной команды: python main.py
  4. Телграмм бот запущен

# Библиотеки

1. Telebot - это синхронная и асинхронная реализация Telegram Bot API.
2. Pillow (PIL) - библиотека для обработки изображений.
