def before_scenario(context, feature):
    if 'UI' in feature.tags:
        print('This comes first')

def after_scenario(context, feature):
    if 'UI' in feature.tags:
        print('This comes after feature')