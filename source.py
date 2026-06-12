import pygame
import numpy as np
import time
#disclaimer : this button set is ai generated , got bigger fish to fry than designing a button class for 5 hours..
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=pygame.Color('white')):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False
        self.clicked = False

        # Load custom font (font.ttf in your folder)
        try:
            self.font = pygame.font.Font("font.ttf", 24)
        except:
            # Fallback to default font if custom font not found
            self.font = pygame.font.Font(None, 24)
            print("Custom font not found, using default")

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.clicked = True
                return True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False

        return False

    def draw(self, screen):
        """Draw the button on screen"""
        # Choose color based on state
        if self.clicked:
            current_color = self.hover_color  # Darker when clicked
        elif self.is_hovered:
            current_color = self.hover_color  # Darker when hovered
        else:
            current_color = self.color

        # Draw button background with rounded corners
        pygame.draw.rect(screen, current_color, self.rect, border_radius=8)
        pygame.draw.rect(screen, pygame.Color('black'), self.rect, 2, border_radius=8)

        # Render text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        # Draw text
        screen.blit(text_surface, text_rect)

    def set_position(self, x, y):
        """Move button to new position"""
        self.rect.x = x
        self.rect.y = y

    def set_text(self, new_text):
        """Change button text"""
        self.text = new_text







class textzone:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.focused=False
        self.text=""
    def focus(self,mx,my):
        if self.x<=mx<=self.x+self.w and self.y<=my<=self.y+self.h:
            self.focused=True
        else:
            self.focused=False
    def record(self,key):
        if self.focused:
            if key.key==pygame.K_BACKSPACE:
                self.text=self.text[:-1]
            else:
                if len(self.text)<10:
                    self.text+=key.unicode
    def render(self,screen,font):
        zone =pygame.Rect(self.x,self.y,self.w,self.h)
        pygame.draw.rect(screen,pygame.Color('white'),zone)
        txtr=font.render(self.text,True,pygame.Color('black'))
        screen.blit(txtr,(self.x+5,self.y+5))
    
        
        














class object:
    def __init__(self,x,y,w,h,mass,rest,fric,stat,color,name):
        self.name=name
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.mass=mass
        self.rest=rest
        self.fric=fric
        self.static=stat
        self.ax=0
        self.ay=0
        self.vx=0
        self.vy=0
        self.color=color
    def appforce(self,fx,fy):
        if self.static :
            return
        self.ax+=fx/self.mass
        self.ay+=fy/self.mass
    def appimp(self,jx,jy):
        if self.static:
            return
        self.vx+=jx/self.mass
        self.vy+=jy/self.mass
    def update(self,dt):
        if(self.static):
            return
        self.vx+=dt*self.ax
        self.vy+=dt*self.ay
        self.ax=0
        self.ay=0
        self.x+=dt*self.vx
        self.y+=dt*self.vy
    def render(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

#            tbh i ll use the axis aligned bounding box(aabb) we ll upgrade later
class world:
    def __init__(self,gravity,screen,rest):
        self.gravity=gravity
        self.objects=list()
        self.sc=screen
        self.rest=rest
        self.dragged=False
        self.dragging=False
        self.mx=0
        self.my=0
        self.offsetx=0
        self.offsety=0
        
    def addobj(self,obj):
        self.objects.append(obj)
    def appdrag(self):
        if not self.dragging or self.dragged==None:
            return 
        obj=self.dragged
        targetx=self.mx-self.offsetx
        targety=self.my-self.offsety
        dx=targetx-obj.x
        dy=targety-obj.y
        stiff=8000
        dmp=400
        fx=dx*stiff - obj.vx*dmp 
        fy=dy*stiff - obj.vy*dmp
        obj.appforce(fx,fy) 
    
    
    
    
    
    
    def update(self,dt):
        for obj in self.objects:
            obj.appforce(0,self.gravity*obj.mass)
        self.appdrag()
        for obj in self.objects:
            obj.update(dt)
        for a in range(self.objects.__len__()):
            for b in range(a+1,self.objects.__len__()):
                obj_a=self.objects[a]
                obj_b=self.objects[b]
                rvx=obj_b.vx-obj_a.vx
                rvy=obj_b.vy-obj_a.vy
                ox=min(obj_a.x+obj_a.w,obj_b.x+obj_b.w) - max(obj_a.x,obj_b.x)
                oy=min(obj_a.y+obj_a.h,obj_b.y+obj_b.h)-max(obj_a.y,obj_b.y)
                if ox>0 and oy>0:
                    if ox < oy:
                        if obj_b.x+obj_b.w/2 > obj_a.x+obj_a.w/2 :
                            nx=1
                            ny=0
                        else:
                            nx=-1
                            ny=0
                        self.cor=max(ox-0.01,0)*0.4
                    
                    else:
                        if obj_b.y+obj_b.h/2 > obj_a.y+obj_a.h/2 :
                            nx=0
                            ny=1
                        else:
                            nx=0
                            ny=-1  
                        self.cor=max(oy-0.01,0)*0.4
                    vel_n=rvx*nx+rvy*ny

                    if obj_a.static:
                        inv_a=0
                    else:
                        inv_a=1/obj_a.mass
                    if obj_b.static:
                        inv_b=0
                    else:
                        inv_b=1/obj_b.mass
                    tot=inv_a+inv_b
                    if tot==0:
                        continue
                    if vel_n<=0:
                        j=-(1+min(obj_a.rest,obj_b.rest))* vel_n/tot
                        obj_a.appimp(-j*nx,-j*ny)
                        obj_b.appimp(j*nx,j*ny)


                    
                    
                    
                    obj_a.x-=(inv_a/tot)*self.cor*nx
                    obj_b.x+=(inv_b/tot)*self.cor*nx
                    
                    obj_a.y-=(inv_a/tot)*self.cor*ny
                    obj_b.y+=(inv_b/tot)*self.cor*ny
                    
                    
                
                    



    def render(self):
        for obj in self.objects:
            obj.render(self.sc)
    def pick(self,mx,my):
        for obj in self.objects:
            if obj.static:
                continue
            if obj.x<=mx<=obj.x+obj.w and obj.y<=my<=obj.y+obj.h:
                self.dragging=True
                self.dragged=obj
                self.mx=mx
                self.my=my
                self.offsetx=obj.x-mx
                self.offsety=obj.y-my
                return obj
        return None
    def info(self,mx,my):
        ls=list()
        for obj in self.objects:
            if obj.x<=mx<=obj.x+obj.w and obj.y<=my<=obj.y+obj.h:
                list.append(obj.name)
                list.append(str(obj.mass)+" g")
                list.append(str(obj.color))

    def set_mouse(self,mx,my):
        if self.dragging:
            self.mx=mx
            self.my=my
    def release(self):
        self.dragging=False
        self.dragged=None

            

        

