import bpy
import sys
import os

#bpy.ops.mesh.primitive_cone_add(radius1=1, radius2=0, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 1))
bpy.ops.mesh.primitive_plane_add(size=50, enter_editmode=False, align='WORLD', location=(0, 0, 0))

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Cube'].select_set(True) # Blender 2.8x
bpy.ops.object.delete()

for obj in bpy.context.selected_objects:
    obj.select_set(False)

argv = sys.argv
argv = argv[argv.index("--") + 2:]

lgi = sys.argv


current = os.getcwd()
email_name = str(sys.argv[5])
print(" And the fourth argument is " + email_name)
for i, eachArg in enumerate(argv):
    print('System arguments {}:'.format(i), eachArg)
    try:
        file_loc = current + '/models/' + str(eachArg).lower() +'.obj'
        imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
        obj_object = bpy.context.selected_objects[0]  ####<--Fix
        print('Imported name: ', obj_object.name)
        #for entry in eachArg:
            #print(entry)
        print(eachArg)
    except:
        print("========================================= Nothing found on this object!! ==========================")

try:
    bpy.data.objects["female_Mesh"].location = (-1.2, -0.3, 0)
except:
    print("No female mesh found")
bpy.data.objects["Camera"].location = (-0.14723,-7.0114,4.5669)
bpy.data.objects["Camera"].rotation_euler = ( 1,0,0 )
bpy.ops.object.select_all(action='DESELECT')


#bpy.ops.wm.save_as_mainfile(filepath="myfilename.blend")
scene = bpy.context.scene
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = os.path.join(current,"image.png")


for scene in bpy.data.scenes:
  scene.render.resolution_x = 480
  scene.render.resolution_y = 480


r = bpy.ops.render
r.render(write_still = 1)



import smtplib
import imghdr
from email.message import EmailMessage

from email.utils import make_msgid

os.environ['EMAIL_USER'] = 'servblend'
os.environ['EMAIL_PASS'] = 'zpupujucqylehanm'
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['artursahak99@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Check out your result!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = email_name

msg.set_content('View the render of the image you uploaded')
asparagus_cid = make_msgid()

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an email from Artur Sahakyan's and Vadim's software!</h1>
    </body>
</html>
""", subtype='html')

print("current working directory is +==================================" + os.getcwd())

with open(os.path.join(current,"image.png"), 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'png',cid=asparagus_cid)
    #msg.add_attachment(img.read(), maintype='image',subtype=imghdr.what(None, img.read()))



#img_data = f"image.png"

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

