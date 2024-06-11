from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import os
from django.utils.text import slugify
from dotenv import load_dotenv
from groq import Groq
from .models import ChatGroup, ChatMessage

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


# Create your views here.
def gpt_response(message):
    response = client.chat.completions.create(
        messages=[
            # {
            #     "role": "system",
            #     "content": "you are profiessional teachter you don't know anything else then teaching ",
            # },
            {"role": "user", "content": message},
        ],
        model="llama3-8b-8192",  # Ensure this is the correct model name
    )
    answers = response.choices[0].message.content

    return answers


def chat_bot(request, group_slug=None):
    groups = None
    if request.method == "POST":
        message = request.POST.get("message")
        response = gpt_response(message)

        if request.user.is_authenticated:
            group_name = " ".join(message.split()[:5])
            group, created = ChatGroup.objects.get_or_create(
                user=request.user, name=group_name, slug=slugify(group_name)
            )
            if created:
                group.members.add(request.user)
            new_chat = ChatMessage.objects.create(
                group=group, user=request.user, message=message, response=response
            )
        else:
            # Handle the case where the user is not authenticated
            return JsonResponse({"error": "User is not authenticated"}, status=403)

        return JsonResponse({"response": response}, status=200)

    if request.user.is_authenticated:
        groups = ChatGroup.objects.filter(user=request.user)

    return render(request, "chat/index.html", {"chat_groups": groups})


@login_required
def get_chat_messages(request, group_slug):

    group = get_object_or_404(ChatGroup, slug=group_slug, user=request.user)
    messages = ChatMessage.objects.filter(group=group).order_by("created_at")

    chat_data = []
    for message in messages:
        chat_data.append(
            {
                "picture": message.user.profile.user_photo.url,
                "message": message.message,
                "response": message.response,
                "created_at": message.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    return JsonResponse({"messages": chat_data}, status=200)
