from googletrans import Translator
from core.mapper import map
import datetime


class TextHelper:
    def __init__(self):
        self.translator = Translator()
        

    def print_time():
        parser = datetime.datetime.now() 
        return parser.strftime("%d-%m-%Y %H:%M:%S")

    def translate(self, text, src_lang, dst_lang):
        if(src_lang == 'zh'):
            src_lang = 'zh-CN'
        output = self.translator.translate(
            text, src=src_lang, dest=map(dst_lang))
        self.file = open("translate_output.txt", "w")
        self.file.write(output.text)
        self.file.close()