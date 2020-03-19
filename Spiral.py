import turtle
turtle.bgcolor("pink")
seurat=turtle.Turtle()
width=5
height=7
dot_distance=25
seurat.setpos(-250,250)


def Spiral(m,n):
    k=0
    l=0
    f=0
    seurat.color("red")
    while k<m and l<n:
        if f==1:
            seurat.right(90)

        for i in range(l,n):
            # print(a[k][i],end=' ')
            seurat.forward(dot_distance)
        k+=1
        f=1

        seurat.right(90)
    
        for i in range(k,m):
            # print(a[i][n-1],end=' ')
            seurat.forward(dot_distance)

        n-=1

        seurat.right(90)

        if k<m:
            for i in range(n-1,l-1,-1):
                seurat.forward(dot_distance)
                # print(a[m-1],[i],end=' ')
            m-=1

        seurat.right(90)

        if l<n:
            for i in range(m-1,k-1,-1):
                # print(a[i][l],end=' ')
                seurat.forward(dot_distance)
                
            l+=1
        

Spiral(20,20)
turtle.done()
# a=[]
# count=1
# for i in range(4):
#     l=[]
#     for j in range(4):
#         l.append(count)
#         count+=1
#     a.append(l)
