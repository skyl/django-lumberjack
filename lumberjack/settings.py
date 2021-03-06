from django.conf import settings

LOGGING = {
    'formatters': {
        'error':{
            '()':'lumberjack.formatters.tb.TracebackFormatter',
            'output':'terminal',
            },
        'sql' : {
            '()':'lumberjack.formatters.sql.SQLFormatter',
            'format':'[%(name)s] %(levelname)s (%(duration)sms) %(message)s',
            'output':'terminal',
        },
        'ajax' : {
            '()':'lumberjack.formatters.ajax.AjaxFormatter',
            'format':'[%(name)s] %(levelname)s %(message)s',
            'output':'terminal',
        },
        'default' : {
            'format' : '[%(name)s] %(levelname)s %(message)s',
        },
    },
    'handlers' : {
        'sqlstream' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'sql',
        },
        'errorstream' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'error',
            },
        'ajaxstream' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'ajax',
            },
        'stream' : {
            'class' : 'logging.StreamHandler',
            'formatter' : 'default',
        },
        #'errorarecibo' : {
        #    'class' : 'lumberjack.handlers.AreciboHandler',
        #    'server': 'http://your-arebico-instance.appspot.com/',
        #    'account': 'public_account_password',
        #    },
        # requires python-arecibo lib
    },
    'loggers' : {
        'django.db' : {
            'level' : 'DEBUG',
            'handlers' : ['sqlstream'],
            },
        'django.errors' : {
            'level' : 'DEBUG',
            'handlers' : ['errorstream'],
            },
        'django.ajax' :{
            'level' : 'DEBUG',
            'handlers' : ['ajaxstream'],
            },
        'django.profile' :{
            'level' : 'DEBUG',
            'handlers' : ['stream'],
            },
        'django.cache' :{
            'level' : 'DEBUG',
            'handlers' : ['stream'],
            },
        'django.request' :{
            'level' : 'DEBUG',
            'handlers' : ['stream'],
            },
        },
}

if hasattr(settings, 'LOGGING') and settings.LOGGING:
    LOGGING = getattr(settings, 'LOGGING', LOGGING)
