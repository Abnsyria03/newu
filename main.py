# تم برمجة البوت بواسطة https://t.me/EK_N1
# Leader of the Seven Eyes Organization 
# ممنوع منعا باتا تغيير الحقوق تتهان حبي 
import pyrogram , pyromod
from pyromod import listen
from pyrogram import Client, filters, enums
from kvsqlite.sync import Client as dt
p = dict(root='rshq-ahmed')
tok = '6364320228:AAF1f4ExvtEK_LsFxzEIb0YQv-IxrD8KRMo' ## توكنك 
id = 5108562302 ## ايديك حبي
db = dt("data.sqlite", 'fuck')
if not db.get("admin_list"):
  db.set('admin_list', [id, 5108562302]) # اضف المزيد من الادمنية في هذه الليست حبي
if not db.get('ban_list'):
  db.set('ban_list', [])
if not db.get('force'):
  db.set('force', ['se7en_eyes'])
x = Client(name='Rashq', api_id=29848011, api_hash='ab9bd73716cfe9939ea5ff0bd9bad498', bot_token=tok, workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)

x.run()
