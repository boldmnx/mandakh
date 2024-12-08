import hashlib

hash256 = hashlib.sha256()
hash256.update('some'.encode('utf-8'))
hashPass = hash256.hexdigest()
print( hashPass)


# image = secure_filename(zurag.filename)
#                 oldImage = image.split('.')
#                 oldImage[0] = scode
#                 newImage = '.'.join(oldImage)
#                 imagePath = os.path.join(app.config['image_root'], newImage)
#                 zurag.save(imagePath)
#             else:
#                 imagePath = ''
#             oyutan_ob.add(scode=scode, sovog=sovog,         simage=imagePath,              sner=sner,
#                           gender=gender, elssen=elssen, tcode=tcode, mcode=mcode, register=register)
#             retu