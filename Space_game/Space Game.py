


from ursina import *                    # Import the ursina engine
from ursina import time
from ursina import application
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from ursina import camera

class Astro(Entity):
	def __init__(self, position = (0,0,0)):
		super().__init__(
            position = position,
			model='astro1',collider='astro1',texture='rockytex' ,scale=(1,1,1),)


app = Ursina()                          # Initialise your Ursina app


window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter


#Entity(model='cube',scale=(.1,.1,.1),color=color.black).add_script(SmoothFollow(target=player, offset=[0,0,0], speed=4))
Sky(texture='starsky')
player = Entity(model='fighter',texture='fighter',scale=(1,1,1),rotation=(0,180,0),collider='box')
#player.collider = 'mesh'     # add MeshCollider based on entity's bounds.
#player.collider = MeshCollider(player, mesh=player.model, center=(0,0,0))
#player.collider.setScale(.9,2,1)
#player.collider.visible = True

#astro = Entity(model='astro1',collider='astro1',texture='rockytex' ,scale=(1,1,1),rotation=(0,0,0),position=(0,4,0))
#ground1 = Entity(model='cube',colider='cube',scale=(14,1,1),color=color.white,position = (0,-5,0))


#(x,z,y)

poslist = [5,10,15,20,25]
astro = Entity(model='astro1',collider='box',texture='tex/rockytex' ,scale=(.5,.5,.5),rotation=(0,0,0),position=(random.randint(-6, 6),random.randint(-6, 6),poslist[0]))
astro2 = Entity(model='astro1',collider='box',texture='tex/rockytex' ,scale=(.5,.5,.5),rotation=(0,0,0),position=(random.randint(-6, 6),random.randint(-6, 6),poslist[1]))
astro3 = Entity(model='astro1',collider='box',texture='tex/rockytex' ,scale=(.5,.5,.5),rotation=(0,0,0),position=(random.randint(-6, 6),random.randint(-6, 6),poslist[2]))
astro4 = Entity(model='astro1',collider='box',texture='tex/rockytex' ,scale=(.5,.5,.5),rotation=(0,0,0),position=(random.randint(-6, 6),random.randint(-6, 6),poslist[3]))
astro5 = Entity(model='astro1',collider='box',texture='tex/rockytex' ,scale=(.5,.5,.5),rotation=(0,0,0),position=(random.randint(-6, 6),random.randint(-6, 6),poslist[4]))
menu = Text("Press 1 to quit, Press 2 to Restart", y=.5,x=-.25)


alive = True



def input(key):
    if held_keys['space']:
        #print(player.x)
        #print(player.y)
        print(player.rotation_x)
    if held_keys['1']:
        quit()
    if held_keys['2']:
        player.visible = True
        player.setPos(0, 0, 0)
        player.collider.setScale(1)
        global alive
        alive = True




def update():
    vel = 3
    maxturn = 15
    player.rotation_x = 0
    player.rotation_z = 0
    if held_keys['w']:
        player.y += vel * time.dt
        player.rotation_x = maxturn
    if held_keys['s']:
        player.y += -vel * time.dt
        player.rotation_x = -maxturn
    if held_keys['d']:
        player.x += vel * time.dt
        player.rotation_z = -maxturn
    if held_keys['a']:
        player.x += -vel * time.dt
        player.rotation_z = maxturn
    while player.y >= 6:
        player.y -= 1
    while player.y <= -6:
        player.y += 1
    while player.x >= 6:
        player.x -= 1
    while player.x <= -6:
        player.x += 1

    astro.z -= vel * time.dt
    astro.rotation_x -= 5
    endpos = 25
    if astro.z <= -2:
        astro.setPos(random.randint(-6, 6), random.randint(-6, 6), endpos)
    astro2.z -= vel * time.dt
    astro2.rotation_x -= 5
    if astro2.z <= -2:
        astro2.setPos(random.randint(-6, 6), random.randint(-6, 6), endpos)
    astro3.z -= vel * time.dt
    astro3.rotation_x -= 5
    if astro3.z <= -2:
        astro3.setPos(random.randint(-6, 6), random.randint(-6, 6), endpos)
    astro4.z -= vel * time.dt
    astro4.rotation_x -= 5
    if astro4.z <= -2:
        astro4.setPos(random.randint(-6, 6), random.randint(-6, 6), endpos)
    astro5.z -= vel * time.dt
    astro5.rotation_x -= 5
    if astro5.z <= -2:
        astro5.setPos(random.randint(-6, 6), random.randint(-6, 6), endpos)



    hit_info = player.intersects()
    if hit_info.hit:
        #hit_info.entity.visible = False
        global alive
        while alive == True:
            print("collision detected")
            #hit_info.world_point
            player.visible = False
            player.collider.setScale(0)
            explo = Entity(model='sphere', scale=1, texture='explosiontex',position=hit_info.world_point)
            explo.animate_scale(3, .3)
            destroy(explo, delay=.3)
            alive = False




        #destroy(player,delay=0)
        #Entity(model='sphere', position=hit_info.world_point, scale=1.5, texture='explosiontex',add_to_scene_entities=False)










#player = PlatformerController2d()


app.run()
