from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required
def course_chat_room(request, course_id):
    try:

        course = request.user.course.get(id=course_id)
    
    except:
        print("err")
    
    return render(request, 'chat/room.html', {'course': course})

