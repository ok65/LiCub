
from licub.licub import LiCub

if __name__ == "__main__":

    a = LiCub()
    b = LiCub()
    c = LiCub()
    d = LiCub()
    print(a.id)
    a.edge[0].connect_to(b.edge[0])
    b.edge[2].connect_to(c.edge[0])
    c.edge[0].connect_to(b.edge[0])

    print(a.where_is(b.id))

    pass