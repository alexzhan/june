#: site configuration
sitename = "June"
siteurl = ''
cookie_secret = 'secret'


#: sqlalchemy database
sqlalchemy_engine = "sqlite:///june.sqlite"
sqlalchemy_kwargs = {"echo": True}


#: third party support
recaptcha_key = '6Le9jtESAAAAAGBuFoL451V-0Vt-_xiNA8ACQiTd'
recaptcha_secret = '6Le9jtESAAAAAO2f24yTcAEnrnzUv35B1ofONIlR'

google_custom_search = "017842580319746762888:veoakwnpkqq"

emoji_url = 'http://python-china.b0.upaiyun.com/emojis/'

image_backend = 'june.front.backends.LocalBackend'
local_static_path = '/tmp/'
local_static_url = 'http://path.to.com/'
