import pygame as pg
from matrix_funtions import *


class Object3D:
    def __init__(self, render):
        self.render = render
        self.vertixes = np.array([(0,0,0,1), (0,1,0,1), (1,1,0,1), (1,0,0,1),
                                  (0,0,1,1), (0,1,1,1), (1,1,1,1), (1,0,1,1)])
        
        self.faces = np.array([(0,1,2,3), (4,5,6,7), (0,4,5,1), (2,3,7,6),
                                 (1,2,6,5),(0,3,7,4)])
        
        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_faces = [(pg.Color('orange'), face) for face in self.faces]
        self.movement_flag, self.draw_vertexes = True, True
        self.label = ''
        
    def draw(self):
        self.screen_projection()
        self.movement()

    def movement(self):
        if self.movement_flag:
            self.rotate_y(pg.time.get_ticks()%0.005)
        
    def screen_projection(self):
        vertexes = self.vertixes @ self.render.camera.camera_matrix()
        vertexes = vertexes @ self.render.projection.projection_matrix
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes[(vertexes>2)|(vertexes<-2)] = 0
        vertexes = vertexes @ self.render.projection.to_screen_matrix
        vertexes = vertexes[:, :2]

        for index, color_face in enumerate(self.color_faces):
            color, face = color_face
            polygon = vertexes[face]
            if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
                pg.draw.polygon(self.render.screen, pg.Color('orange'), polygon, 3)
                if self.label:
                    text = self.font.render(f'{self.label}', True, pg.Color('white'))
                    self.render.screen.blit(text, polygon[0]) 

        if self.draw_vertexes:
            for vertex in vertexes:
                if not np.any((vertex == self.render.H_WIDTH) | (vertex == self.render.H_HEIGHT)):
                    pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 6)
    
    def translate(self, pos):
        self.vertixes = self.vertixes @ translate(pos)
    
    def scale(self, s):
        self.vertixes = self.vertixes @ scale(s)
    
    def rotate_x(self, angle):
        self.vertixes = self.vertixes @ rotate_x(angle)
    
    def rotate_y(self, angle):
        self.vertixes = self.vertixes @ rotate_y(angle)
    
    def rotate_z(self, angle):
        self.vertixes = self.vertixes @ rotate_z(angle)

class Axes(Object3D):
    def __init__(self, render):
        super().__init__(render)
        self.vertixes = np.array([(0,0,0,1), (1,0,0,1), (0,1,0,1), (0,0,1,1)])
        self.faces = np.array([(0,1), (0,2), (0,3)])
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertexes = False
        self.label = 'XYZ'