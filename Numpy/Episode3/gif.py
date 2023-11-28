from PIL import Image

frames = []
#убрал 215 лишних кадров чобы живенько смотрелось 
for frame_number in range(25):  
    frame = Image.open(f'{frame_number}.png')
    frames.append(frame)
 

frames[0].save(
    'Fuck.gif',
    save_all=True,
    append_images=frames,  
    optimize=True,
    duration=100,
    loop=0
)