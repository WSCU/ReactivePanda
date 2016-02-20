from PandaSRC.Panda import *
# You can add more photos to your nametag by placing some geometric solids in your animation

# You can put an arbitrary number of photos in a wheel, 6 photos on a cube, or 4 on a tetrahedron

a = cube("Luna.jpg", "Crawling.jpg", "Everett.jpg" , "Hilary_Mayes.jpg", "Rob_Fillmore.jpg", "Rafting.jpg")

a.hpr = hpr(time*-6, sin(time), 0)
b = blastPicture("Crawling.jpg",5,5)
for f in b:
    f.position = itime(at(p3(2,1,3))+to(1,p3(randomRange(-3,7),randomRange(1,2),randomRange(-7,7)))+to(pi,f.location+p3(2,0,0)))
c = blastPicture("Rob_Fillmore.jpg",5,5)
for f in c:
    f.position = itime(at(p3(-4,1,3))+to(pi,p3(randomRange(-3,7),randomRange(1,2),randomRange(-7,7)))+to(pi,f.location+p3(-2,0,0)))
d = blastPicture("Hilary_Mayes.jpg",5,5)
for f in d:
    f.position = itime(at(p3(2,1,-4))+to(2,p3(randomRange(-3,7),randomRange(1,2),randomRange(-7,7)))+to(pi,f.location+p3(0,0,2)))
fire(position=p3( -2,0,-1),texture="fire.png",size=.4*step(time-7.5))
sphere(position=p3(0,0,0),texture="bricks", size=-30)
#cube(t1, t2, t3, t4, t5, t6)



#tetra(t1, t2, t3, t4)



start()
