import logging

try:
    from systemd.journal import JournalHandler

    journalEnabled = True
except:
    journalEnabled = False

if journalEnabled:
    logger = logging.getLogger('waifu_logger')
    logger.addHandler(JournalHandler())
    logger.setLevel(logging.DEBUG)
    logger.info('logger enabled')


def log(*messages):
    message = ''
    for m in messages:
        message += str(m)
    print(message)
    if journalEnabled:
        logger.info(message)
