import logging

def before_all(context):
    context.config.setup_logging(filename = context.config.userdata.get('logging_file'))
    logging.info('before_all')

def after_all(context):
    logging.info('after_all')

def before_feature(context, feature):
    logging.info('before_feature:' + feature.name)

def after_feature(context, feature):
    logging.info('after_feature:' + feature.name)

def before_scenario(context, scenario):
    logging.info('before_scenario:' + scenario.name)

def after_scenario(context, scenario):
    logging.info('after_scenario:' + scenario.name)

def before_step(context, step):
    logging.info('before_step:' + step.name)

def after_step(context, step):
    logging.info('after_step:' + step.name)

def before_tag(context, tag):
    logging.info('before_tag:' + tag)

def after_tag(context, tag):
    logging.info('after_tag:' + tag)
