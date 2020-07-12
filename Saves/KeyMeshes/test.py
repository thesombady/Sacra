import os
from SacraMathEngine import vec3d
MeshCube = {
    "South" : [(vec3d(0, 0, 0), vec3d(0, 1, 0), vec3d(1, 1, 0)),
    (vec3d(0, 0, 0), vec3d(1, 1, 0), vec3d(1, 0, 0))],
    "Eash" : [(vec3d(1, 0, 0), vec3d(1, 1, 0), vec3d(1, 1, 1)),
    (vec3d(1, 0, 0), vec3d(1, 1, 1), vec3d(1, 0, 1))],
    "North": [(vec3d(1, 0, 1), vec3d(1, 1, 1), vec3d(0, 1, 1)),
    (vec3d(1, 0, 1), vec3d(0, 1, 1), vec3d(0, 0, 1))],
    "West" : [(vec3d(0, 0, 1), vec3d(0, 1, 1), vec3d(0, 1, 0)),
    (vec3d(0, 0, 1), vec3d(0, 1, 0), vec3d(0, 0, 0))],
    "Top" : [(vec3d(0, 1, 0), vec3d(0, 1, 1), vec3d(1, 1, 1)),
    (vec3d(0, 1, 0), vec3d(1, 1, 1), vec3d(1, 1, 0))],
    "Bottom" : [(vec3d(1, 0, 1), vec3d(0, 0, 1), vec3d(0, 0, 0)),
    (vec3d(1, 0, 1), vec3d(0, 0, 0), vec3d(1, 0, 0))]
}
print(MeshCube)
