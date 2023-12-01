
allowExt = set(['png', 'jpg', 'jpeg'])


def allowed_file(e):
    return '.' in e and e.split('.')[1].lower() in allowExt
