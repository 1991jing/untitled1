import os
import yaml
from logbook import Logger, TimedRotatingFileHandler

TimedRotatingFileHandler(f'log/{os.path.basename(__file__).rstrip(".py")}.log', date_format='%Y-%m-%d',
                         rollover_format='{basename}_{timestamp}{ext}', backup_count=10).push_application()



# 将字典写入到yaml
desired_caps = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "debug_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "D://v7app_auto//untitled1//v7jxc_auto//log//debug.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "D://v7app_auto//untitled1//v7jxc_auto//log//info.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "simple",
            "filename": "D://v7app_auto//untitled1//v7jxc_auto//log//errors.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },
    "loggers": {
        "my_module": {
            "level": "DEBUG",
            "handlers": [
                "debug_file_handler"
            ],
            "propagate": "no"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": [
            "console",
            "info_file_handler",
            "error_file_handler"
        ]
    }
}

# curpath = os.path.dirname(os.path.realpath(__file__))
# print(curpath)
# yamlpath = os.path.join(curpath, "../log/logconfig")
yamlpath = "../data/logconfig"

# 写入到yaml文件
with open(yamlpath, "w", encoding="utf-8") as f:
    yaml.dump(desired_caps, f)