from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from images.forms import ImageCreateForm
from images.models import Image
from django.views.decorators.http import require_POST,require_http_methods
from django.http import JsonResponse
from action.utils import create_action

# Create your views here.
@login_required
def image_create(request):
    if request.method == "POST":
        # 表单被提交
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            # 表单验证通过
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            #吧当前用户附加到数据对象上
            new_item.user = request.user
            new_item.save()
            # 行为流 添加图片动作
            create_action(request.user,'添加了图片',new_item)
            messages.success(request,'图片添加成功')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(request.GET)

    return render(request,'images/create.html',{'section':'images','form':form})


def image_detail(request,id,slug):
    """
    :url : /image/detail/
    :param request:
    :param id:  图片的id
    :param slug:  图片的slug字段
    :return: {"image":object,"section":string}
    """
    image = get_object_or_404(Image,id=id,slug=slug)
    return render(request,'images/detail.html',{'image':image,'section':'images'})

@login_required
@require_POST
def image_like(request):
    """
    :param request:
    :return:
    """
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    print(image_id)
    print(action)
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            #多对多字段的管理
            #使用add和remove方法用来添加和删除多对多关系
            #add方法即使传入已经存在的数据对象，也不会重复建立关系
            #remove方法即使传入不存在的数据对象，也不会报错
            if action == 'like':
                image.user_like.add(request.user)
                create_action(request.user,'喜欢了图片',image)
            else:
                image.user_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'error'})

@login_required
def image_list(request):
    images = Image.objects.all()
    return render(request,'images/image_list.html',{'images':images,'section':'images'})