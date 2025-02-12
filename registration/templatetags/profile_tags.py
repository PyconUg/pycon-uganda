from django import template 

register = template.Library() 

from registration.models import Profile 
 

@register.inclusion_tag('profiles/profilepic_nav.html')
def show_nav_pics():
    show_nav_pic = Profile.objects.all()
    return {'show_nav_pic': show_nav_pic}


@register.inclusion_tag('profiles/profilepic_side.html')
def show_side_pics():
    show_side_pic = Profile.objects.all()
    return {'show_side_pic': show_side_pic}
 