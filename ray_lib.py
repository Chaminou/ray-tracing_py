
import numpy as np

class Vector :
    def __init__(self, coords) :
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]

    def parameters(self) :
        return [self.x,
                self.y,
                self.z,]

    def copy(self) :
        return Vector([self.x, self.y, self.z])

    def to_point(self) :
        return Point(self.parameters())

    def length2(self) :
        return self.x**2 + self.y**2 + self.z**2

    def length(self) :
        return np.sqrt(self.length2())

    def dot(self, u) :
        return self.x*u.x + self.y*u.y + self.z*u.z

    def normalize(self) :
        return self.scalar_mul(1/self.length())

    def me_normalize(self) :
        self.me_scalar_mul(1/self.length())
        return self

    def vect_add(self, u) :
        return Vector([self.x + u.x,
                       self.y + u.y,
                       self.z + u.z,])

    def me_vect_add(self, u) :
        self.x += u.x
        self.y += u.y
        self.z += u.z
        return self

    def vect_diff(self, u) :
        return Vector([self.x - u.x,
                       self.y - u.y,
                       self.z - u.z,])

    def me_vect_diff(self, u) :
        self.x -= u.x
        self.y -= u.y
        self.z -= u.z
        return self

    def scalar_add(self, scalar) :
        return Vector([self.x + scalar,
                       self.y + scalar,
                       self.z + scalar,])

    def me_scalar_add(self, scalar) :
        self.x += scalar
        self.y += scalar
        self.z += scalar

    def scalar_mul(self, scalar) :
        return Vector([self.x*scalar,
                       self.y*scalar,
                       self.z*scalar,])

    def me_scalar_mul(self, scalar) :
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self

    def hadamard_prod(self, u) :
        return Vector([self.x*u.x,
                       self.y*u.y,
                       self.z*u.z,])

    def me_hadamard_prod(self, u) :
        self.x *= u.x
        self.y *= u.y
        self.z *= u.z
        return self

    def hadamard_div(self, u) :
        return Vector([self.x/u.x,
                       self.y/u.y,
                       self.z/u.z,])

    def me_hadamard_div(self, u) :
        self.x /= u.x
        self.y /= u.y
        self.z /= u.z
        return self

    def cross_prod(self, u) :
        return Vector([self.y*u.z - self.z*u.y,
                       self.z*u.x - self.x*u.z,
                       self.x*u.y - self.y*u.x,])

    def me_cross_prod(self, u) :
        temp_x = self.y*u.z - self.z*u.y
        temp_y = self.z*u.x - self.x*u.z
        temp_z = self.x*u.y - self.y*u.x
        self.x = temp_x
        self.y = temp_y
        self.z = temp_z
        return self


class Point :
    def __init__(self, coords) :
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]

    def parameters(self) :
        return [self.x,
                self.y,
                self.z,]

    def copy(self) :
        return Point([self.x, self.y, self.z])

    def to_vector(self) :
        return Vector(self.parameters())

    def vect_translate(self, u) :
        return Point([self.x + u.x,
                      self.y + u.y,
                      self.z + u.z,])

    def me_vect_translate(self, u) :
        self.x = self.x + u.x
        self.y = self.y + u.y
        self.z = self.z + u.z
        return self

    def pt_dist_from(self, p) :
        return Vector([self.x - p.x,
                       self.y - p.y,
                       self.z - p.z,])

    def pt_dist_to(self, p) :
        return Vector([p.x - self.x,
                       p.y - self.y,
                       p.z - self.z,])


class Ray :
    def __init__(self, parameters) :
        self.origin = parameters[0]     # Point object
        self.direction = parameters[1]  # Vector object
        if len(parameters) > 2 :
            self.t_max = parameters[2]  # float
        else :
            self.t_max = 10000000.0     # default value

    def parameters(self) :
        return [self.origin.parameters(),
                self.direction.parameters(),
                self.t_max,]

    def copy(self) :
        return Ray([self.origin.copy(), self.direction.copy(), self.t_max])

    def eval(self, t) :
        return pt_vect_translate(self.origin, self.direction.scalar_mul(t))

#==================== Vector Operator ============================
def vect_dot(u, v) :
    return u.x*v.x + u.y*v.y + u.z*v.z

def vect_add(u, v) :
    return Vector([u.x + v.x,
                   u.y + v.y,
                   u.z + v.z,])

def vect_diff(u, v) :
    return Vector([u.x - v.x,
                   u.y - v.y,
                   u.z - v.z,])

def vect_cross_prod(u, v) :
    return Vector([u.y*v.z - u.z*v.y,
                   u.z*v.x - u.x*v.z,
                   u.x*v.y - u.y*v.x,])

def vect_hadamard_prod(u, v) :
    return Vector([u.x*v.x,
                   u.y*v.y,
                   u.z*v.z,])

def vect_hadamard_div(u, v) :
    return Vector([u.x/v.x,
                   u.y/v.y,
                   u.z/v.z,])

#==================== Point Operator =============================
def pt_dist(p, q) :
    return Vector([p.x - q.x,
                   p.y - q.y,
                   p.z - q.z,])

#==================== Point & Vector Operator ====================
def pt_vect_translate(p, u) :
    return Point([p.x + u.x,
                  p.y + u.y,
                  p.z + u.z,])


if __name__ == '__main__' :
    print("ray_lib.py by Pierre CHAMINADE")
