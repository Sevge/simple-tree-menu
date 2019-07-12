from django.shortcuts import render, redirect, HttpResponse
from app01.models import MPTTtree


# Create your views here.

# def get_list(objs):
#     li = []
#     for obj in objs:
#         li.append(obj)
#         children = obj.children.all()
#         if len(children) > 0:
#             li.append(get_list(obj.children.all()))
#     return li
#
#
# def tree_display(request):
#     nodes = Tree.objects.filter(parent=None)
#     result = get_list(nodes)
#     return render(request, 'main.html', {'result': result})

def tree_display(request):
    nodes = MPTTtree.objects.all()
    return render(request, 'main.html', {'nodes': nodes})


def delete_node(request, node_id):
    try:
        MPTTtree.objects.filter(id=node_id).delete()
        return redirect('/tree/')
    except TypeError:
        print('该节点不为空！')
        return HttpResponse('注意：该节点不为空！')


def add_node(request, node_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        if node_id != '0':
            MPTTtree.objects.create(name=name, parent_id=node_id)
        else:
            MPTTtree.objects.create(name=name)
        return redirect('/tree/')
    return render(request, 'add.html')
