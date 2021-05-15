# djangologin


git remote add origin https://github.com/restuie/djangologin.git
git push -u origin master


https://www.itread01.com/content/1559200023.html
https://www.cnblogs.com/wj-1314/p/10065929.html
https://www.learncodewithmike.com/2020/04/django-authentication-and-usercreationform.html


# models.Model 中常用的資料欄位格式
BigIntegerField| |64位元之大整數

BooleanField| |布林值，只有 True/False 兩種 CharField max_length：指定可接受之字串長度 用來儲存較短資料的字串，通常使用 於單行的文字資料 

DateField|auto_now：每次物件被儲存時即自動加入目前日期auto_now_add：只有在物件被建立時才加入目前日期|日期格式，可用於 datetime.date

DateTimeField|同上|日期時間格式，對應到datetime.datetime 

DecimalField|max_digits：可接受的最大位數 decimal_places：在所有的位數中，小數佔幾個位數|定點小數數值資料，適用於 Python的 Decimal模組之實例

EmailField|max_length：最長字數|可接受電子郵件位址格式之欄位 

FloatField| |浮點數欄位 

IntegerField| |整數欄位，是通用性最高的整數格式 

PostiveIntegerField| |正整數欄位

SlugField|max_length：最大字元長度|和CharField 是一樣的，通常用來當做是網址的一部份

TextField| |長文字格式，一般是用在 HTML 表單 中的 Textarea 輸入項目

URLField|max_length：最大字元長度|和CharField是一樣的，特別用來記 錄完整的 URL 網址

# models.Model各欄位常用的屬性說明
null|此欄位是否接受儲存空值 NULL，預設值是 False

blank|此欄位是否接受儲存空白內容，預設值是False

choices|以選項的方式（只有固定內容的資料可以選用）當做是此欄位的侯選值

default|輸入此欄位的預設值

help_text|欄位的求助訊息

primary_key|把此欄位設定為資料表中的主鍵KEY，預設值為False

unique|設定此欄位是否為唯一值，預設值為False

