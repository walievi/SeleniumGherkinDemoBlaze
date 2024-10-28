from browser import get_browser

def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()

def before_scenario(context, scenario):
    context.driver = get_browser()

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()